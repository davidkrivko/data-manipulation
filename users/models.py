from django.db import models

from users.choices import GENDER_CHOICE


class CategoryModel(models.Model):
    name = models.CharField(max_length=64)


class UserModel(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField()
    gender = models.CharField(
        choices=GENDER_CHOICE
    )
    birth_date = models.DateTimeField()
