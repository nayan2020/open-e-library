from time import sleep

import flask

import library.services.user_service as user_service
import library.infrastructure.cookie_auth as cookie_auth

blueprint = flask.Blueprint('account', __name__, template_folder='templates')


# ########################## INDEX ###################

@blueprint.route('/account')
def index():  # put application's code here
    user_id = cookie_auth.get_user_id_via_auth_cookie(flask.request)
    if user_id is None:
        return flask.redirect('/account/login')

    user = user_service.find_user_by_id(user_id)
    if not user:
        return flask.redirect('/account/login')

    data = {'user': user, 'user_id': cookie_auth.get_user_id_via_auth_cookie(flask.request), }
    return flask.render_template('account/index.html')


# ########################## REGISTER ###################

@blueprint.route('/account/register', methods=['GET'])
def register_get():  # put application's code here
    data = {'user_id': cookie_auth.get_user_id_via_auth_cookie(flask.request), }
    return flask.render_template('account/register.html')


@blueprint.route('/account/register', methods=['POST'])
def register_post():  # put application's code here
    flask.render_template('account/register.html')
    r = flask.request

    name = r.form.get('name')
    email = r.form.get('email', '').lower().strip()
    password = r.form.get('password', '').strip()

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
    r = flask.request

    email = r.form.get('email', '').lower().strip()
    password = r.form.get('password', '').strip()

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

