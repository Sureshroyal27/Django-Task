import threading
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Signal handler to check thread ID
@receiver(post_save, sender=MyModel)
def my_model_post_save(sender, instance, **kwargs):
    current_thread = threading.get_ident()
    print(f"Signal handler thread ID: {current_thread}")
