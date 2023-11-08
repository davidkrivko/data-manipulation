from django.db import models

from users.choices import GENDER_CHOICE


class CategoryModel(models.Model):
    name = models.CharField(max_length=64)


class UserModel(models.Model):
    email = models.EmailField()

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICE,
    )
    birth_date = models.DateField()

    category = models.ForeignKey(
        "CategoryModel",
        on_delete=models.SET_NULL,
        null=True,
    )
