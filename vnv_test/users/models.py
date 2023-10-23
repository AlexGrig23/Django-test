from django.db import models
from django.urls import reverse


class Group(models.Model):

    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=120)

    def get_absolute_url(self):
        return reverse('groups_list')

    def __str__(self):
        return self.title


class User(models.Model):

    user_name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(Group, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('users_list')

    def __str__(self):
        return self.user_name


