from django.db import models

# Create your models here.


class Advisor(models.Model):
    photo = models.URLField(max_length=1000)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
