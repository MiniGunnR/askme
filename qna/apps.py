from __future__ import unicode_literals

from django.apps import AppConfig


class QnaConfig(AppConfig):
    name = 'qna'
    verbose_name = 'Q&A'

    def ready(self):
        import qna.signals.handler