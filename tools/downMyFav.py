# __author__=xk
# -*- coding: utf-8 -*-
from tools import myRequest
from urllib import urlretrieve
from urllib2 import HTTPError
from urllib2 import urlopen

# if __name__ == '__main__':
#     request = myRequest.Requests()
#     photourl = "https://api.flickr.com/services/rest/?&method=flickr.favorites.getPublicList&api_key=0b20e726fd5a04cb2be8a7177f20deac&user_id=143531823@N07"
#     request.get(photourl)
#     originList = set()
#     photosList = set()
#     file = open(r'C:\Users\xk\PycharmProjects\Coding\res\photoid')
#     for lines in file.readlines():
#         originList.add(lines.strip('\n'))
#
#
#     photoTag = request.getAllLabel("photo")
#     for e in photoTag:
#         photosList.append("https://c5.staticflickr.com/" + e['farm'] + '/' + e['server'] + '/' + e['id'] + '_' + e['secret'] + '_h.jpg')
#     for url in photosList:
#         filename = 'D:/photos/' + url.split('/')[5].split('_')[0] + '.jpg'
#         try:
#             if urlopen(url).geturl() == url:
#                 urlretrieve(url, filename)
#             else:
#                 url = url.split('_h.jpg')[0] + '_b.jpg'
#                 if urlopen(url).geturl() == url:
#                     urlretrieve(url, filename)
#                 # else:
#                 #     photourl = "https://www.flickr.com/photos/vedebe/30122330004/in/faves-143531823@N07/"
#                 #     request.get(photourl)
#                 #     url = 'http:' + request.getAllAttrsValue("img", "src")[1].split('.jpg')[0] + '_h.jpg'
#         except HTTPError as e:
#             print e

if __name__ == '__main__':
    request = myRequest.Requests()
    photourl = "https://api.flickr.com/services/rest/?&method=flickr.favorites.getPublicList&api_key=0b20e726fd5a04cb2be8a7177f20deac&user_id=143531823@N07"
    request.get(photourl)
    originList = set()
    photosList = set()
    file = open(r'C:\Users\xk\PycharmProjects\Coding\res\photoid', 'r')
    for lines in file.readlines():
        originList.add(lines.strip('\n'))

    file = open(r'C:\Users\xk\PycharmProjects\Coding\res\photoid', 'a')
    for id in request.getAllAttrsValue('photo', 'id'):
        photosList.add(id)
    photosList = photosList - originList

    for id in photosList:
        photoSizeUrl = "https://api.flickr.com/services/rest/?method=flickr.photos.getSizes&api_key=e6e96eed7af7deb2d35cac2e3739ed7d&photo_id=" + id
        request.get(photoSizeUrl)
        l = request.getAllAttrsValue('size', 'source')
        downUrl = l[len(l) - 1]
        filename = 'D:\photos' + id + '.jpg'
        urlretrieve(downUrl, filename)
        file.write(id + '\n')
        print id




        # for e in photoTag:
        #     photosList.append("https://c5.staticflickr.com/" + e['farm'] + '/' + e['server'] + '/' + e['id'] + '_' + e[
        #         'secret'] + '_h.jpg')
        # for url in photosList:
        #     filename = 'D:/photos/' + url.split('/')[5].split('_')[0] + '.jpg'
        #     try:
        #         if urlopen(url).geturl() == url:
        #             urlretrieve(url, filename)
        #         else:
        #             url = url.split('_h.jpg')[0] + '_b.jpg'
        #             if urlopen(url).geturl() == url:
        #                 urlretrieve(url, filename)
        #                 # else:
        #                 #     photourl = "https://www.flickr.com/photos/vedebe/30122330004/in/faves-143531823@N07/"
        #                 #     request.get(photourl)
        #                 #     url = 'http:' + request.getAllAttrsValue("img", "src")[1].split('.jpg')[0] + '_h.jpg'
        #     except HTTPError as e:
        #         print e
