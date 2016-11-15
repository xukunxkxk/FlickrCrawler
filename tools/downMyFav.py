# __author__=xk
# -*- coding: utf-8 -*-
from tools import myRequest
from urllib import urlretrieve
from urllib2 import HTTPError
from urllib2 import urlopen

if __name__ == '__main__':
    request = myRequest.Requests()
    photourl = "https://api.flickr.com/services/rest/?&method=flickr.favorites.getPublicList&api_key=0b20e726fd5a04cb2be8a7177f20deac&user_id=143531823@N07"
    request.get(photourl)
    photosList = []
    photoTag = request.getAllLabel("photo")
    for e in photoTag:
        photosList.append("https://c5.staticflickr.com/" + e['farm'] + '/' + e['server'] + '/' + e['id'] + '_' + e['secret'] + '_h.jpg')
    for url in photosList:
        filename = 'D:/photos/' + url.split('/')[5].split('_')[0] + '.jpg'
        try:
            if urlopen(url).geturl() == url:
                urlretrieve(url, filename)
            else:
                url = url.split('_h.jpg')[0] + '_b.jpg'
                if urlopen(url).geturl() == url:
                    urlretrieve(url, filename)
                # else:
                #     photourl = "https://www.flickr.com/photos/vedebe/30122330004/in/faves-143531823@N07/"
                #     request.get(photourl)
                #     url = 'http:' + request.getAllAttrsValue("img", "src")[1].split('.jpg')[0] + '_h.jpg'
        except HTTPError as e:
            print e





