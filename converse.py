coding=utf-8
import urllib
import binascii
def converse(string,mode,real):
	#base64编码
	if mode=="base64" and real==1:
		print string.encode("base64")
	#base64解码
	elif mode=="base64" and real==0:
		print string.decode("base64")
	#urlencode编码
	elif mode=="urlencode" and real==1:
		print urllib.quote(string)
	#urlencode解码
	elif mode=="urlencode" and real==0:
		print urllib.unquote(string)
	#字符串转16进制
	elif mode=="0x" and real==1:
		print binascii.hexlify(string)
	#16进制转字符串
	elif mode=="0x" and real==0:
		print binascii.unhexlify(string)
	else:
		print "correct the input please"
#这里是要转换的字符串
string="d2VsY29tZQ=="
#这里是转化函数
#格式为 converse(string,"base64",1)
#"base64"为模式，支持的转化有base64，urlencode，16进制(0x)
#1为判断值，1时进行编码，0时进行解码
converse(string,"base64",0)
#如果想要unicode解码
#print u"\u5B66\u5E74".encode("utf-8")
