#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import re
import redis
import json
import random
import os

import book

class Crawler(object) :
  '抓取器,将根url作为入口,爬取所有url,当格式满足小说目录页的格式时,记下url,然后爬取内容'

  pool = redis.ConnectionPool(host='123.207.41.109', password='foobared')
  urlpfx = "hs_url_"
  bookpfx = "tq_book_"

  def __init__(self, rooturl, bookpattern) :
    self.rootUrl = rooturl
    self.count = 0

    try :
      self.bookPattern = re.compile(bookpattern, re.S)
    except :
        print("小说识别正则表达式有误,请检查后重试!")
        exit()

  def parseStart(self) :
    print("parseStart")
    self.parse(self.rootUrl)
    
    

  def parse(self, curl) :
    self.count += 1
    if (self.count > 128) :
      return
    self.redis = redis.Redis(connection_pool=Crawler.pool)
    self.redis.sadd(Crawler.urlpfx + self.rootUrl, curl)
    
    try :
      page = requests.get(curl)
    except :
      print("错误连接:", curl)
      return

    print("获取网页:", page.status_code, curl)
    if page.status_code != 200 :
      print("链接失效:", curl)
      return
    # 解密之类
    print("count: ", self.count)
    print(self.isBookMenu(page.text))
    if self.isBookMenu(page.text) :
      #加入同步任务队列
      self.redis.lpush(Crawler.bookpfx + self.rootUrl, curl)
      print("加入任务队列", curl)
      return

    # 过滤herf
    pattern = re.compile(r'''href=['"](.+?)['"]''')
    urls = pattern.findall(page.text)

    # 链接查重, 新链接,递归解析
    for suffix in urls :
      print("后缀:", suffix)
      pos = suffix.find("//")
      if -1 != pos or -1 != suffix.find(":") or -1 != suffix.find(".css"):
        # //后直接作为url访问,认为不是本网站,忽略
        pass
      elif len(suffix) > 0 and suffix[0] == '#' :
        # 本页面内的锚点,忽略.
        pass
      elif len(suffix) > 0 and suffix != "/" :
        # 拼接到根url,继续解析
        if suffix[0] == '/' :
          newurl = self.rootUrl + suffix
        else :
        # 拼接到当前url, 继续解析
          newurl = curl + '/' + suffix
        if not self.redis.sismember(Crawler.urlpfx + self.rootUrl, newurl) :
          self.parse(newurl)
          print("Step next level:", newurl)
        print("This url exist: ", newurl)
      else :
        pass

    self.count -= 1

  def syncBook(self, cbfatchinfo, cbgetcontent) :
    '''将任务队列中的书同步到磁盘上,使用两个回调:
    bookinfo, menu = cbfatchinfo(string)
    content = cbgetcontent(chapterurl)
    '''
    print("syncBook")
    self.redis = redis.Redis(connection_pool=Crawler.pool)
    while True :
      curl = self.redis.lpop(Crawler.bookpfx + self.rootUrl)
      print("take url is :", curl)
      self.bookParse(curl, cbfatchinfo, cbgetcontent)
    
  def bookParse(self, curl, cbfatchinfo, cbgetcontent) :
    page = requests.get(curl)
    page.encoding = 'utf-8'
    print(page.text)
    bookinfo, menu = cbfatchinfo(page.text)
    if (bookinfo == None or None == menu) :
      return
    i = 0

    prefix = "./book/" + bookinfo.id
    os.makedirs(prefix)

    bookinfo.record2mysql(host="123.207.41.109", password="MYSQL@yidu", database="yidu_docxor_cn", user="yidu_docxor_cn")
    
    for capter in menu :
      print(capter, capter[0])
      newurl = curl + b"/" + bytes(capter[0], encoding='utf-8')
      print(newurl)
      content = cbgetcontent(newurl)
      print(content)
      fname = bookinfo.chapter_name(i)
      print(bookinfo.id)
      print(fname)
      
      file = open(prefix + "/" + fname, "w")
      file.write("# " + capter[1] + "\n" + content[0])
      file.close()
      i += 1
    
    

  def isBookMenu(self, page) :
    return 0 < len(self.bookPattern.findall(page))


  

def onGetContent(url) :
  page = requests.get(url)
  page.encoding = 'utf-8'
  if len(page.text) > 0 :
    return re.findall(r'''<div id="content">.(.*?).</div>''', page.text, flags=re.S)
  pass



