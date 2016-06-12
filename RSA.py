#coding=utf-8
#16进制转化库
#import binascii
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
#取两个质数p，q
p=473398607161
q=4511491
#计算数据
#i为p-1,q-1的乘积
#e为1<e<l且与l互质的一个数
#e*dmodi=1,即模逆
n=p*q
i=(p-1)*(q-1)
e=17
d=moni(i,e)
#加密
#密文为  明文^e MOD n
#例如 123^e%n,123为明文
def jiami(a):
	return a**e%n
#解密
#明文为  密文^d MOD n
#例如 225^d%n,225为密文 
def jiemi(a):
	return a**d%n
#如果数字很大，运算时间会很长，建议手动
print jiami(32762643845309729)
#如果采用16进制对应字符串
#16进制转10进制
#a=eval(a)
#10进制转16进制
#a=hex(a)
#16进制转字符串
#a=binascii.unhexlify(a)
