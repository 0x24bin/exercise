#coding=utf-8
#为了使输出不换行，引入库
#print("haha",end='')
from __future__ import print_function
#定义模逆函数,求逆元
def moni(a,b):
	#初始化
	e=0
	f=1
	z=a
	while 1:
		#计算
		c=a%b
		d=a/b
		g=f
		h=e-f*d
		#复原赋值
		e=g
		f=h
		a=b
		b=c
		#判断
		if c==1:
			if f<0:
				return f+z
			else:
				return f
			break
#字典
dic=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
ab=(3,5,7,9,11,15,17,19,21,23,25)
#要破解的字符串
strs="yfsfnhtzlsrftclhwrffonw"
l=0
while l<len(ab):
	#the key:a,b   
	#y=(ax+b)mod26
	a=ab[l]
	b=0
	#得到逆元
	c=moni(26,a)
	#毅种循环
	while b<26:
		i=0
		while i<len(strs):
			j=dic.index(strs[i])
			k=(c*(j-b))%26
			print(dic[k],end='')
			i=i+1
		print("\n",end='')
		b+=1
	l=l+1
