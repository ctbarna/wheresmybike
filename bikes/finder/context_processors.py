from django.conf import settings
def api_keys(context):
    api_keys = {}

    for key, value in settings.API_KEYS.iteritems():
        api_keys["%s_API_KEY" % key.upper()] = value
    return api_keys
