# __author__=xk
# -*- coding: utf-8 -*-



if __name__ == '__main__':
    from urllib2 import Request
    from urllib2 import urlopen
    from urllib import urlencode
    from bs4 import BeautifulSoup
    import hashlib

    secret = '81596b5796db85c3'
    api_key = '3d7218133aa1fc6cb757b74f4842ded7'
    method = 'flickr.auth.getFrob'
    src = secret + 'api_key' + api_key + 'method' + method
    m2 = hashlib.md5()
    m2.update(src)
    api_sig = m2.hexdigest()

    url = "https://api.flickr.com/services/rest/?&method=flickr.auth.getFrob&api_key=" + \
          api_key + '&api_sig=' + api_sig
    bsob = BeautifulSoup(urlopen(url), "html.parser")

    frob = str(bsob.find('frob').get_text())
    perms = "read"
    src = secret + 'api_key' + api_key + 'frob' + frob + 'perms' + perms
    m2 = hashlib.md5()
    m2.update(src)
    api_sig = m2.hexdigest()

    url = "https://www.flickr.com/services/auth/?api_key=" + api_key + "&perms=read&frob=" + frob + "&api_sig=" + api_sig
    print url
    header = {'accept-encoding': 'gzip, deflate, br', \
              'accept-language': 'zh-CN,zh;q=0.8', \
              'cache-control': 'max-age=0', \
              'content-length': '229', \
              'content-type': 'application/x-www-form-urlencoded', \
              'origin': 'https://www.flickr.com',
              'referer': url}

    print "Starting Post Data "
    magic_cookie = "caaad4f0e0f75faf563b8b3639e059badd1e9886f31c075e55ce86e3165b7a27"
    url = "https://www.flickr.com/services/auth/"
    formdata = {"magic_cookie": magic_cookie, "aki_key": api_key, "perms": "read", "frob": frob, "done_auth": 1}
    data = urlencode(formdata)
    req = Request(url, data)
    fd = urlopen(req)
    print fd.read()

    src = secret + 'api_key' + api_key + 'frob' + frob + 'methodflickr.auth.getToken'
    m2 = hashlib.md5()
    m2.update(src)
    api_sig = m2.hexdigest()
    url = "https://api.flickr.com/services/rest/?&method=flickr.auth.getToken&api_key=" + api_key + "&frob=" + frob + "&api_sig=" + api_sig
    print url
    bsob = BeautifulSoup(urlopen(url), "html.parser")
    print str(bsob.find("token").get_text())






    # caaad4f0e0f75faf563b8b3639e059badd1e9886f31c075e55ce86e3165b7a27
    # magic_cookie:magic_cookie
    # api_key:bfefc988a3a7c852823d414ae917a785
    # api_sig:0
    # f390966605c9d6b66ed044cc20d5254
    # perms:read
    # frob:72157674815276106 - 6
    # c425768474f68d4 - 546261
    # done_auth:1
    # https: // www.flickr.com / services / auth /
