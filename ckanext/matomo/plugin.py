import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckanext.matomo import helpers



class MatomoPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')


    # ITemplateHelpers
    def get_helpers(self):
        return {
                'matomo_get_site_id': helpers.get_matomo_id,
                'matomo_get_domain': helpers.get_matomo_domain,
                'matomo_get_custom_url': helpers.get_matomo_custom_url
                }
