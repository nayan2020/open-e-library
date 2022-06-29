import flask


class RequestDictionary(dict):
    def __getattr__(self, key):
        return self.get(key)


def create(**route_args) -> RequestDictionary:
    request = flask.request
    data = {
        **request.args,  # The key/value pairs in the URL query string
        **request.headers,  # Header values
        **request.form,  # The key/values pairs in the body, form a HTML post form
        **route_args,  # And additional arguments the method access, if they want them merge
    }

    return RequestDictionary(data)
