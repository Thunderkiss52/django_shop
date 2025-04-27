from gc import get_objects

from django.http.response import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Course
# Create your views here.

def index(request):
    courses = Course.objects.all()
    return render(request, 'shop/courses.html', {'courses': courses})
    # return HttpResponse([str(course) + '<br>' for course in courses])

def single_course(request, course_id):
    # Option 1
    # try:
    #     course = Course.objects.get(pk=course_id)
    #     return render(request, 'single_course.html', {'course': course})
    # except Course.DoesNotExist:
    #     raise Http404("Course does not exist")

    # Option 2
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'shop/single_course.html', {'course': course})



