from django.contrib import admin
from rango.models import Category, Page

admin.site.register(Category)
admin.site.register(Page)

#class Category(models.Model):
#    name = models.CharField(max_length=128, unique=True)

#    class Meta:
#        verbose_name_plural = 'Categorys'

#    def __str__(self):
#        return self.name



# Register your models here.
