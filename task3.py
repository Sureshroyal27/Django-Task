from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Signal handler to check if the data is visible inside the signal
@receiver(post_save, sender=MyModel)
def my_model_post_save(sender, instance, **kwargs):
    # Try to read the MyModel instance inside the signal handler
    if MyModel.objects.filter(id=instance.id).exists():
        print("Signal handler can see the saved object")
    else:
        print("Signal handler cannot see the saved object")
