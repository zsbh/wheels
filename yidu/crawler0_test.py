#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re

generpage = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<script type="text/javascript" src="/js/m.js"></script>
<title>修真四万年无弹窗_修真四万年最新章节列表_笔趣阁</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<meta name="keywords" content="修真四万年,修真四万年无弹窗" />
<meta name="description" content="修真四万年无弹窗最新章节由网友提供，《修真四万年》情节跌宕起伏、扣人心弦，是一本情节与文笔俱佳的科幻小说，笔趣阁免费提供修真四万年最新清爽干净的文字章节在线阅读。" />
<meta http-equiv="Cache-Control" content="no-transform" />
<meta http-equiv="Cache-Control" content="no-siteapp" />
<meta http-equiv="mobile-agent" content="format=html5; url=https://m.biquke.com/bq/22/22682/" />
<meta http-equiv="mobile-agent" content="format=xhtml; url=https://m.biquke.com/bq/22/22682/" />
<meta property="og:type" content="novel"/>
<meta property="og:title" content="修真四万年"/>
<meta property="og:description" content="“这是一艘‘鸿钧’级晶石战舰，重三亿九千万吨，由一千五百二十三名炼气期修真者操纵，主控晶脑每秒运算九千万道神念，‘计算力’堪比元婴老怪，可以瞬息镇压一个星球！”
李耀卓立于无尽星海之上，看着眼前的庞然大物，心中默默计算：
“把这艘战舰拆成废铁，我需要——7秒钟！”
……
修真40000年代，一个普普通通的边境少年，咆哮星辰，主宰银河的热血传奇！"/>
<meta property="og:image" content="https://www.biquke.com/files/article/image/22/22682/22682s.jpg"/>
<meta property="og:novel:category" content="科幻小说"/>
<meta property="og:novel:author" content="卧牛真人"/>
<meta property="og:novel:book_name" content="修真四万年"/>
<meta property="og:novel:read_url" content="https://www.biquke.com/bq/22/22682/"/>
<meta property="og:novel:status" content="连载中"/>
<meta property="og:novel:update_time" content="2019-04-08 10:00"/>
<meta property="og:novel:latest_chapter_name" content="韩特传（六十四）逃亡之旅"/>
<meta property="og:novel:latest_chapter_url" content="https://www.biquke.com/bq/22/22682/11867557.html"/>
<link rel="stylesheet" type="text/css" href="/css/common.css"/>
<link rel="stylesheet" type="text/css" href="/css/list.css"/>
<script type="text/javascript" src="https://libs.baidu.com/jquery/1.4.2/jquery.min.js"></script>
<script language="javascript" type="text/javascript">var bookid = "22682"; var booktitle = "修真四万年";</script>
<script type="text/javascript" src="/js/common.js"></script>
<script type="text/javascript" src="/js/bqg.js"></script>
<script type="text/javascript" src="/js/btn.js"></script>
</head>
<body>
<div id="wrapper">
<div class="ywtop">
<div class="ywtop_con">
<div class="ywtop_sethome"><a onclick="this.style.behavior='url(#default#homepage)';this.setHomePage('https://www.biquke.com/');" href="#">将笔趣阁设为首页</a></div>
<div class="ywtop_addfavorite"><a href="javascript:window.external.addFavorite('https://www.biquke.com/','笔趣阁_书友最值得收藏的网络小说阅读网')">收藏笔趣阁</a></div>
<script language="javascript" src="/js/denglu.js"></script>
</div>
</div>
<div class="header">
<div class="header_logo"><a href="https://www.biquke.com/">笔趣阁</a></div>
<script>list_panel();</script>
</div>
<div class="nav">
<ul>
<li><a href="/">首页</a></li>
<li><a href="/xuanhuan/">玄幻小说</a></li>
<li><a href="/xiuzhen/">修真小说</a></li>
<li><a href="/dushi/">都市小说</a></li>
<li><a href="/chuanyue/">穿越小说</a></li>
<li><a href="/wangyou/">网游小说</a></li>
<li><a href="/kehuan/">科幻小说</a></li>
<li><a href="/paihangbang/">排行榜单</a></li>
<li><a href="/wanjiexiaoshuo/">全本小说</a></li>
<li><a href="/modules/article/bookcase.php">我的书架</a></li>
</ul>'''

menupage = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<script type="text/javascript" src="/js/m.js"></script>
<title>三寸人间无弹窗_三寸人间最新章节列表_笔趣阁</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<meta name="keywords" content="三寸人间,三寸人间无弹窗" />
<meta name="description" content="三寸人间无弹窗最新章节由网友提供，《三寸人间》情节跌宕起伏、扣人心弦，是一本情节与文笔俱佳的修真小说，笔趣阁免费提供三寸人间最新清爽干净的文字章节在线阅读。" />
<meta http-equiv="Cache-Control" content="no-transform" />
<meta http-equiv="Cache-Control" content="no-siteapp" />
<meta http-equiv="mobile-agent" content="format=html5; url=https://m.biquke.com/bq/43/43961/" />
<meta http-equiv="mobile-agent" content="format=xhtml; url=https://m.biquke.com/bq/43/43961/" />
<meta property="og:type" content="novel"/>
<meta property="og:title" content="三寸人间"/>
<meta property="og:description" content="举头三尺无神明，掌心三寸是人间。这是耳根继《仙逆》《求魔》《我欲封天》《一念永恒》后，创作的第五部长篇小说《三寸人间》。"/>
<meta property="og:image" content="https://www.biquke.com/files/article/image/43/43961/43961s.jpg"/>
<meta property="og:novel:category" content="修真小说"/>
<meta property="og:novel:author" content="耳根"/>
<meta property="og:novel:book_name" content="三寸人间"/>
<meta property="og:novel:read_url" content="https://www.biquke.com/bq/43/43961/"/>
<meta property="og:novel:status" content="连载中"/>
<meta property="og:novel:update_time" content="2019-04-11 11:49"/>
<meta property="og:novel:latest_chapter_name" content="第593章 拜宫阁！"/>
<meta property="og:novel:latest_chapter_url" content="https://www.biquke.com/bq/43/43961/11928010.html"/>
<link rel="stylesheet" type="text/css" href="/css/common.css"/>
<link rel="stylesheet" type="text/css" href="/css/list.css"/>
<script type="text/javascript" src="https://libs.baidu.com/jquery/1.4.2/jquery.min.js"></script>
<script language="javascript" type="text/javascript">var bookid = "43961"; var booktitle = "三寸人间";</script>
<script type="text/javascript" src="/js/common.js"></script>
<script type="text/javascript" src="/js/bqg.js"></script>
<script type="text/javascript" src="/js/btn.js"></script>
</head>
<body>
<div id="wrapper">
<div class="ywtop">
<div class="ywtop_con">
<div class="ywtop_sethome"><a onclick="this.style.behavior='url(#default#homepage)';this.setHomePage('https://www.biquke.com/');" href="#">将笔趣阁设为首页</a></div>
<div class="ywtop_addfavorite"><a href="javascript:window.external.addFavorite('https://www.biquke.com/','笔趣阁_书友最值得收藏的网络小说阅读网')">收藏笔趣阁</a></div>
<script language="javascript" src="/js/denglu.js"></script>
</div>
</div>
<div class="header">
<div class="header_logo"><a href="https://www.biquke.com/">笔趣阁</a></div>
<script>list_panel();</script>
</div>
<div class="nav">
<ul>
<li><a href="/">首页</a></li>
<li><a href="/xuanhuan/">玄幻小说</a></li>
<li><a href="/xiuzhen/">修真小说</a></li>
<li><a href="/dushi/">都市小说</a></li>
<li><a href="/chuanyue/">穿越小说</a></li>
<li><a href="/wangyou/">网游小说</a></li>
<li><a href="/kehuan/">科幻小说</a></li>
<li><a href="/paihangbang/">排行榜单</a></li>
<li><a href="/wanjiexiaoshuo/">全本小说</a></li>
<li><a href="/modules/article/bookcase.php">我的书架</a></li>
</ul>
</div>
<div class="dahengfu"><script type="text/javascript">list_top();</script></div>
<div class="box_con">
<div class="con_top">
<div id="bdshare" class="bdshare_b" style="line-height: 12px;"><img src="https://bdimg.share.baidu.com/static/images/type-button-7.jpg"/><a class="shareCount"></a></div>
<a href="/">笔趣阁</a> &gt; <a href="/xiuzhen/">修真小说</a> &gt; 三寸人间最新章节列表
</div>
<div id="maininfo">
<div id="info">
<h1>三寸人间</h1>
<p>作&nbsp;&nbsp;&nbsp;&nbsp;者:耳根</p>
<p>类&nbsp;&nbsp;&nbsp;&nbsp;别:修真小说</p>
<p>最&nbsp;&nbsp;&nbsp;&nbsp;新：<a href="11928010.html">第593章 拜宫阁！</a></p>
<p>日&nbsp;&nbsp;&nbsp;&nbsp;期：2019-04-11 11:49</p>
<p>动&nbsp;&nbsp;&nbsp;&nbsp;作:<a href="Javascript:void(0);" onclick="javascript:addbookcase(43961);">加入书架</a>, <a href="Javascript:void(0);" onclick="javascript:vote(43961);">投推荐票</a>, <a href="#footer">直达底部</a></p>
</div>
<div id="intro">
<p> 举头三尺无神明，掌心三寸是人间。这是耳根继《仙逆》《求魔》《我欲封天》《一念永恒》后，创作的第五部长篇小说《三寸人间》。</p>
<p>本站提示：各位书友要是觉得《三寸人间》还不错的话请不要忘记向您QQ群和微博里的朋友推荐哦！</p>
</div>
</div>
<div id="sidebar">
<div id="fmimg">
<img width="120" height="150" src="/files/article/image/43/43961/43961s.jpg" onerror="src='/modules/article/images/nocover.jpg'" alt="三寸人间"/>
<span class="b"></span>
</div>
</div>
<div id="listtj">&nbsp;推荐阅读：<a href="/bq/3/3714/" target="_blank">飞剑问道</a>、<a href="/bq/0/372/" target="_blank">元尊</a>、<a href="/bq/0/990/" target="_blank">凡人修仙传仙界篇</a>、<a href="/bq/48/48551/" target="_blank">天下第九</a>、<a href="/bq/23/23102/" target="_blank">不朽凡人</a>、<a href="/bq/0/248/" target="_blank">帝尊</a>、<a href="/bq/43/43961/" target="_blank">三寸人间</a>、<a href="/bq/0/754/" target="_blank">修仙狂徒</a>、<a href="/bq/50/50908/" target="_blank">重生西游之齐天大圣</a>、<a href="/bq/43/43518/" target="_blank">全职武神</a>、<a href="/bq/0/23/" target="_blank">莽荒纪</a>、<a href="/bq/19/19743/" target="_blank">仙路至尊</a>、<a href="/bq/52/52078/" target="_blank">一品修仙</a>、<a href="/bq/52/52064/" target="_blank">大夏纪</a> </div>
</div>
<script type="text/javascript">list_middle();</script>
<div class="box_con">
<div id="list">
<dl>
<dd><a href="12247043.html" title="写在连载前">写在连载前</a></dd>
<dd><a href="12247044.html" title="第一章 我要减肥！">第一章 我要减肥！</a></dd>
<dd><a href="5134012.html" title="第二章 王宝乐，你干了什么！">第二章 王宝乐，你干了什么！</a></dd>
<dd><a href="5139159.html" title="第三章 好同学，一切有我！">第三章 好同学，一切有我！</a></dd>
<dd><a href="5140032.html" title="第四章 飘渺道院">第四章 飘渺道院</a></dd>
<dd><a href="5140413.html" title="第五章 特招学子">第五章 特招学子</a></dd>
<dd><a href="5143733.html" title="第六章 麻烦大了">第六章 麻烦大了</a></dd>
<dd><a href="5144627.html" title="第七章 全民矿工">第七章 全民矿工</a></dd>
<dd><a href="5148408.html" title="第八章 才智与反击！">第八章 才智与反击！</a></dd>
<dd><a href="5149350.html" title="第九章 太虚噬气诀！">第九章 太虚噬气诀！</a></dd>
<dd><a href="5153429.html" title="第十章 无敌战武系">第十章 无敌战武系</a></dd>
<dd><a href="5154339.html" title="第十一章 老师，带我一个">第十一章 老师，带我一个</a></dd>
<dd><a href="5158132.html" title="第十二章 突破">第十二章 突破</a></dd>
<dd><a href="5159017.html" title="第十三章 化清丹">第十三章 化清丹</a></dd>
<dd><a href="5162903.html" title="第十四章 法兵系的优势">第十四章 法兵系的优势</a></dd>
<dd><a href="5163759.html" title="第十五章 这就是抢钱！">第十五章 这就是抢钱！</a></dd>
<dd><a href="5167597.html" title="第十六章 上品灵石">第十六章 上品灵石</a></dd>
<dd><a href="5168455.html" title="第十七章 专门欺负我们战武系？">第十七章 专门欺负我们战武系？</a></dd>
<dd><a href="5172156.html" title="第十八章 封身境">第十八章 封身境</a></dd>
<dd><a href="5172994.html" title="第十九章 太虚擒拿术">第十九章 太虚擒拿术</a></dd>
<dd><a href="5176666.html" title="第二十章 搏击俱乐部">第二十章 搏击俱乐部</a></dd>
<dd><a href="5177533.html" title="第二十一章 叫爸爸！">第二十一章 叫爸爸！</a></dd>
<dd><a href="5181107.html" title="第二十二章 碎了……">第二十二章 碎了……</a></dd>
<dd><a href="5182004.html" title="第二十三章 无耻胖兔">第二十三章 无耻胖兔</a></dd>
<dd><a href="5185665.html" title="第二十四章 我不和你打">第二十四章 我不和你打</a></dd>
<dd><a href="5186540.html" title="第二十五章 太虚擒拿术大成">第二十五章 太虚擒拿术大成</a></dd>
<dd><a href="5190297.html" title="第二十六章 鄙人谢海洋">第二十六章 鄙人谢海洋</a></dd>
<dd><a href="5191167.html" title="第二十七章 死神丹！">第二十七章 死神丹！</a></dd>
<dd><a href="5194884.html" title="第二十八章 封身大圆满">第二十八章 封身大圆满</a></dd>
<dd><a href="5195720.html" title="第二十九章 毫不犹豫！">第二十九章 毫不犹豫！</a></dd>
<dd><a href="5199457.html" title="第三十章 申请考核！">第三十章 申请考核！</a></dd>
<dd><a href="5200439.html" title="第三十一章 强势！">第三十一章 强势！</a></dd>
<dd><a href="5203887.html" title="第三十二章 整肃门户">第三十二章 整肃门户</a></dd>
<dd><a href="5204739.html" title="第三十三章 柳道斌的天赋">第三十三章 柳道斌的天赋</a></dd>
<dd><a href="5208212.html" title="第三十四章 法兵土豪">第三十四章 法兵土豪</a></dd>
<dd><a href="5209027.html" title="第三十五章 草木学首郑良">第三十五章 草木学首郑良</a></dd>
<dd><a href="5212471.html" title="第三十六章 人才柳道斌">第三十六章 人才柳道斌</a></dd>
<dd><a href="5213301.html" title="第三十七章 联邦构架">第三十七章 联邦构架</a></dd>
<dd><a href="5216767.html" title="第三十八章 道歉！">第三十八章 道歉！</a></dd>
<dd><a href="5217627.html" title="第三十九章 资格？">第三十九章 资格？</a></dd>
<dd><a href="5221099.html" title="第四十章 学首变革">第四十章 学首变革</a></dd>
<dd><a href="5221867.html" title="第四十一章 青木湖畔的惨叫">第四十一章 青木湖畔的惨叫</a></dd>
<dd><a href="5225420.html" title="第四十二章 干掉他们！">第四十二章 干掉他们！</a></dd>
</dl>
</div></div>
<div class="dahengfu"><script type="text/javascript">list_bot();</script></div>
<div id="footer" name="footer">
<div class="footer_link">
新书推荐：
<a href="/bq/0/372/" target="_blank"><b>元尊</b></a>、
<a href="/bq/3/3714/" target="_blank"><b>飞剑问道</b></a>、
<a href="/bq/69/69959/" target="_blank"><b>王小六的修炼生活</b></a>、
<a href="/bq/69/69946/" target="_blank"><b>一仙难球</b></a>、
<a href="/bq/69/69936/" target="_blank"><b>弃少归来</b></a>、
<a href="/bq/69/69913/" target="_blank"><b>万古第一仙</b></a>、
<a href="/bq/69/69911/" target="_blank"><b>诸天之道叩洪荒</b></a>、
<a href="/bq/69/69889/" target="_blank"><b>我一拳超神</b></a>、
<a href="/bq/69/69876/" target="_blank"><b>黄山修道士</b></a>、
<a href="/bq/69/69863/" target="_blank"><b>仙诛昊</b></a>、
<a href="/bq/69/69857/" target="_blank"><b>绝品神女攻略</b></a>、
<a href="/bq/69/69856/" target="_blank"><b>我七岁就成了仙帝</b></a>、
</div>
<div class="footer_cont">
<p>《三寸人间》情节跌宕起伏、扣人心弦，是一本情节与文笔俱佳的修真小说,笔趣阁转载收集三寸人间最新章节。</p>
<script type="text/javascript">footer();</script>
</div>
</div>
<script>recordedclick(43961);</script>
</body>
</html>
'''

