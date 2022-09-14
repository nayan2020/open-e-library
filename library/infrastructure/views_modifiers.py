from functools import wraps
import flask


def response(*, mimetype: str = None, template_file: str = None):  # put application's code here
    def response_inner(f):  # put application's code here'

        # print("Wrapping in response {}".format(f.__name__), flush=True)

        @wraps(f)
        def view_method(*args, **kwargs):  # put application's code here'
            response_val = f(*args, **kwargs)
            if isinstance(response_val, flask.Response):  # put application's code here'
                return response_val

            if isinstance(response_val, dict):  # put application's code here'
                model = dict(response_val)
            else:
                model = dict()

            if template_file and not isinstance(response_val, dict):  # put application's code here
                raise Exception("Invalid return type {},we....")

            if template_file:
                response_val = flask.render_template(template_file, **response_val)

            resp = flask.make_response(response_val)
            resp.model = model
            if mimetype:
                resp.mimetype = mimetype

            return resp

        return view_method

    return response_inner
