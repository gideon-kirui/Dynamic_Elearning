from django.shortcuts import render, redirect
from .models import School, Course, Unit, Marks
from django.contrib.auth.decorators import login_required

def home(request):
    schools = School.objects.all()
    allcourses = Course.objects.all()
    mycourse = ''
    usert = str(request.user)[0]
    if usert == 'S':
        user = request.user.s_register
        mycourse = Course.objects.get(studentincourse=user)

    elif usert == 'L':
        user = request.user.l_register
        mycourse = Course.objects.get(lecturerassigned=user)

    context = {'schools':schools, 'allcourses':allcourses, 'usert':usert, 'mycourse':mycourse}
    return render(request, 'base/index.html', context)

def school(request, sch_id):
    school = School.objects.get(id=sch_id)
    courses = school.course.all()
    mycourse = ''
    usert = str(request.user)[0]
    if usert == 'S':
        user = request.user.s_register
        mycourse = Course.objects.get(studentincourse=user)
        
    if usert == 'L':
        user = request.user.l_register
        mycourse = Course.objects.get(lecturerassigned=user)

    context = {'courses':courses, 'school':school, 'usert':usert, 'mycourse':mycourse}
    return render(request, 'base/index.html', context)

@login_required(login_url='accounts:loginuser')
def course(request, course_id):
    user = request.user
    course = Course.objects.get(id=course_id)
    
    usert = str(request.user)[0]
    if usert == 'S':
        if user.s_register.course == course:
            year = user.s_register.year
            cuni = user.s_register.course
            unic = cuni.courseunit.all()
            yunits = year.unit.all()
            context = {'course':course, 'year':year, 'unic':unic, 'usert':usert, 'yunits':yunits}
            return render(request, 'base/course.html', context)
        
        else:
            return redirect('base:home')

    usert = str(request.user)[0]
    if usert == 'L':
        if user.l_register.course == course:
            year = user.l_register.year
            cuni = user.l_register.course
            unic = cuni.courseunit.all()
            yunits = year.unit.all()
            context = {'course':course, 'year':year, 'unic':unic, 'usert':usert, 'yunits':yunits}
            return render(request, 'base/course.html', context)
        else:
            return redirect('base:home')
        
    
    
@login_required(login_url='accounts:loginuser')
def unit(request, unit_id):
    usert = str(request.user)[0]
    studentmks = ''
    if usert == 'S':
        studentmks = request.user.stdmarks
    unit = Unit.objects.get(id=unit_id)
    marks = unit.unitmarks.all()
    course = Course.objects.get(courseunit=unit)
    topics = unit.topic.all()
    context = {'course':course, 'topics':topics, 'unit':unit, 'marks':marks, 'usert':usert, 'studentmks':studentmks}
    return render(request, 'base/unit.html', context)