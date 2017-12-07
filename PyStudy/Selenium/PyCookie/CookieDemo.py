#-*-coding:utf-8-*-
# Time:2017/9/23 10:15
# Author:YangYangJun

import requests
#导入配置文件
import baseinfo

#登录访问地址
loginUrl = baseinfo.loginUrl
#请求头
loginHeaders = baseinfo.loginHeaders

#登录后Cookie1
CNBlogsCookie = baseinfo.CNBlogsCookie
#登录后Cookie2
CnblogsAspNetCoreCookies = baseinfo.CnblogsAspNetCoreCookies
#新建随笔方位地址
editUrl = baseinfo.editUrl
#获取session
s = requests.session()

#
#r = s.get(loginUrl,headers = loginHeaders,verify = False )

#获取cookie
c = requests.cookies.RequestsCookieJar()

# 添加登录需要的两个cookie
c.set(".CNBlogsCookie",CNBlogsCookie)
c.set('.Cnblogs.AspNetCore.Cookies',CnblogsAspNetCoreCookies)
#更新cookie
s.cookies.update(c)


body = {"__VIEWSTATE": "",
        "__VIEWSTATEGENERATOR":"FE27D343",
        "Editor$Edit$txbTitle":"这是绕过登录的标题： -*- Bluesky -*-",
        "Editor$Edit$EditorBody":"<p>这里是中文内容：http://www.cnblogs.com/Skyyj/</p>",
        "Editor$Edit$Advanced$ckbPublished":"on",
        "Editor$Edit$Advanced$chkDisplayHomePage":"on",
        "Editor$Edit$Advanced$chkComments":"on",
        "Editor$Edit$Advanced$chkMainSyndication":"on",
        "Editor$Edit$lkbDraft":"存为草稿",
         }
r2 = s.post(editUrl, data=body, verify=False)
#获取请求返回的响应信息
print r2.content


