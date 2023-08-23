from django.contrib import admin
from myfiles.models import *
# Register your models here.


class AdminService(admin.ModelAdmin):
    list_display = ['id','nomi','rasm','text','date']

admin.site.register(Service,AdminService)


class AdminWorker(admin.ModelAdmin):
    list_display = ['id','ism','lavozim','rasm','text','date']

admin.site.register(Worker,AdminWorker)


class AdminProject(admin.ModelAdmin):
    list_display = ['id','nomi','manzil','rasm','text','date']

admin.site.register(Project,AdminProject)


class AdminBlog(admin.ModelAdmin):
    list_display = ['id','nomi','rasm','text','date']

admin.site.register(Blog,AdminBlog)

class AdminContact(admin.ModelAdmin):
    list_display = ['id','nomi','rasm','text','date']

admin.site.register(Contact,AdminContact)


class AdminMessage(admin.ModelAdmin):
    list_display = ['id','name','email','text','date']

admin.site.register(Messages,AdminMessage)