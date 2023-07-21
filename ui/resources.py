from import_export import resources
from .models import CodeModels

class CodeResource(resources.ModelResource):
    class Meta:
        model = CodeModels
