from django.contrib import admin

from main.models import BaseProcess, ProcessA, ProcessB

admin.site.register(BaseProcess)
admin.site.register(ProcessA)
admin.site.register(ProcessB)
