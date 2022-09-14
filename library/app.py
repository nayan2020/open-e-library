import os.path
import flask
import library.data.db_session as db_session

app = flask.Flask(__name__)


def main():
    register_blueprints()
    setup_db()
    app.run(debug=True)


def setup_db():
    db_file = os.path.join(
        os.path.dirname(__file__),
        'db',
        'library.sqlite'
    )
    db_session.global_init(db_file)


def register_blueprints():
    from views import cms_views
    from views import home_views
    from views import package_views
    from views import account_views

    app.register_blueprint(home_views.blueprint)
    app.register_blueprint(cms_views.blueprint)
    app.register_blueprint(package_views.blueprint)
    app.register_blueprint(account_views.blueprint)


if __name__ == '__main__':
    main()
