from django.db import models
from django.urls import reverse
import uuid
from django.utils import timezone

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


class Lecturer (models.Model):
    STATUS_CHOICES = (
       ('0','In active'),
       ('1', 'Active')
    )
    names = models.CharField(max_length=50, unique=True)
    code = models.UUIDField(default=uuid.uuid4)
    phone = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=50, default='')
    courses = models.ManyToManyField(Course)
    created_on = models.DateTimeField(default=timezone.now)
    status = models.CharField(default=0, max_length=200, choices=STATUS_CHOICES)

    class Meta:
        db_table = "lecturers"
        verbose_name_plural = "lecturers"
    
    def __str__(self):
        return self.names

    def get_absolute_url(self):
        return reverse('lecturer-details', kwargs={'pk': self.pk})

class Student (models.Model):
    STATUS_CHOICES = (
       ('0','In active'),
       ('1', 'Active')
    )
    names = models.CharField(max_length=50, unique=True)
    code = models.UUIDField(default=uuid.uuid4)
    phone = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=50, default='')
    regno = models.CharField(max_length=50, default='')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=timezone.now)
    status = models.CharField(default=0, max_length=200, choices=STATUS_CHOICES)

    class Meta:
        db_table = "students"
        verbose_name_plural = "students"
    
    def __str__(self):
        return self.names

    def get_absolute_url(self):
        return reverse('student-details', kwargs={'pk': self.pk})

class LecturerStudentAssignment(models.Model):
    STATUS_CHOICES = (
        ('0','In active'),
        ('1', 'Active')
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
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
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
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
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    code = models.UUIDField(default=uuid.uuid4)
    date = models.DateField()
    worked_on = models.CharField(max_length=500, unique=True)
    logbook = models.ForeignKey(StudentLogBook, on_delete=models.CASCADE, default=1)
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
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
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