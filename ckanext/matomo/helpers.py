from urllib.parse import urlparse
from ckan.plugins import toolkit


def get_matomo_id():
    """
    Return the config option "ckanext.matomo.site_id" that will be a unique Matomo id.
    """
    matomo_id = toolkit.config.get('ckanext.matomo.site_id', None)
    return matomo_id


def get_matomo_domain():
    """
    Return the config option "ckanext.matomo.domain" which will contain the base matomo URL to be used.
    """
    matomo_url = toolkit.config.get('ckanext.matomo.domain', None)
    if matomo_url and not matomo_url.endswith("/"):
        matomo_url += "/"
    return matomo_url


def get_matomo_custom_url():
    """
    Returns a custom url which should be used when tracking searching in Matomo. Based on the documentation in:
    - https://matomo.org/faq/reports/tracking-site-search-keywords/
    """
    custom_url = None
    page = getattr(toolkit.g, "page", None)
    q = getattr(toolkit.g, "q", None)

    if q and page is not None:
        # need to remove all existing query parameters from the request url, as those will be added by add_url_param
        # not the prettiest code, but at least without any new imports
        custom_url = toolkit.h.add_url_param(
            alternative_url=urlparse(toolkit.request.url)._replace(query=None).geturl(),
            new_params={"search_count": page.item_count}
        )

    return custom_url