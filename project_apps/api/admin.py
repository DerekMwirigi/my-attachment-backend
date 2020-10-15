from django.contrib import admin
from .models import (
    User,
    Course,
    LecturerStudentAssignment,
    StudentLogBookItem,
    StudentLogBook,
    StudentAttachmentLocation
)
class UserAdmin(admin.ModelAdmin):
    list_display= ('first_name', 'last_name', 'phone', 'email', 'user_role')

admin.site.register(User, UserAdmin)
admin.site.register(Course)
admin.site.register(LecturerStudentAssignment)
admin.site.register(StudentLogBookItem)
admin.site.register(StudentLogBook)
admin.site.register(StudentAttachmentLocation)

