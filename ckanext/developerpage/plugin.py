import ckan.plugins as p
import ckan.lib.helpers as ckanhelpers
from ckan.logic import get_action
import ckan.plugins.toolkit as toolkit

from ckanext.developerpage import blueprint
from ckanext.developerpage.helpers import get_host_info, get_ckan_info, get_extensions_info


def counter_helper():
    stats = ckanhelpers.get_site_statistics()
    stats['dataset_count'] = get_action('package_search')(
        {}, {"rows": 0, "include_private": True})['count']
    return stats


class DeveloperpagePlugin(p.SingletonPlugin):
    p.implements(p.IConfigurer)
    p.implements(p.IBlueprint)
    p.implements(p.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'developerpage')

    def get_helpers(self):
        return {
            'get_host_info': get_host_info,
            'get_ckan_info': get_ckan_info,
            'counter_helper': counter_helper,
            'get_extensions_info': get_extensions_info,
        }

    def get_blueprint(self):
        return blueprint.developerpage
