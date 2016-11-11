# __author__=xk
# -*- coding: utf-8 -*-



if __name__ == '__main__':
    import hashlib



    #frob api_sig=000005fab4534d05api_key9a0554259914a86fb9e7eb014e4e5d52methodflickr.auth.getFrob
    # secret='ca80bdb1db2e4fb0'
    # api_key='bfefc988a3a7c852823d414ae917a785'
    # method='flickr.auth.getFrob'
    # src = secret+'api_key'+api_key+'method'+method
    # m2 = hashlib.md5()
    # m2.update(src)
    # print m2.hexdigest()

    #https://api.flickr.com/services/rest/?&method=flickr.auth.getToken&api_key=&frob=&api_sig=
    magic_cookie='caaad4f0e0f75faf563b8b3639e059badd1e9886f31c075e55ce86e3165b7a27'
    api_key='3d7218133aa1fc6cb757b74f4842ded7'
    secret='81596b5796db85c3'
    frob="72157674815276106-6c425768474f68d4-546261"
    perms="read"
    src = secret+'api_key'+api_key+'frob'+frob+'perms'+perms+'done_auth'+'1'
    m2 = hashlib.md5()
    m2.update(src)
    print m2.hexdigest()


    #getToken api_sig=000005fab4534d05api_key9a0554259914a86fb9e7eb014e4e5d52frob934-746563215463214621methodflickr.auth.getToken
    # method="flickr.auth.getToken"
    # src = secret+'api_key'+api_key+'frob'+frob+'method'+method
    # m2 = hashlib.md5()
    # m2.update(src)

    # print m2.hexdigest()


