from django.contrib import admin

from .models import Service, Subscription

# Register your models here.

# admin.site.register(Comment)
admin.site.register(Subscription)





class ServiceModelAdmin(admin.ModelAdmin):

    list_display = ['__str__', 'service_name', 'featured', 'bucksamonth','emoji']

    class Meta:
        model = Service


admin.site.register(Service, ServiceModelAdmin)

    #
    #
	# service_name 			= models.CharField(max_length=140)
	# service_slug			= models.SlugField(blank=True)
	# url_name 				= models.CharField(max_length=200)
	# description_long		= models.CharField(max_length=500, default='')
	# description_short		= models.CharField(max_length=140, default='')
	# category				= models.ManyToManyField(Category, blank=True)
	# featured				= models.BooleanField(default=False)
	# date_created 			= models.DateField(auto_now=True)
	# bucksamonth 			= models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
	# emoji					= models.CharField(max_length=20, default='')
	# twitter 				= models.CharField(max_length=100, default='')
	# tags 					= TaggableManager()
