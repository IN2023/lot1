from django.db import models


class Brands(models.Model):
    title = models.CharField(max_length=200, blank=False)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"


class Goods(models.Model):
    icon = models.ImageField(upload_to="icons/%Y/%m/%d/", blank=False)
    brand = models.ForeignKey(Brands, on_delete=models.PROTECT)
    title = models.CharField(max_length=200, blank=False)
    number_of_servings = models.IntegerField(blank=False)
    price = models.FloatField(blank=False)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.brand}, {self.title}, {self.number_of_servings}"
