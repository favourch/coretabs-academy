from django.dispatch import Signal


user_updated = Signal(providing_args=["user"])
