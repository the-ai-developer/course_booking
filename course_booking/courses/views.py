from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Course, Enrollment
from .forms import CourseForm

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

@login_required
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        Enrollment.objects.create(user=request.user, course=course)
        return redirect('course_list')
    return render(request, 'courses/course_detail.html', {'course': course})

@login_required
def course_edit(request, pk=None):
    if pk:
        course = get_object_or_404(Course, pk=pk)
    else:
        course = Course()

    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'courses/course_edit.html', {'form': form})

def home(request):
    return render(request, 'courses/home.html')

@login_required
def dashboard(request):
    courses = Course.objects.all()
    enrollments = Enrollment.objects.all()
    course_popularity = {course: enrollments.filter(course=course).count() for course in courses}
    return render(request, 'courses/dashboard.html', {'course_popularity': course_popularity})


def aboutus(request):
    return render(request, 'courses/aboutus.html')


def contact(request):
    return render(request, 'courses/contactus.html')