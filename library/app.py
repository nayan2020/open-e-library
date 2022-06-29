import flask

from nosql import mongo_setup
from nosql.users import User

app = flask.Flask(__name__)


def main():
    configure()
    app.run(debug=True, port=5006)


def configure():
    print("Configuring Flask app")

    register_blueprints()
    print("Registered blueprints")

    setup_db()
    print("DB setup completed")


def setup_db():
    mongo_setup.global_init()

def register_blueprints():
    from views import account_views
    from views import home_views

    app.register_blueprint(account_views.blueprint)
    app.register_blueprint(home_views.blueprint)


if __name__ == '__main__':
    main()
