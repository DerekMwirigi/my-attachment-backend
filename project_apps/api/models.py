from django.db import models
from django.urls import reverse
import uuid
from django.utils import timezone

from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
from django.utils import timezone

SuperAdmin = 0
Lecturer = 1
Student = 2

USER_ROLE_CHOICES = (
    (SuperAdmin, 'SuperAdmin'),
    (Lecturer, 'Lecturer'),
    (Student, 'Student')
)

ACTIVE = 1
INACTIVE = 0

USER_STATUS_CHOICES = (
    (ACTIVE,'Active'),
    (INACTIVE, 'In Active'),
)
class User(AbstractUser):
    """
    A base user for auth and extending
    """
    code = models.UUIDField(default=uuid.uuid4)
    phone = models.CharField(max_length=12, default='')
    user_role = models.PositiveSmallIntegerField(choices=USER_ROLE_CHOICES, default=Student)
    status = models.PositiveSmallIntegerField(default=ACTIVE, choices=USER_STATUS_CHOICES)


    def __str__(self):
        return self.username

    @property
    def full_names(self):
        return "{} {}".format(self.first_name.capitalize(),self.last_name.capitalize())

    @property
    def get_phone(self):
        return self.phone
    
    @property
    def get_email(self):
        return self.email

class Course(models.Model):
    STATUS_CHOICES = (
        ('0','In active'),
        ('1', 'Active')
    )
    name = models.CharField(max_length=50)
    code = models.UUIDField(default=uuid.uuid4)
    created_on = models.DateTimeField(default=timezone.now)
    status = models.CharField(default=0, max_length=200, choices=STATUS_CHOICES)

    class Meta:
        db_table = "courses"
        verbose_name_plural = "courses"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
	    return reverse('course-details', kwargs={'pk': self.pk})

class LecturerStudentAssignment(models.Model):
    STATUS_CHOICES = (
        ('0','In active'),
        ('1', 'Active')
    )
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_assign')
    lecturer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lecturer_assign')
    code = models.UUIDField(default=uuid.uuid4)
    created_on = models.DateTimeField(default=timezone.now)
    status = models.CharField(default=0, max_length=200, choices=STATUS_CHOICES)

    class Meta:
        db_table = "lecturer_student_assignments"
        verbose_name_plural = "lecturer_student_assignments"

    def __str__(self):
        return 'Student: ' + self.student.names + ', Lecturer: ' + self.lecturer.names

    def get_absolute_url(self):
	    return reverse('assignment-details', kwargs={'pk': self.pk})


class StudentLogBook(models.Model):
    STATUS_CHOICES = (
        ('0','Not Approved'),
        ('1', 'Approved')
    )
    label = models.CharField(max_length=500, unique=True, default='Default Logbook')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_logbook')
    code = models.UUIDField(default=uuid.uuid4)
    created_on = models.DateTimeField(default=timezone.now)
    status = models.CharField(default=0, max_length=200, choices=STATUS_CHOICES)

    class Meta:
        db_table = "student_logbooks"
        verbose_name_plural = "student_logbooks"

    def __str__(self):
        return self.student.names + ', ' + self.label

    def get_absolute_url(self):
	    return reverse('logbook-details', kwargs={'pk': self.pk})

class StudentLogBookItem(models.Model):
    STATUS_CHOICES = (
        ('0','Not Approved'),
        ('1', 'Approved')
    )
    code = models.UUIDField(default=uuid.uuid4)
    date = models.CharField(max_length=500, unique=False)
    worked_on = models.CharField(max_length=500, unique=True)
    logbook = models.ForeignKey(StudentLogBook, on_delete=models.CASCADE, default=0)
    created_on = models.DateTimeField(default=timezone.now)
    status = models.CharField(default=0, max_length=200, choices=STATUS_CHOICES)

    class Meta:
        db_table = "student_logbook_items"
        verbose_name_plural = "student_logbook_items"

    def __str__(self):
        return self.student.names + ', ' + self.worked_on + ', ' + str(self.date)

    def get_absolute_url(self):
	    return reverse('logbook-item-details', kwargs={'pk': self.pk})


class StudentAttachmentLocation(models.Model):
    code = models.UUIDField(default=uuid.uuid4)
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_att_loc')
    street = models.CharField(max_length=50, default='')
    lat = models.CharField(max_length=100,default='')
    lng = models.CharField(max_length=100, default='')
    info = models.CharField(max_length=500, default='')

    class Meta:
        db_table = "student_attachment_locations"
        verbose_name_plural = "student_attachment_locations"
    
    def __str__(self):
        return self.student.names

    def get_absolute_url(self):
        return reverse('student-attachment-location-details', kwargs={'pk': self.pk})