from os.path import abspath
from urllib.parse import urljoin
from urllib.request import pathname2url
import ssl
from suds.client import Client
import os

os.chdir("C:\DATA\TRAINING\PYTHON")

WSDL = urljoin('file:', pathname2url(abspath('schema\AXLAPI.wsdl')))

# Allow insecure connections
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

CLIENT = Client(WSDL, location='https://%s:8443/axl/' % ('10.122.44.121'),
                username='admin', password='c1sco123')

try:
    response = CLIENT.service.listUser(
        searchCriteria={
            'userid': '%'
        },
        returnedTags={
            'userid': True,
            'telephoneNumber': True
        })
    print(response['return']['user'])

except Exception:
    print('CUCM AXL login failed, incorrect host or username/password ?')
