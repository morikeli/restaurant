from accounts.models import User
from django.db import models
from PIL import Image


class Food(models.Model):
    id = models.CharField(max_length=15, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=False)
    price = models.PositiveIntegerField(default=0, editable=False)
    type = models.CharField(max_length=30, blank=False)
    image = models.ImageField(upload_to='Food-Imgs/', blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Foods'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super(Food, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 500 and img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Tables(models.Model):
    id = models.CharField(max_length=15, primary_key=True, unique=True, editable=False)
    booked = models.BooleanField(default=False, editable=False)
    name = models.CharField(max_length=50, blank=False)
    seats = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Tables'

    def __str__(self):
        return self.name
    

class FoodOrders(models.Model):
    id  = models.CharField(max_length=20, primary_key=True, unique=True, editable=False)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    food = models.ForeignKey(Food, on_delete=models.DO_NOTHING, editable=False)
    order = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0, editable=False)
    cost = models.PositiveIntegerField(default=0, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        verbose_name_plural = 'Customer Food Orders'

    def __str__(self):
        return self.name


class BookTable(models.Model):
    id  = models.CharField(max_length=20, primary_key=True, unique=True, editable=False)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    table_no = models.ForeignKey(Tables, on_delete=models.DO_NOTHING, editable=False)
    people = models.PositiveIntegerField(default=0)
    cost = models.PositiveIntegerField(default=0, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        verbose_name_plural = 'Booked Tables'

    def __str__(self):
        return self.name
    
