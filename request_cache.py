from requests import request
from libs import cache_for
from requests_toolbelt import MultipartEncoder


class RestApi(object):
    def __init__(self, cache):
        self.cache_for = cache

    @cache_for(lambda x: x.cache_for)
    def get(self, url, params=None, **kwargs):
        kwargs.setdefault('allow_redirects', True)
        return request('get', url, params=params, **kwargs)

    @cache_for(lambda x: x.cache_for)
    def post(self, url, data=None, json=None, **kwargs):
        # print(self.cache_for)
        return request('post', url, data=data, json=json, **kwargs)

    @cache_for(lambda x: x.cache_for)
    def put(self, url, data=None, **kwargs):
        return request('put', url, data=data, **kwargs)

    @cache_for(lambda x: x.cache_for)
    def post_form(self, url, data=None, json=None, **kwargs):
        search_data = MultipartEncoder(
            fields=data
        )
        return request('post', url, data=search_data.to_string(), headers={'Content-Type': search_data.content_type},
                       json=json, **kwargs,
                       )
