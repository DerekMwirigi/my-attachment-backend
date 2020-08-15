from django.contrib import admin
from .models import (
    Course,
    LecturerStudentAssignment,
    StudentLogBookItem,
    StudentLogBook,
    StudentAttachmentLocation
)
admin.site.register(Course)
admin.site.register(LecturerStudentAssignment)
admin.site.register(StudentLogBookItem)
admin.site.register(StudentLogBook)
admin.site.register(StudentAttachmentLocation)

