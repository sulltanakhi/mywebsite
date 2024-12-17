from django.contrib import admin

from course.models import Course

from course.models import Subject
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']

admin.site.register(Course, CourseAdmin)

admin.site.register(Subject)