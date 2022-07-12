from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .forms import OrderForm, InterestForm
from .models import Topic, Course, Student, Order
from django.shortcuts import render
from .forms import OrderForm

def index(request):
    top_list = Topic.objects.all().order_by('id')[:10]
    return render(request, 'myapp/index.html', {'top_list': top_list})


# about view
def about(request):
    return render(request, 'myapp/about.html')


# detail view
def detail(request, top_no):
    top = Topic.objects.filter(id=top_no)
    get_object_or_404(top)  # gives 404 error if id not found
    course_list = Course.objects.filter(topic__name=str(top.get()))
    return render(request, 'myapp/detail.html', {'top_obj': top.get(),
                                                  'course_list': course_list})


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