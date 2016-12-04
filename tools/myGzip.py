# __author__=xk
# -*- coding: utf-8 -*-
import StringIO, gzip


# 解压
def gzipDecode(encodedData):
    compressedStream = StringIO.StringIO(encodedData)
    gziper = gzip.GzipFile(fileobj=compressedStream)
    decodeData = gziper.read()  # 读取解压缩后数据
    return decodeData


# 压缩
def gzipEncode(encodeData):
    buf = StringIO.StringIO()
    gziper = gzip.GzipFile(mode='wb', fileobj=buf)
    gziper.write(encodeData)  # 读取压缩后数据
    gziper.close()
    return buf.getvalue()


if __name__ == '__main__':
    import urllib, urllib2, cookielib
    from urllib2 import urlopen
    import StringIO, gzip
    from  bs4 import BeautifulSoup

    cookie = cookielib.CookieJar()

    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

    urllib2.install_opener(opener)

    # Open Login for openid

    url = "https://openid.stackexchange.com/account/login"

    response = urllib2.urlopen(url)

    content = response.read()

    pos = content.find('<input type="hidden" name="fkey"')

    fkey = content[pos + 40: pos + 76]

    # Login Submit for openid

    url = "https://openid.stackexchange.com/account/login/submit"

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Context-type": "application/x-www-form-urlencoded",
        "Origin": "https://openid.stackexchange.com",
        "Referer": "https://openid.stackexchange.com/account/login",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
    }

    post_data = urllib.urlencode({
        "email": "zzrabs@gmail.com",
        "password": "stack@18846542",
        "fkey": fkey
    })

    req = urllib2.Request(url, post_data, headers)

    try:
        response = opener.open(req)

    except Exception, ex:
        print "login_error"
        exit()

    data = response.read()
    s = gzipDecode(data)
    s = gzipEncode(s)
    s = gzipDecode(s)
    print type(s)
    data = StringIO.StringIO(data)
    gzipper = gzip.GzipFile(fileobj=data)
    html = gzipper.read()
