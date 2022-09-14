from time import sleep

import flask

from library.infrastructure.views_modifiers import response
import library.services.user_service as user_service
import library.infrastructure.cookie_auth as cookie_auth
import library.infrastructure.request_dict as request_dict

from library.viewmodels.account.index_viewmodel import IndexViewModel
from library.viewmodels.account.register_viewmodel import RegisterViewModel

blueprint = flask.Blueprint('account', __name__, template_folder='templates')


# ########################## INDEX ###################

@blueprint.route('/account')
@response(template_file='account/index.html')
def index():  # put application's code here
    user_id = cookie_auth.get_user_id_via_auth_cookie(flask.request)
    if user_id is None:
        return flask.redirect('/account/login')

    user = user_service.find_user_by_id(user_id)
    if not user:
        return flask.redirect('/account/login')

    return {
        'user': user,
        'user_id': cookie_auth.get_user_id_via_auth_cookie(flask.request),
    }


# ########################## REGISTER ###################

@blueprint.route('/account/register', methods=['GET'])
@response(template_file='account/register.html')
def register_get():  # put application's code here
    return { 'user_id': cookie_auth.get_user_id_via_auth_cookie(flask.request), }


@blueprint.route('/account/register', methods=['POST'])
# @response(template_file='account/register.html')
def register_post():  # put application's code here
    flask.render_template('account/register.html')

    data = request_dict.create()

    name = data.name
    email = data.email.lower().strip()
    password = data.password.strip()

    print(name, email, password)
    if not name or not email or not password:
        return flask.render_template('account/register.html',
                                     name=name,
                                     email=email,
                                     error="Some required fields are Missing",
                                     user_id=cookie_auth.get_user_id_via_auth_cookie(flask.request),
                                     )
    # TODO: Create the user

    user = user_service.create_user(name, email, password)

    if not user:
        return flask.render_template('account/register.html',
                                     name=name,
                                     email=email,
                                     error="A User  with that mail already exits",
                                     user_id=cookie_auth.get_user_id_via_auth_cookie(flask.request),
                                     )

    # TODO: Log in browser as a session
    sleep(.005)
    resp = flask.redirect('/account')
    cookie_auth.set_auth(resp, user.id)
    return resp


# ########################## LOGIN ###################


@blueprint.route('/account/login', methods=['GET'])
def login_get():  # put application's code here
    return flask.render_template('account/login.html')


@blueprint.route('/account/login', methods=['POST'])
def login_post():  # put application's code here
    flask.render_template('account/login.html')
    data = request_dict.create()

    email = data.email.strip()
    password = data.password.strip()
    print(email, password)
    if not email or not password:
        return flask.render_template('account/login.html',
                                     email=email,
                                     error="Some required fields are Missing", )
    # TODO: Validate the user
    user = user_service.login_user(email, password)
    if not user:
        return flask.render_template('account/login.html',
                                     email=email,
                                     error="The account does not exit or password is  wrong.", )

    # TODO: Log in browser as a session
    resp = flask.redirect('/account')
    cookie_auth.set_auth(resp, user.id)

    return resp


# ########################## LOGOUT ###################

@blueprint.route('/account/logout')
def logout():  # put application's code here'
    resp = flask.redirect('/')
    cookie_auth.logout(resp)

    return resp

# def ok():
#     user =flask.request.cookies.get()
#
#