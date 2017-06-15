from django.contrib import admin
from .models import (Domain, Situation, Semestre, Cours)

# Register your models here.
admin.site.register(Domain)
admin.site.register(Situation)
admin.site.register(Semestre)
admin.site.register(Cours)