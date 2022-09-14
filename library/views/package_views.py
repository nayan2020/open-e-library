import flask
from library.infrastructure.views_modifiers import response
from library.services import package_service

blueprint = flask.Blueprint('packages', __name__, template_folder='templates')


@blueprint.route('/project/<package_name>')
@response(template_file='/packages/details.html')
def package_details(package_name: str):  # put application's code here
    if not package_name:
        return flask.abort(status=404)

    package = package_service.get_package_by_id(package_name.strip().lower())
    if not package:
        return flask.abort(status=404)
    #
    latest_version = "0.0.0"

    # latest_release = None
    # is_latest = True
    #
    # if package.releases:
    #     latest_release = package.releases[0]
    #     latest_version = latest_release.version_text
    #
    # return {
    #     'package': package,
    #     'latest_version': latest_version,
    #     'latest_release': latest_release,
    #     'release_version': latest_release,
    #     'is_latest': True
    # }

    return {
        'package': package,
        'latest_version': latest_version

    }


@blueprint.route('/<int:rank>')
# @response(template_file='/home/details.html')
def popular(rank: int):  # put application's code here
    return f'Package details for {rank}th most popular package'


