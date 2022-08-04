
from django.contrib import admin
from django.db import models
from .models import Topic, Course, Student, Order

# Register your models here.

#final project part 1
class CourseInline(admin.TabularInline):
    model = Course

class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    inlines = [
        CourseInline,
    ]
admin.site.register(Topic, TopicAdmin)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Order)
