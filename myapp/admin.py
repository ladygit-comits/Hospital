from django.contrib import admin
from myapp.models import users
from myapp.models import Product
from myapp.models import Appointment
from myapp.models import Contact
from myapp.models import Member
# Register your models here.

admin.site.register(users)
admin.site.register(Product)
admin.site.register(Appointment)
admin.site.register(Contact)
admin.site.register(Member)

