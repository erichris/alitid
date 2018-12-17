from django.contrib import admin

from .models import PlanEscape, PlanEscapeAdmin

admin.site.register(PlanEscape, PlanEscapeAdmin)