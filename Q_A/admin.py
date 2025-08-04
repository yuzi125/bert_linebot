from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from Q_A.models import QA
# Register your models here.



#admin.site.register(QA) 未顯示類別

@admin.register(QA)

class QA_import_export(ImportExportModelAdmin):
    list_display=('id','question','answer')
    pass

