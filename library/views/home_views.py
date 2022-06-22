

from flask import Blueprint
import flask


blueprint = flask.Blueprint('home', __name__, template_folder='templates') 


@blueprint.route('/')
def index():
	return flask.render_template('home/index.html')

@blueprint.route('/about')
def about():
	return flask.render_template('home/about.html')