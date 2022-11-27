from django.contrib import admin
from .models import MyCovidModel,MyApplyModel
# Register your models here.
admin.site.register(MyCovidModel)
admin.site.register(MyApplyModel)