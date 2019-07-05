import ckan.plugins as p

import ckan.plugins.toolkit as toolkit

from ckanext.developerpage import blueprint
from ckanext.developerpage.helpers import get_host_info, get_ckan_info



class DeveloperpagePlugin(p.SingletonPlugin):
    p.implements(p.IConfigurer)
    p.implements(p.IActions)
    p.implements(p.IAuthFunctions)
    p.implements(p.IBlueprint)
    p.implements(p.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'developerpage')


    def get_helpers(self):
        return {
            'get_host_info' : get_host_info,
            'get_ckan_info' : get_ckan_info, }

    def get_actions(self):
        return {}

    def get_blueprint(self):
        return blueprint.developerpage