# from redis import StrictRedis

# redis = StrictRedis(host='123.207.41.109', password='foobared')
# redis.set('hello', 'world')
# print(redis.get("hello"))
# print(redis.get("foo"))


infostr = r'''og:title" +content="(.*?)".*
.*og:description" +content="(.*?)".*
.*og:image" +content="(.*?)".*
.*og:novel:category" +content="(.*?)".*
.*og:novel:author" +content="(.*?)".*
.*og:novel:book_name" +content="(.*?)".*
.*og:novel:read_url" +content="(.*?)".*
.*og:novel:status" +content="(.*?)".*
.*og:novel:update_time" +content="(.*?)".*
.*og:novel:latest_chapter_name" +content="(.*?)".*
<dl>
(<dd><a +href="(.*?)" +title="(.*?)">.*).+
</dl>'''



# pattern = re.compile(r'''href=['"](.+?)['"]''')
# pattern = re.compile(infostr, flags=re.S)
# urls = pattern.findall(menupage)

# print(urls)
'''
suffix = "/xuanhuan/"
if -1 != suffix.find("//") or -1 != suffix.find(":") or -1 != suffix.find(".css"):
        # //后直接作为url访问,认为不是本网站,忽略
  print(1)
elif len(suffix) > 0 and suffix[0] == '#' :
        # 本页面内的锚点,忽略.
  print(2)
elif len(suffix) > 0 and suffix != "/" :
        # 拼接到根url,继续解析
  if suffix[0] == '/' :
    print(3)
  else :
    # 拼接到当前url, 继续解析
    print(4)
  print(5)
else :
  print(6)
'''
'''
import yidu
import book
import redis



bi0 = yidu.Biquke0('https://www.biquke.com')
bi0.run()
'''
"""
rds = redis.Redis(host="123.207.41.109", password="foobared")
while True :
  curl = rds.lpop(name="tq_book_" + "https://www.biquke.com")
  print("take url is :", curl)
  bi1 = yidu.Biquke1(curl)
  bi1.run()

"""
"""
import threading

pattern = re.compile(yidu.Biquke0.goalmode, flags=re.S)
res = pattern.findall(menupage)
print(res)
"""

