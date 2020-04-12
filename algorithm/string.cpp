#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "string.h"

namespace zsbh {

void str_init(string *p)
{
	assert(NULL != p);

	p->str = NULL;
	p->length = 0;
}

static bool adjust_space(string *p, int lenth)
{
	assert(NULL != p);
	 
	if (NULL == p->str)
	{
		p->str = (char *)malloc(sizeof(char) * lenth);
	}
	else
	{
		p->str = (char *)realloc(p->str, sizeof(char) * lenth);
		
	}
	p->length = lenth;

	return p->str;
}

void str_destory(string *p)
{
	assert(NULL != p);

	if (NULL != p->str)
	{
		free(p->str);
		p->length = 0;
	}
}

void str_assign(string *p, char *str) //�ַ���->����ת��
{
	assert(NULL != p && NULL != str);

	int lenth = strlen(str);
	adjust_space(p, lenth);
	memcpy(p->str, str, sizeof(char) * lenth);

}

void str_copy(string *dst, string *src)
{
	assert(NULL != dst && NULL != src);

	adjust_space(dst, src->length);
	memcpy(dst->str, src->str, sizeof(char) * src->length);

}

bool str_empty(string *p)
{
	assert(NULL != p);

	return !p->length;
}

char str_compare(string *dst, string *src)
{
	assert(NULL != dst && NULL != src);

	for (int i = 0; i < dst->length && i < src->length; i++)
	{
		char ret = 0;
		if (ret = dst->str[i] - src->str[i])
		{
			return ret;
		}
	}

	if (dst->length == src->length)
	{
		return 0;
	}
	else
	{
		return dst->length > src->length ? 1 : -1;
	}
}

int str_length(string *p)
{
	assert(NULL != p);

	return p->length;
}

bool str_sub(string *p, string *n, int pos, int lenth) //�Ӵ���ȡ
{
	assert(NULL != p && NULL != n);

	if (pos >= p->length || lenth >= p->length - pos)
	{
		return false;
	}
	adjust_space(n, lenth);
	memmove(n->str, &p->str[pos], sizeof(char) * lenth);

	return true;
}

int str_str(string *dst, string *src) //BF�㷨
{
	assert(NULL != dst && NULL != src);

	int end = dst->length - src->length;//β

	for (int i = 0; i <= end; )   //����ѭ������
	{
		int j = 0;
		while (j < src->length)
		{
			if (dst->str[i++] != src->str[j++])
			{
				i = i - j + 1;      
				j = -1;
				break;
			}
		}
		if (-1 != j)
		{
			return i - j;
		}

	}
	return -1;
}

void str_insert(string *dst, int pos, string *src)
{
	assert(NULL != dst && NULL != src);

	adjust_space(dst, dst->length + src->length);

	memmove(&dst->str[pos + src->length], &dst->str[pos], dst->length - pos);
	memcpy(&dst->str[pos], src->str, src->length);
}

bool str_delete(string *p, int pos, int lenth)
{
	assert(NULL != p);

	if (pos >= p->length || lenth >= p->length - pos)
	{
		return false;
	}
	memmove(&p->str[pos], &p->str[pos + lenth], sizeof(char) * (p->length - pos - lenth));
	adjust_space(p, p->length - lenth);
	
	return true;
}

void str_replace(string *dst, string *sub, string *src, int pos)
{
	assert(NULL != dst && NULL != sub && NULL != src);

	int end = dst->length - src->length;

	for (int i = pos; i <= end; )   
	{
		int j = 0;
		while (j < src->length)
		{
			if (dst->str[i++] != src->str[j++])
			{
				i = i - j + 1;
				j = -1;
				break;
			}
		}
		if (-1 != j)
		{
			str_replace(dst, sub, src, i);
			str_delete(dst, i - j, sub->length);
			str_insert(dst, i - j, src);
			return;
		}

	}
}

void str_replace_all(string *dst, string *sub, string *src) 
{
	assert(NULL != dst && NULL != sub && NULL != src);

	str_replace(dst, sub, src, 0);
}




void str_cat(string *dst, string *src)
{
	assert(NULL != dst && NULL != src);

	int pos = dst->length;
	adjust_space(dst, dst->length + src->length);

	memcpy(&dst->str[pos], src->str, sizeof(char) * src->length);
}

char str_cmp_ignoreCase(string *dst, string *src)
{
	assert(NULL != dst && NULL != src);

	return true;
}

bool start_with(string *dst, string *prefix)  
{
	assert(NULL != dst && NULL != prefix);

	return false;
}

bool end_with(string dst, string *prefix)   
{
	return false;
}

}