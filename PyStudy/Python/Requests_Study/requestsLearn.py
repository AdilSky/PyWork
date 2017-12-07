#-*-coding:utf-8-*-
# Time:2017/10/12 22:54
# Author:YangYangJun


#开始 requests学习之旅，这里直接在代码编写文字了。

#requests 是python的第三方库，所以这里需要安装

# 直接在命令行窗口执行 pip install requests  即可

#如果提示安装失败，可以参看提示，安装必备软件然后重新安装即可

#安装成功后 即可直接导入

import  requests

#如上不报错即可

#参考资料

#访问网址 http://cn.python-requests.org/zh_CN/latest/  即可查看官方中文文档

#或是查看源代码  https://github.com/requests/requests

#也可到 自己的安装目录下查找 D:/SProgram/Python/Lib/site-packages/requests/api.py 等文件查看介绍


''' requests 接口介绍  '''
# 这部分文档包含了 Requests 所有的接口。对于 Requests 依赖的外部库部分，我们在这里介绍最重要的部分，并提供了规范文档的链接。
#
# 主要接口
# Requests 所有的功能都可以通过以下 7 个方法访问。它们全部都会返回一个 Response 对象的实例。

# 1、request()方法
# requests.request(method, url, **kwargs)   Constructs and sends a Request. 构造和发送请求。
# 这里的参数 method 、 url 是必选参数，**kwargs 是可选参数，是 可变关键字参数，Dictionary 类型
'''
参数:	
method -- method for the new Request object.  
新请求对象的方法
url -- URL for the new Request object.  
新的请求对象的URL
params -- (optional) Dictionary or bytes to be sent in the query string for the Request.  
(可选)在查询字符串中为请求发送的字典或字节。
data -- (optional) Dictionary or list of tuples [(key, value)] (will be form-encoded), bytes, or file-like object to send in the body of the Request.
(可选)字典或元组列表[(键，值)](将以表单编码)、字节或类似文件的对象发送到请求体中。
json -- (optional) json data to send in the body of the Request.
(可选)json数据发送到请求体中。
headers -- (optional) Dictionary of HTTP Headers to send with the Request.
(可选)HTTP报头字典，以发送请求。
cookies -- (optional) Dict or CookieJar object to send with the Request.
(可选)命令或CookieJar对象发送请求。
files -- (optional) Dictionary of 'name': file-like-objects (or {'name': file-tuple}) for multipart encoding upload. file-tuple can be a 2-tuple 
('filename', fileobj), 3-tuple ('filename', fileobj, 'content_type') or a 4-tuple ('filename', fileobj, 'content_type', custom_headers), 
where 'content-type' is a string defining the content type of the given file and custom_headers a dict-like object containing additional 
headers to add for the file.
438/5000  
(可选)“名称”的字典:文件- like- object(或{' name ':file - tuple})，用于多部分编码上传。文件- tuple可以是一个2元组(文件名，fileobj)，
3元组(文件名，fileobj，' content_type ')或一个4元组(' filename '，fileobj，' content_type '，custom_headers)，
其中' content-type '是一个字符串，它定义了给定文件的内容类型和custom_headers，其中包含了一个类似于dict的对象，其中包含了添加文件的附加头文件。

auth -- (optional) Auth tuple to enable Basic/Digest/Custom HTTP Auth.
(可选)Auth tuple来启用Basic /Digest /自定义HTTP Auth。
timeout (float or tuple) -- (optional) How many seconds to wait for the server to send data before giving up, as a float, or a (connect timeout, read timeout) tuple.
(可选)在放弃之前，等待服务器发送数据的时间是多少秒，作为一个浮点数，或者是一个(连接超时，读超时)元组。
allow_redirects (bool) -- (optional) Boolean. Enable/disable GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD redirection. Defaults to True.
(可选)布尔。启用/禁用GET /选项/ POST / PUT /补丁/删除/头重定向。默认值为True。
proxies -- (optional) Dictionary mapping protocol to the URL of the proxy.
(可选)字典映射协议到代理的URL。
verify -- (optional) Either a boolean, in which case it controls whether we verify the server's TLS certificate, or a string, in which case it must be a path to a CA bundle to use. Defaults to True.
(可选)一个布尔值，在这种情况下，它控制我们是否验证服务器的TLS证书，或者是一个字符串，在这种情况下，它必须是一个到CA包使用的路径。默认值为True。
stream -- (optional) if False, the response content will be immediately downloaded.
(可选)如果错误，将立即下载响应内容。
cert -- (optional) if String, path to ssl client cert file (.pem). If Tuple, ('cert', 'key') pair.
(可选)如果字符串，路径到ssl客户机cert文件(. pem)。如果是Tuple(' cert '，' key ')对。
'''


# request()方法实例
req = requests.request('GET', 'http://httpbin.org/get')

print req
# 得到 <Response [200]>

# 2、head()方法


# requests.head(url, **kwargs)
# Sends a HEAD request.  发送一个HEAD 请求。

# Optional arguments that ``request`` takes.  请求获取的可选参数。
r"""Sends a HEAD request.

   :param url: URL for the new :class:`Request` object.
   :param \*\*kwargs: Optional arguments that ``request`` takes.  
   :return: :class:`Response <Response>` object  
   :rtype: requests.Response
   """
# head()方法实例
req = requests.head('http://httpbin.org/get')

print req
# 得到 <Response [200]>



# 3、get()方法

# requests.get(url, params=None, **kwargs)[源代码]
# Sends a GET request.
#
# 参数:
# url -- URL for the new Request object.
# params -- (optional) Dictionary or bytes to be sent in the query string for the Request.
# **kwargs -- Optional arguments that request takes.
# 返回:
# Response object
#
# 返回类型:
# requests.Response

# get()方法实例
req = requests.get('http://httpbin.org/get')

print req
# 得到 <Response [200]>


# 4、post()方法

# requests.post(url, data=None, json=None, **kwargs)[源代码]
# Sends a POST request.
#
# 参数:
# url -- URL for the new Request object.
# data -- (optional) Dictionary (will be form-encoded), bytes, or file-like object to send in the body of the Request.
# json -- (optional) json data to send in the body of the Request.
# **kwargs -- Optional arguments that request takes.
# 返回:
# Response object
#
# 返回类型:
# requests.Response

# post()方法实例
req = requests.post('http://httpbin.org/get')

print req
# 得到 <Response [405]>

# 5、put()方法

# requests.put(url, data=None, **kwargs)[源代码]
# Sends a PUT request.
#
# 参数:
# url -- URL for the new Request object.
# data -- (optional) Dictionary (will be form-encoded), bytes, or file-like object to send in the body of the Request.
# json -- (optional) json data to send in the body of the Request.
# **kwargs -- Optional arguments that request takes.
# 返回:
# Response object
#
# 返回类型:
# requests.Response

# 6、patch()方法

# requests.patch(url, data=None, **kwargs)[源代码]
# Sends a PATCH request.
#
# 参数:
# url -- URL for the new Request object.
# data -- (optional) Dictionary (will be form-encoded), bytes, or file-like object to send in the body of the Request.
# json -- (optional) json data to send in the body of the Request.
# **kwargs -- Optional arguments that request takes.
# 返回:
# Response object
#
# 返回类型:
# requests.Response


# 7、delete()方法

# requests.delete(url, **kwargs)[源代码]
# Sends a DELETE request.
#
# 参数:
# url -- URL for the new Request object.
# **kwargs -- Optional arguments that request takes.
# 返回:
# Response object
#
# 返回类型:
# requests.Response
#



