#!/usr/bin/env python
import os
import sys
from blog.models import Advertiser
advertisers = Advertiser.objects.all()
for advertiser in advertisers:
    print(advertiser.name)
from myapp.models import Advertisement
advertisements = Advertisement.objects.all()
for advertisement in advertisements:
    print(advertisement.title)

