# client-crawler
目前这个项目只能爬取新浪微博的内容，根据搜索关键字爬取一天内更新的微博。

# pre-install
由于新浪更新了版本，原始网页都是二进制，不好爬，需要使用webdriver 进行解析然后才能进行爬取，所以使用了selenium+phantomjs进行爬取。

本地需要使用pip安装selenium，并且需要下载，安装phantomjs:

```shell
pip install selenium
npm install phantomjs
```

由于Mac上面的文件系统限制，建议使用virtualenv安装selenium，win和linux可以随意。另外，phantomjs的下载也是很慢的，建议直接去github上面找到下载链接然后开迅雷。

# How to Use
目前新浪微博使用cookie登录。因为哪怕使用用户名密码也一样会有验证码的问题，还不如干脆每天换个验证码呢：

```shell
#设置SINA_COOKIE环境变量
SINA_COOKIE=SINAGLOBAL=4284585.158.1472283501553; _s_tentry=login.sina.com.cn; Apache=2759536782836.5757.147524550; ULV=1470024593:4:3:1:2759536782836.5757.1475220024550:1474189056612; login_sid_t=7a271b7753ef657e81143db0; appkey=; user_active=2610051657; user_unver=cbe1bb2ccd25a6d33893db8; SSOLoginState=15658271; un=18582087@126.com; wvr=6; SCF=ArwfV5ggqj2Y4hJQsJBnVMtnE8Od9dO_vUb-COlkBltismI5wpX2Dh_xPpvPSJ6bXTFRmuyurLwdOfTSJUhfr7c.; SUB=_2A256_D_qDeTxGeBO6FUV9ynFyDuIHXVZiBYirDV8PUNbmtBeLVf4kW8Xf9wpqmXoXj6HNqG-B95zgLi4Dg..; SUBP=0033WrqPxfM725Ws9jqgMF55529P9D9Whxig5vcjqJ-yJTnX219W7y5JpX5KMhUgL.Foq7e0MXS0M4e0M2dJLoIpWP9gi29P9Ldsv79Pz7eh.R; SUHB=0d4urJ-k3X0Xip; ALF=1507427129; UOR=www.cctime.com,widget.weibo.com,login.sina.com.cn
```
这是从chrome里面的cookie头直接复制出来的cookie，代码里面使用分号切割，然后根据等号切关键字和数值。

目前还没有完全成型，所以调用还是很随意的：

``` shell
cd src
python sina.py ${key_word}
```

将key_word替换成想搜索的关键字即可

