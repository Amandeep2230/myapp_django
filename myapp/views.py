from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .forms import OrderForm, InterestForm
from .models import Topic, Course, Student, Order
from django.shortcuts import render
from .forms import OrderForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from datetime import datetime


# lab9 login view
def user_login(request):
    if request.method == 'POST':

        '''
        # lab 9 testing cookie
        
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
            return HttpResponse("<h1>Test cookie worked</h1>")
        else:
            return HttpResponse("<h1>cookies not enables</h1>")
        '''

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                # store date and time in session
                request.session['last_login'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                # set expiry to 1 hour
                # uncomment to set session expiry
                # request.session.set_expiry(3600)
                return HttpResponseRedirect(reverse('myapp:index'))
            else:
                return HttpResponse('<h1>Your account is disabled.</h1>')
        else:
            return HttpResponse('<h1>Invalid login details.</h1>')
    else:
       # request.session.set_test_cookie()
        return render(request, 'myapp/login.html')


@login_required
def user_logout(request):
    # logout(request)
    try:
        del request.session['last_login']
    except KeyError:
        pass
    return HttpResponseRedirect(reverse(('myapp:index')))


# lab 9 my account
#@login_required
def myaccount(request):
    user = request.user     # get current user

    if user.is_authenticated:   # check if user logged in
        u = User.objects.get(username=user)
        try:
            student = Student.objects.get(username=u)
            orders = Order.objects.filter(student__id=student.id)
            topics = Student.objects.filter(username=u).values_list('interested_in__name', flat=True)

            return render(request, 'myapp/myaccount.html', {'student': student, 'orders': orders, 'topics': topics})

        except Student.DoesNotExist:
            return HttpResponse('<h1>You are not a registered student!</h1>')
    else:
        return HttpResponse('<h1>User not logged in!</h1>')


def index(request):
    if request.session.get('last_login', False):    # check if session exists
        msg = request.session['last_login']
        user = request.user
        islogged = True
    else:
        msg = 'Your last login was more than an hour ago'
        user = 'User'
        islogged = False

    top_list = Topic.objects.all().order_by('id')[:10]
    return render(request, 'myapp/index.html', {'top_list': top_list, 'msg': msg, 'user': user, 'islogged': islogged})


# about view
def about(request):

    if request.session.get('last_login', False):
        user = request.user
    else:
        user = 'User'

    if request.COOKIES.get('about_visits'):     # check if cookie exists
        visits = int(request.COOKIES.get('about_visits')) + 1   # increment number of visits
        response = render(request, 'myapp/about.html', {'num_visits': visits, 'user': user})

    else:
        visits = 1
        response = render(request, 'myapp/about.html', {'num_visits': visits, 'user': user})

    response.set_cookie('about_visits', visits, max_age=300)  # set cookie with updated value and age of 5 mins
    return response


# detail view
def detail(request, top_no):

    if request.session.get('last_login', False):
        user = request.user
    else:
        user = 'User'

    top = Topic.objects.filter(id=top_no)
    get_object_or_404(top)  # gives 404 error if id not found
    course_list = Course.objects.filter(topic__name=str(top.get().name))
    return render(request, 'myapp/detail.html', {'top_obj': top.get(),
                                                  'course_list': course_list, 'user': user})


# updated till lab 6
def courses(request):

    if request.session.get('last_login', False):
        user = request.user
    else:
        user = 'User'

    courlist = Course.objects.all().order_by('id')
    return render(request, 'myapp/courses.html', {'courlist': courlist, 'user': user})


# Lab 8 - place order view
def place_order(request):
    msg = ''
    courlist = Course.objects.all()


    if request.session.get('last_login', False):
        user = request.user
    else:
        user = 'User'


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
            return render(request, 'myapp/order_response.html', {'msg': msg, 'user': user})
    else:
        form = OrderForm()
    return render(request, 'myapp/placeorder.html', {'form': form, 'msg': msg, 'courlist': courlist, 'user': user})


# Lab 8 - course detail view
def coursedetail(request, cour_id):
    msg = ''
    course = Course.objects.get(id=cour_id)

    if request.session.get('last_login', False):
        user = request.user
    else:
        user = 'User'

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
    return render(request, 'myapp/coursedetail.html', {'course': course, 'msg': msg, 'form': form, 'user': user})
