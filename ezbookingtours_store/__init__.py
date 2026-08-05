import datetime

import django.utils.timezone

if not hasattr(django.utils.timezone, "utc"):
    django.utils.timezone.utc = datetime.timezone.utc
