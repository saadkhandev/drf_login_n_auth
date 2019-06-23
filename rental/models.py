from django.db import models
from django.contrib.auth.models import User


class Friend(models.Model):
    name = models.CharField(max_length=100)


class OwnedModel(models.Model):
    owner = models.ForeignKey(User,
    on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Belonging(OwnedModel):
    name = models.CharField(max_length=100)


class Borrowed(models.Model):
    what = models.ForeignKey(Belonging, on_delete=models.CASCADE)
    to_who = models.ForeignKey(Friend, on_delete=models.CASCADE)
    when = models.DateTimeField(auto_now_add=True)
    returned = models.DateTimeField(null=True, blank=True)
