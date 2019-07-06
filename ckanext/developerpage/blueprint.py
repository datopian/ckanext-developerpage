import sys
from flask import Blueprint, abort
from flask.views import MethodView 

import ckan.plugins.toolkit as toolkit

import ckan.model as model
import ckan.logic as logic
import ckan.lib.base as base
import ckan.lib.helpers as h

from ckan.common import g, config, _

import ckanext.developerpage.helpers as dp_helpers

developerpage = Blueprint(u'developerpage', __name__)


@developerpage.before_request
def before_request():
    u'''set context and check authorization'''
    try:
        context = {
            u'model': model,
            u'user': g.user,
            u'auth_user_obj': g.userobj}
        logic.check_access(u'dashboard_activity_list', context)
    except logic.NotAuthorized:
        abort(403)

def show():
    return base.render(u'developerpage/developerpage.html')


developerpage_urls = [
    (u'/developer', show)
]

for rule, view_func in developerpage_urls:
    developerpage.add_url_rule(rule, view_func=view_func)
