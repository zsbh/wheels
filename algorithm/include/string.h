#ifndef _ZSBH_STRING_H_
#define _ZSBH_STRING_H_

namespace zsbh {

typedef struct {	
	int length;
	char *str;
} string;

void str_init(string *p);

void str_destory(string *p);

void str_assign(string *p, char *str); 

void str_copy(string *dst, string *src);

bool str_empty(string *p);

char str_compare(string *dst, string *src);

int str_length(string *p);

bool str_sub(string *p, string *n, int pos, int lenth); 

int str_str(string *dst, string *src);

void str_insert(string *dst, int pos, string *src);

bool str_delete(string *p, int pos, int lenth);

void str_replace(string *dst, string *sub, string *src, int pos);

void str_replace_all(string *dst, string *sub, string *src); 


char str_cmp_ignoreCase(string *dst, string *src);

void str_cat(string *dst, string *src);

bool start_with(string *prefix);         

bool end_with(string *prefix);  

}

#endif //!_ZSBH_STRING_H_
