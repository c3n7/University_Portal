from django.contrib import admin
from .models import SemesterEnrollment

class SemesterEnrollmentAdmin(admin.ModelAdmin):
    model = SemesterEnrollment
    list_display = ['student', 'enrolled_course', 'year', 'semester']

admin.site.register(SemesterEnrollment, SemesterEnrollmentAdmin)
