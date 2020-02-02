from django.contrib import admin

# Register your models here.
from .models import Artical, Category, Label
 
admin.site.register(Artical)
admin.site.register(Category)
admin.site.register(Label)