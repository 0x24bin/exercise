#coding=utf-8
import os
import re
import rsa
import time
import base64
import urllib
import urllib2
import binascii
import cookielib
username=''   #微博账号账号
password=''    #微博密码
filename='weibo_cookie.txt'  #cookie保存地址
file=''  #cookie文件,如果有
pic=['4.jpg','2.jpg']   #微博图片,jpg格式
text="[二哈]"   #微博文本
mid=4025182010233290  #转发微博的mid。开发者模式在"转发"那里
repost_text="[二哈]"   #转发文本

sendurl="http://weibo.com/aj/mblog/add?ajwvr=6&__rnd="+str(int(1000*time.time()))
reposturl="http://weibo.com/aj/v6/mblog/forward?ajwvr=6&__rnd="+str(int(1000*time.time()))
picurl="http://picupload.service.weibo.com/interface/pic_upload.php?app=miniblog&data=1&url=weibo.com&markpos=1&logo=1&marks=1&mime=image/jpeg"
referer_text="http://weibo.com/home?wvr=5"
referer_pid="http://js.t.sinajs.cn/t6/home/static/swf/MultiFilesUpload.swf?version=6bc79d24319630ce"
pattern0=re.compile(r'"pid":"(.*)","name"')
pattern1=re.compile(r'"code":"100000"')
user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'

def test(content):
	t=re.search(pattern1,content)
	if t:
		print "success"
	else:
		print "failed"
def connect(url):
	try:
		result=opener.open(url)
		return result.read()
	except urllib2.HTTPError,e:
		print e.code,e.reason
		os._exit(0)
	except urllib2.URLError,e:
		print e.reason
		os._exit(0)
def post(url,data):
	try:
		result=opener.open(url,data)
		return result.read()
	except urllib2.HTTPError,e:
		print e.code,e.reason
		os._exit(0)
	except urllib2.URLError,e:
		print e.reason
		os._exit(0)
def login(user,passw):
	preurl="https://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=&rsakt=mod&client=ssologin.js(v1.4.18)&_="+str(int(1000*time.time()))
	pattern2=re.compile(r'"servertime":(.*),"pcid"')  #servertime
	pattern3=re.compile(r'"nonce":"(.*)","pubkey"')   #nonce
	pattern4=re.compile(r'"rsakv":"(.*)","exe')   #rsakv
	pattern5=re.compile(r'"pubkey":"(.*)","rsa') #pubbket
	pattern6=re.compile(r'location.replace\(\'(.*)\'\)')
	content=connect(preurl)
	servertime=re.findall(pattern2,content)
	nonce=re.findall(pattern3,content)
	rsakv=re.findall(pattern4,content)
	pubkey=re.findall(pattern5,content)

	#以下部分修改自 http://www.tuicool.com/articles/uQRzIzE

	rsa_public_key=int(pubkey[0],16)
	key = rsa.PublicKey(rsa_public_key, 65537)
	message = str(servertime[0]) + '\t' + str(nonce[0]) + '\n' + str(passw)
	passwd = rsa.encrypt(message, key)
	passwd = binascii.b2a_hex(passwd)
	user = urllib2.quote(user)
	user = base64.encodestring(user)
	form_data = {
        'entry': 'weibo',
        'gateway': '1',
        'from': '',
        'savestate': '7',
        'useticket': '1',
        'pagerefer': 'http://login.sina.com.cn/sso/logout.php?entry=miniblog&r=http://weibo.com/logout.php?backurl=/',
        'vsnf': '1',
        'su': user,
        'service': 'miniblog',
        'servertime': servertime[0],
        'nonce': nonce[0],
        'pwencode': 'rsa2',
        'rsakv': rsakv[0],
        'sp': passwd,
        'sr': '1366*768',
        'encoding': 'UTF-8',
        'prelt': '282',
        'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
        'returntype': 'META'
    }
	form_data = urllib.urlencode(form_data)


	loginurl="http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.18)"
	referer="http://weibo.com/"
	opener.addheaders=[('User-agent',user_agent),('Referer',referer)]
	content=post(loginurl,form_data)
	url=re.findall(pattern6,content)
	connect(url[0])
	cookie.save(ignore_discard=True,ignore_expires=True)
def send(texts,pics=[]):
	if pics:
		pids=[]
		for picss in pics:
			opener.addheaders=[('User-agent',user_agent),('Referer',referer_pid),('Content-Length',os.path.getsize(picss)),('Content-type','application/octet-stream')]
			f=open(picss,"rb")
			content=post(picurl,f.read())
			f.close()
			pid=re.findall(pattern0,content)
			pids.append(pid[0])
		pidd=''
		for pidss in pids:
			if pidss==pids[0]:
				pidd=pidss
			else:
				pidd=pidd+' '+pidss
		opener.addheaders=[('User-agent',user_agent),('Referer',referer_text)]
		data={"location":"v6_content_home","text":texts,"appkey":"","style_type":1,"pic_id":pidd,"pdetail":"","gif_ids":"","rank":0,"rankid":"","module":"stissue","pub_source":"main_","pub_type":"dialog","_t":0}
		postdata=urllib.urlencode(data)
		content=post(sendurl,postdata)
		test(content)
	else:
		opener.addheaders=[('User-agent',user_agent),('Referer',referer_text)]
		data={"location":"v6_content_home","text":texts,"appkey":"","style_type":1,"pic_id":"","pdetail":"","rank":0,"rankid":"","module":"stissue","pub_source":"main_","pub_type":"dialog","_t":0}
		postdata=urllib.urlencode(data)
		content=post(sendurl,postdata)
		test(content)
def repost(reposts,mids):
	data={"pic_src":"","pic_id":"","appkey":"","mid":mids,"style_type":1,"mark":"","reason":reposts,"module":"","page_module_id":"","refer_sort":"","rank":0,"rankid":"","_t":0}
	postdata=urllib.urlencode(data)
	opener.addheaders=[('User-agent',user_agent),('Referer',referer_text)]
	content=post(reposturl,postdata)
	test(content)

if __name__ == '__main__':
	if file:
		cookie=cookielib.MozillaCookieJar()
		cookie.load(file, ignore_discard=True, ignore_expires=True)
		opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
	else:
		cookie=cookielib.MozillaCookieJar(filename)
		opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
		login(username,password)

	send(text)
	#send(text,pic)
	#repost(repost_text,mid)