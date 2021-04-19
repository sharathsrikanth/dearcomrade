from django.contrib import admin
from .models import ResultantTempUserTable


class ResultantTempUserTableAdmin(admin.ModelAdmin):
    list_display = ('userid', 'name', 'age', 'avgrating', 'compatibilityscore', 'profilepicurl')


admin.site.register(ResultantTempUserTable,ResultantTempUserTableAdmin)

