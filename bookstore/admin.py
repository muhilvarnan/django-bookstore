from django.contrib import admin

# Register your models here.
from .models import Books,Authors,Orders,Customers,Publishers

admin.site.register(Books)
admin.site.register(Authors)
admin.site.register(Orders)
admin.site.register(Customers)
admin.site.register(Publishers)
