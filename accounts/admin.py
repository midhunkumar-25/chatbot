from django.contrib import admin
from .models import Student,Staff,CollegeFee,Placements,HostelFee
# Register your models here.
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(CollegeFee)
admin.site.register(Placements)
admin.site.register(HostelFee)