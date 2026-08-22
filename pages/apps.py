from django.apps import AppConfig
from suit.apps import DjangoSuitConfig

class PagesConfig(AppConfig):
    name = 'pages'

class SuitConfig(DjangoSuitConfig):

    layout = 'horizontal'  # horizontal navigation