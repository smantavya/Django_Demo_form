from django.contrib import admin
from form.models import MyUser

# Register your models here.
class MyUserAdmin(admin.ModelAdmin):
    list_display = ['Full_name','State','City','Membership','Career']
admin.site.register(MyUser,MyUserAdmin)
