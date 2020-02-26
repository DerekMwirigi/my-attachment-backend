from django.contrib import admin
from .models import (
    Course,
    Student,
    Lecturer,
    LecturerStudentAssignment,
    StudentLogBookItem,
    StudentLogBook,
    StudentAttachmentLocation
)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Lecturer)
admin.site.register(LecturerStudentAssignment)
admin.site.register(StudentLogBookItem)
admin.site.register(StudentLogBook)
admin.site.register(StudentAttachmentLocation)

