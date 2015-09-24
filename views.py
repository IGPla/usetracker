# -*- coding: utf-8 -*-
from django.shortcuts import render
from usetracker import models
from django.http import JsonResponse
from collections import Counter
from django.contrib.auth.decorators import permission_required

@permission_required("usetracker.use_tracker_admin")
def show_progress(request):
    """
    Show tracking progress
    """
    return render(request,
                  "usetracker/show_progress.html",
                  {
                  }
    )

@permission_required("usetracker.use_tracker_admin")
def get_available_hosts(request):
    """
    Return available hosts
    """
    hosts = {'hosts': [""] + [ut for ut in models.UseTracker.objects.order_by("host").values_list("host", flat=True).distinct() if ut]}
    return JsonResponse(hosts)

@permission_required("usetracker.use_tracker_admin")
def get_available_protocols(request):
    """
    Return available protocols
    """
    protocols = {'protocols': [""] + [ut for ut in models.UseTracker.objects.order_by("protocol").values_list("protocol", flat=True).distinct() if ut]}
    return JsonResponse(protocols)

@permission_required("usetracker.use_tracker_admin")
def get_available_users(request):
    """
    Return available users
    """
    users = {'users': [""] + [ut for ut in models.UseTracker.objects.order_by("username").values_list("username", flat=True).distinct() if ut]}
    return JsonResponse(users)

@permission_required("usetracker.use_tracker_admin")
def get_available_fields(request):
    """
    Return usetracker fields
    """
    fields = {'fields': [unicode(field.verbose_name) for field in models.UseTracker._meta.fields]}
    return JsonResponse(fields)

@permission_required("usetracker.use_tracker_admin")
def get_filtered_data(request):
    """
    Return filtered data
    """
    qset = models.UseTracker.objects.filtered_search(request.GET)
    rdata = {
        'rawdata': [],
        'data': [[]],
        'labels': [],
        'series': [request.GET.get("charttype")]
    }
    grouper = request.GET.get("groupby")
    if request.GET.get("charttype") in ("Requests started at", "Requests end at"):
        if request.GET.get("charttype") == "Requests started at":
            qset = qset.order_by("created_at")
            values = qset.values_list("created_at", flat = True)
        elif request.GET.get("charttype") == "Requests end at":
            qset = qset.order_by("finished_at")
            values = qset.values_list("finished_at", flat = True)
        prev = None
        for val in values:
            grouped = getattr(val, grouper)
            if grouped != prev:
                prev = grouped
                rdata['labels'].append(val.strftime("%Y-%m-%d %H:%M:%S"))
                rdata['data'][0].append(0)
            rdata['data'][0][-1] += 1
                
    elif request.GET.get("charttype") == "Execution time":
        qset = qset.order_by("execution_time")
        values = qset.values_list("execution_time", flat = True)
        
        for key, val in Counter(values).items():
            rdata['labels'].append(key)
            rdata['data'][0].append(val)

    rdata['rawdata'] = list(qset.values_list())

    if not len(rdata['labels']):
        rdata['labels'].append("")
        rdata['data'][0].append(0)

    return JsonResponse(rdata)
