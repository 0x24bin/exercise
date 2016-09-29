#coding=utf-8
#为了使输出不换行，引入库
#print("haha",end='')
from __future__ import print_function
#字典
dic=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
#要破解的字符串
strs="abcdefghijklmnopqrstuvwxyz};</=23"
#l is the key
l=0
while l<26:
	#初始化
	i=0
	while i<len(strs):
		#判断
		if strs[i] in dic:
			j=dic.index(strs[i])
			k=j+l
			if k<26:
				print(dic[k],end='')
			else:
				print(dic[k-26],end='')
		else:
			print(strs[i],end='')
		i+=1
	print("\n",end='')
	l=l+1
