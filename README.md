# django-request-cache

How to use :

```python

from request_cache import RestApi
url = "example.com"
data = {
    "var1" :1
}
# cache for 500 seconds
API = RestApi(cache=500)
response = API.post(url=url,data=data)

```
Test on :
* Django 1.10
* python 3.6