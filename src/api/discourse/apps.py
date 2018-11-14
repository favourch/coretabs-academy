from django.apps import AppConfig


class DiscourseConfig(AppConfig):
    name = 'discourse'

    def ready(self):
        import discourse.signals
