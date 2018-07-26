from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'


class Comment(models.Model):
    name = models.CharField(max_length=30)
    comment = models.CharField(max_length=1000)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('comment')


class Register(models.Model):
    First_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=40)
    email = models.EmailField()
    city = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.First_name

