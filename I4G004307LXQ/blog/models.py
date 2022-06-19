# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=1000000)
    author = models.ForeignKey(User)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    published_date = models.DateTimeField(default=datetime.now, blank=True)