import book

def onBookInfo(content) :
  info = re.findall(infostr, content, flags=re.S)[0]
  if (len(info) < 11) :
    print("parse error")
    return None, None
  menu = re.findall(r'''<dd><a +href="(.*?)" +title="(.*?)">''', info[10], flags=re.S)
  
  b = book.Book(imageurl=info[2], realurl=info[6], name=info[0], author=info[4],
    category=info[3], status=info[7], descrip=info[1], cnum=len(menu))
  print(menu)
  return b, menu



import crawler0
import threading
import mysql.connector

cr = crawler0.Crawler(rooturl='https://www.biquke.com', bookpattern=infostr)

def wrapcrawler(crl) :
  crl.parseStart()

def warpdown(crl) :
  crl.syncBook(onBookInfo, crawler0.onGetContent)

# th1 = threading.Thread(target=crawler.Crawler.parseStart, args=(cr,))
th2 = threading.Thread(target=crawler0.Crawler.syncBook, args=(cr, onBookInfo, crawler0.onGetContent))
# th1.start()
# conn = mysql.connector.connect(host="123.207.41.109", password="MYSQL@yidu", database="yidu_docxor_cn", user="root")
# print(conn)
th2.start()
# import requests

# l = list(infostr)
# l.reverse()
# str = ""
# print(str.join(l))
# ct = requests.get('https://www.biquke.com/bq/43/43961/')
# ct.encoding = 'utf-8'
# onBookInfo(ct.text)

