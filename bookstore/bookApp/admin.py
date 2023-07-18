from django.contrib import admin

from .models import Contact,Book,Category,Author,Subscriber
# Register your models here.

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Contact)
admin.site.register(Subscriber)
