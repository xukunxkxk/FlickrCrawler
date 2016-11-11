# __author__=xk
# -*- coding: utf-8 -*-
from tools import myRequest
from time import ctime


if __name__ == '__main__':
    request = myRequest.Requests()
    URL = "https://api.flickr.com/services/rest/?&method=flickr.people.getPublicPhotos&api_key=e6e96eed7af7deb2d35cac2e3739ed7d&user_id=100007433@N06&per_page=500&page=1"
    request.get(URL)
    # print request.getBSObjet()
    # print len(request.getAllAttrsValue('photo', 'id'))
    photoUrlPrefix = 'http://c5.staticflickr.com/'

    print ctime()
    for e in request.getAllLabel('photo'):
        id = e['id']
        farm = e['farm']
        server = e['server']
        secret = e['secret']
        photoSuffix = str(e['farm'] + '/' + e['server'] + '/' + e['id'] + '_' + e['secret'] + '_h' + '.jpg')
        print type(photoUrlPrefix + photoSuffix)
    print ctime()
