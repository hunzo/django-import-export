from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import CodeModels
from .resources import CodeResource

class CodeAdmin(ImportExportModelAdmin):
    resource_class = CodeResource
    list_display = ["name", "code"]
# Register your models here.

admin.site.register(CodeModels, CodeAdmin)
