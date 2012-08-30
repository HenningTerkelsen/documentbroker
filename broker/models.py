
import os
import urllib

from client.template_client import TemplateServer
from client.documentbroker_settings import TEMPLATE_URL, TEMPLATE_BASE_URL
from configuration.models import PluginMapping
from util.document_plugin import PluginManager

class DocumentBroker(object):
    """This class is not really a Django model. Rather, it implements a proxy
    which serves as a unified front for all the document-related functionality
    we need to support from the views. Thus, this is the "model" for the
    document broker, template retrieval and similar functionality which we need
    to handle the requests received by the views. 
    
    Whereas the view functions may be protocol dependent, this model class is
    not.
    """

    def __init__(self, user_system_id):
        self._user_system_id = user_system_id

    def generate_document(self, template_id, fields):
        """Return URL to the generated document - throw exception if not
        possible."""
        # Check user system is allowed to use template.
        ts = TemplateServer(TEMPLATE_URL)
        templates = ts.get_templates(self._user_system_id)
        template_dict = { t[1] : t[2] for t in templates } 

        try:
            url = template_dict[template_id]
        except KeyError:
            url = None
            raise RuntimeError(
                    'Template {0} not available for client.'.format(
                        template_id)
                    )
        # Retrieve template from template server.
        real_url = TEMPLATE_BASE_URL + url
        extension = os.path.splitext(url)[1]
        tmp_name = '/tmp/{0}{1}'.format(template_id, extension)
        (fn , headers) = urllib.urlretrieve(real_url, tmp_name)

        # Finally generate document, store in appropriate place and 
        # return URL.

        # Get plugin.
        plugin_mapping = PluginMapping.objects.filter(
                extension=extension.strip('.').upper()
                )[0]
        plugin = PluginManager.get_plugin(plugin_mapping.plugin)

        # TODO: Get fields
        fields = { 'Hello' : 1 }
        # TODO: Get output file name
        output_file = '/tmp/dummy.odt'
        raise RuntimeError("Not implemented: {0}".format(plugin_mapping))
        return ""

