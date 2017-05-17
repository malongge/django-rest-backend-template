from django.apps import AppConfig


class ArticlesAppConfig(AppConfig):
    name = 'conf.apps.articles'
    label = 'articles'
    verbose_name = 'Articles'

    def ready(self):
        import conf.apps.articles.signals

default_app_config = 'conf.apps.articles.ArticlesAppConfig'
