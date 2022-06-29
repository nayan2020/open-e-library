import flask

from library.infrastructure import cookie_auth

blueprint = flask.Blueprint('home', __name__, template_folder='templates')


@blueprint.route('/')
def index():
    return flask.render_template('home/index.html',
                                 user_id=cookie_auth.get_user_id_via_auth_cookie(flask.request),
                                 )


@blueprint.route('/about')
def about():
    return flask.render_template('home/about.html',
                                 user_id=cookie_auth.get_user_id_via_auth_cookie(flask.request),
                                 )
