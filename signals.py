# -*- coding: utf-8 -*-
from django.db.models.signals import pre_save
from usetracker.models import UseTracker
from django.utils import timezone

def set_creation_date(sender, **kwargs):
    if not kwargs.get("instance").created_at:
        kwargs.get("instance").created_at = timezone.now()

pre_save.connect(set_creation_date, sender = UseTracker)

def calculate_execution_time(sender, **kwargs):
    if kwargs.get("instance").finished_at and kwargs.get("instance").created_at:
        kwargs.get("instance").execution_time = (kwargs.get("instance").finished_at - kwargs.get("instance").created_at).seconds
pre_save.connect(calculate_execution_time, sender = UseTracker)
