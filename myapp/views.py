from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Topic, Course, Student, Order
from django.shortcuts import render


def index(request):
    #top_list = Topic.objects.all().order_by('id')[:10]
    #response = HttpResponse()
    #heading1 = '<p>' + 'List of topics: ' + '</p>'
    #response.write(heading1)
    #for topic in top_list:
    #    para = '<p>' + str(topic.id) + ': ' + str(topic) + '</p>'
    #    response.write(para)

    #response.write('<br>')

    # List of courses
    #course_list = Course.objects.all().order_by('-price')[:5]
    #heading2 = '<p>' + 'List of Courses: ' + '</p>'
    #response.write(heading2)
    #for course in course_list:
    #    if course.for_everyone:
    #        access = 'This Course is For Everyone!'
    #    else:
    #        access = 'This Course is Not For Everyone!'
    #    line = '<p>' + str(course.price) + ' ' + str(course) + ': ' + access + '</p>'
    #    response.write(line)
    #return response
    top_list = Topic.objects.all().order_by('id')[:10]
    return render(request, 'myapp/index0.html', {'top_list': top_list})

# about view
def about(request):
    return render(request, 'myapp/about0.html')


# detail view

