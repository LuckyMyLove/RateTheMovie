from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.


class Categories(models.Model):
    name = models.TextField()


class Movies(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    title = models.TextField()
    description = models.TextField()
    premier_date = models.TextField()
    # If Category get deleted, it will delete Movie also (just to give you an example)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
