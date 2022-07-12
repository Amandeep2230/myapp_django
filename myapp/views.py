from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .forms import OrderForm, InterestForm
from .models import Topic, Course, Student, Order
from django.shortcuts import render
from .forms import OrderForm

def index(request):
    top_list = Topic.objects.all().order_by('id')[:10]
<<<<<<< HEAD
    return render(request, 'myapp/index.html', {'top_list': top_list})
=======
    '''response = HttpResponse()
    heading1 = '<p>' + 'List of topics: ' + '</p>'
    response.write(heading1)
    for topic in top_list:
        para = '<p>' + str(topic.id) + ': ' + str(topic) + '</p>'
        response.write(para)

    response.write('<br>')

    # List of courses
    course_list = Course.objects.all().order_by('-price')[:5]
    heading2 = '<p>' + 'List of Courses: ' + '</p>'
    response.write(heading2)
    for course in course_list:
        if course.for_everyone:
            access = 'This Course is For Everyone!'
        else:
            access = 'This Course is Not For Everyone!'
        line = '<p>' + str(course.price) + ' ' + str(course) + ': ' + access + '</p>'
        response.write(line)
    return response'''
    return render(request, 'myapp/index0.html', {'top_list': top_list})

>>>>>>> f42d2cf72a5dc45cf03e1af5ed19c50606c4aff3


# about view
def about(request):
    response = HttpResponse()
    '''response.write('<h2 fontWeight="bold">This is an E-learning Website! Search our Topics to find all available '
                   'Courses.</h2>')
    return response'''
    return render(request, 'myapp/about0.html')


# detail view
def detail(request, top_no):
    top = Topic.objects.filter(id=top_no)
    get_object_or_404(top)  # gives 404 error if id not found
    course_list = Course.objects.filter(topic__name=str(top.get()))
    '''response = HttpResponse()
    response.write('<h1>' + str(top.get()) + '</h1>')
    response.write('<br> <h2>Category: ' + str(top.get().category) + '</h2>')

<<<<<<< HEAD

# updated till lab 6
def courses(request):
    courlist = Course.objects.all().order_by('id')
    return render(request, 'myapp/courses.html', {'courlist': courlist})


# Lab 8 - place order view
def place_order(request):
    msg = ''
    courlist = Course.objects.all()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if order.levels <= order.course.stages:
                order.save()
                msg = 'Your course has been ordered successfully.'
                if order.course.price > 150.00:     # check if price > $150
                    order.course.price = order.course.discount()    # apply discount

            else:
                msg = 'You exceeded the number of levels for this course.'
            return render(request, 'myapp/order_response.html', {'msg': msg})
    else:
        form = OrderForm()
    return render(request, 'myapp/placeorder.html', {'form': form, 'msg': msg, 'courlist': courlist})


# Lab 8 - course detail view
def coursedetail(request, cour_id):
    msg = ''
    course = Course.objects.get(id=cour_id)

    if not course.for_everyone:
        msg = 'This course is not for everyone'

    if request.method == 'POST':    # if method is POST
        form = InterestForm(request.POST)
        if form.is_valid():   # check if form is valid
            is_interested = int(form.cleaned_data['interested'])
            course.interested += is_interested  # increment interested in db
            course.save()           # save db
            return HttpResponseRedirect('/myapp/')  # redirect to main page
    else:   # if method is GET
        form = InterestForm()
    return render(request, 'myapp/coursedetail.html', {'course': course, 'msg': msg, 'form': form})
=======
    course_list = Course.objects.filter(topic__name=str(top.get()))
    response.write('<br> <h2>Courses: </h2>')
    for course in course_list:
        line = '<p>' + str(course) + '</p>'
        response.write(line)

    return response'''
    return render(request, 'myapp/detail0.html', {'top_obj': top.get(),
                                                  'course_list': course_list})
>>>>>>> f42d2cf72a5dc45cf03e1af5ed19c50606c4aff3
