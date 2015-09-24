# -*- coding: utf-8 -*-
from django.db import models

class UseTrackerManager(models.Manager):
    def filtered_search(self, filter_dict):
        """
        Filter search by filter_dict valid params
        """
        qset = self.filter()
        valid_filters = {"fromdate": 'created_at__gte', 
                         "todate": 'created_at__lte', 
                         "protocol": 'protocol__icontains', 
                         "host": 'host__icontains', 
                         "path": 'path__icontains', 
                         "getparams": 'get_params__icontains',
                         "headers": 'headers__icontains', 
                         "postpayload": 'post_payload__icontains', 
                         "user": 'username__icontains', 
                         "exceptiontext": 'exception__icontains', 
                         "minexecutiontime": 'execution_time__gte', 
                         "maxexecutiontime": 'execution_time__lte'}
        filters = {}
        try:
            for vf in valid_filters.keys():
                if vf in filter_dict.keys() and filter_dict[vf] != "":
                    filters[valid_filters[vf]] = filter_dict[vf]
            qset = qset.filter(**filters)
        except:
            qset = self.none()
        return qset
