from django.contrib import admin
from .models import department, employee, truck_type, truck, delivery_note, truck_list_report, truck_header_report, master_package, dn_list_report, dn_header_report

admin.site.register(department)
admin.site.register(employee)
admin.site.register(truck_type)
admin.site.register(truck)
admin.site.register(delivery_note)
admin.site.register(truck_list_report)
admin.site.register(truck_header_report)
admin.site.register(master_package)
admin.site.register(dn_list_report)
admin.site.register(dn_header_report)