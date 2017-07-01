from django.core.cache import cache


def cache_get_key(*args, **kwargs):
    import hashlib
    serialise = []
    for arg in args:
        serialise.append(str(arg))
    for key, arg in kwargs.items():
        serialise.append(str(key))
        serialise.append(str(arg))
    key = hashlib.md5("".join(serialise).encode('utf-8')).hexdigest()
    return key


# decorator for caching functions
def cache_for(_lambda):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            key = cache_get_key(fn.__name__, *args, **kwargs)

            result = cache.get(str(key))
            if not result:
                result = fn(*args, **kwargs)
                cache.set(key, result, args[0].cache_for)
            return result

        return wrapper

    return decorator
