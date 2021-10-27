from django.contrib import admin
from .models import carossel, content, home_page, message, service, subscriber, formation

# Register your models here.
admin.site.register(carossel)
admin.site.register(content)
admin.site.register(home_page)
admin.site.register(service)
admin.site.register(message)
admin.site.register(subscriber)
admin.site.register(formation)