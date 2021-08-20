from django.contrib import admin

# Register your models here.
from .models import User, Movie, Review, Comment

admin.site.register(User)
admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Comment)