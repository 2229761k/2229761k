from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class PageAdmin (admin.ModelAdmin):
    list_display = ('title','category','url')

# Update the registration to include this customised interface
admin.site.register(Category, CategoryAdmin)

admin.site.register(Page, PageAdmin)

admin.site.register(UserProfile)

# Add in this class to customise the Admin Interface


#class Category(models.Model):
#    name = models.CharField(max_length=128, unique=True)

#    class Meta:
#        verbose_name_plural = 'Categorys'

#    def __str__(self):
#        return self.name



# Register your models here.
