from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Promotion(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    url = models.URLField(null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    user = models.ForeignKey(UserModel, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.title
