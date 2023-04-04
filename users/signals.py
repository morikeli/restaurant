from .models import Food, Tables, FoodOrders, BookTable
from django.db.models.signals import pre_save
from django.dispatch import receiver
import uuid


@receiver(pre_save, sender=Food)
def generate_foodID(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace('-', '')[:15]

@receiver(pre_save, sender=Tables)
def generate_ID(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace('-', '')[:15]

@receiver(pre_save, sender=FoodOrders)
def generate_ID(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace('-', '')[:20]

@receiver(pre_save, sender=BookTable)
def generate_ID(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace('-', '')[:20]

