#coding=utf-8
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
			return f+z
			break
#字典
dic=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
#the key:a,b   
#y=(ax+b)mod26
a=15
b=23
#要破解的字符串
strs="yfsfnhtzlsrftclhwrffonw"
#得到逆元
c=moni(26,a)
#开始循环
i=0
while i<len(strs):
	j=dic.index(strs[i])
	k=(c*(j-b))%26
	print dic[k],
	i=i+1
