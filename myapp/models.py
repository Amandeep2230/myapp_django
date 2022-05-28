from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200, default="")

    def __str__(self):
        return "%s %s" % (self.name, self.category)


class Course(models.Model):
    topic = models.ForeignKey(Topic, related_name='courses', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    for_everyone = models.BooleanField(default=True)
    description = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return "%s" % (self.name)


class Student(User):
    CITY_CHOICES = [('WS', 'Windsor'),
                    ('CG', 'Calgary'),
                    ('MR', 'Montreal'),
                    ('VC', 'Vancouver')]
    school = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=2, choices=CITY_CHOICES, default='WS')
    interested_in = models.ManyToManyField(Topic)

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)


class Order(models.Model):
    ORDER_STATUS = [(0, 'Cancelled'),
                    (1, 'Order Confirmed')]
    course = models.ForeignKey(Course, related_name="course", on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name="student", on_delete=models.CASCADE)
    order_status = models.IntegerField(choices=ORDER_STATUS, default=0)
    order_date = models.DateField()

    def __str__(self):
        return "{0} {1}".format(self.order_status, self.order_date)

    def total_cost(self):
        total = 0
        if self.course == Course.topic:
            total += Course.price
        else:
            total += 0
        return total
