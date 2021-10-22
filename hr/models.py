from django.db import models

# Create your models here.


class Employees(models.Model):
    system_id = models.AutoField
    emp_id = models.CharField(max_length=10, default="", blank=False)
    name = models.CharField(max_length=100, default="", blank=False)
    email = models.EmailField(max_length=100, blank=True)
    contact_number = models.IntegerField(default=1234567890, blank=False)
    alternate_contact_number = models.IntegerField(
        default=1234567890, blank=True)
    address = models.TextField(default="No address specified", blank=False)
    birthdate = models.DateField()
    highest_qualification = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    job_title = models.CharField(max_length=100)
    date_of_joining = models.DateField()
    salary = models.IntegerField(default=0)
    expectations = models.TextField(blank=True)
    job_descriptions = models.CharField(max_length=100)
    achivement = models.TextField(max_length=300)
    number_of_projects_handled = models.IntegerField(default=0)
    resume = models.FileField(upload_to='resume')
    employee_image = models.ImageField(upload_to='image')

    def __str__(self):
        return self.system_id
