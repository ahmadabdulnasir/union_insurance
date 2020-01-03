#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__author__ = 'Ahmad Abdulnasir Shu'aib <me@ahmadabdulnasir.com.ng>'
__homepage__ = https://ahmadabdulnasir.com.ng
__copyright__ = 'Copyright (c) 2019, salafi'
__version__ = "0.01t"
"""
from django.utils import timezone
from uuid import uuid4
# from core.models import SiteInformation

class Egg:
    title = "Page Not Created"
    slug = "Page Not Created"
    sub_title = "Sorry This Page is Not Created Yet !!"
    body = sub_title
    img = None
    pub_date = timezone.now()
    extra_info = None

    def __str__(self):
        return self.title

def getUniqueId():
    tmp = uuid4()
    tmp_ = str(tmp).split('-')[0]
    return tmp_

def LongUniqueId():
    tmp = uuid4()
    return tmp

def siteLoginUrl():
    return 'accounts/login/'