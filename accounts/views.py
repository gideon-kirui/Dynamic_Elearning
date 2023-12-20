from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . forms import LoginForm, UserRegistrationform, userEditForm, ProfileEditForm, AddTopicForm, StudentMarks, profileEditLForm
from django.contrib.auth.models import User
from . models import S_register, L_register
from base.models import Unit, Topic, Marks
from django.contrib.auth.decorators import login_required

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            login(request, user)
            myuser = str(user)
            firstl = myuser[0]
            if firstl == 'S':
                S_register.objects.create(student=user)
                return redirect('accounts:updated_d')
            elif firstl == 'L':
                L_register.objects.create(lecturer=user)
                return redirect('accounts:updated_l')
    else:
        form = LoginForm()

    context = {'form':form}
    return render(request, 'accounts/login.html', context)

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            login(request, user)
            return redirect('base:home')
    else:
        form = LoginForm()

    context = {'form':form}
    return render(request, 'accounts/login.html', context)

def userlogout(request):
    logout(request)
    return redirect('base:home')

def user_registration(request):
    if request.method == "POST":
        form = UserRegistrationform(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password2'])
            new_user.save()
            return redirect('accounts:login')
    else:
        form = UserRegistrationform()

    context = {'form':form}
    return render(request, 'accounts/register.html', context)

def UpdateDetails(request):
    if request.method == 'POST':
        user_form = userEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.s_register, data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('base:home')

    else:
        user_form = userEditForm(instance=request.user)
        profile_form = ProfileEditForm()

    context = {'user_form':user_form, 'profile_form':profile_form}

    return render(request, 'accounts/updated.html', context)

def LUpdateDetails(request):
    if request.method == 'POST':
        user_form = userEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.l_register, data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('base:home')

    else:
        user_form = userEditForm(instance=request.user)
        profile_form = profileEditLForm()

    context = {'user_form':user_form, 'profile_form':profile_form}

    return render(request, 'accounts/updated.html', context)

@login_required(login_url='accounts:loginuser')
def addtopic(request, unit_id):
    unit = Unit.objects.get(id=unit_id)
    usert = str(request.user)[0]
    if usert == 'L':
        if request.method == 'POST':
            form = AddTopicForm(data=request.POST)
            if form.is_valid():
                new_form = form.save(commit=False)
                new_form.unit = unit
                new_form.save()
                return redirect('base:unit', unit.id)
        else:
            form = AddTopicForm()
        context = {'form':form, 'unit':unit, 'usert':usert}
        return render(request, 'accounts/addtopic.html', context)
    else:
        return redirect('base:unit', unit.id)

@login_required(login_url='accounts:loginuser')
def edittopic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    unit = Unit.objects.get(topic=topic)
    usert = str(request.user)[0]
    if usert == 'L':
        if request.method == 'POST':
            form = AddTopicForm(instance=topic, data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('base:unit', unit.id)
        else:
            form = AddTopicForm(instance=topic)

        context = {'form':form, 'usert':usert}
        return render(request, 'accounts/edittopic.html', context)
    else:
        return redirect('base:unit', unit.id)

@login_required(login_url='accounts:loginuser')
def deletetopic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    unit = Unit.objects.get(topic=topic)
    usert = str(request.user)[0]
    if usert == 'L':
        if request.method == 'POST':
            topic.delete()
            return redirect('base:unit', unit.id)
        else:
            obj = topic

        context = {'obj':obj}
        return render(request, 'base/delete.html', context)
    else:
        return redirect('base:unit', unit.id)

@login_required(login_url='accounts:loginuser')
def addstudentmarks(request, unit_id):
    unit = Unit.objects.get(id=unit_id)
    usert = str(request.user)[0]
    if request.method == 'POST':
        form = StudentMarks(data=request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.unit = unit
            new_form.save()
            return redirect('base:unit', unit.id)
    else:
        form = StudentMarks()
    context = {'form':form, 'usert':usert}
    return render(request, 'accounts/addmarks.html', context)

@login_required(login_url='accounts:loginuser')
def editmarks(request, marks_id):
    marks = Marks.objects.get(id=marks_id)
    unit = Unit.objects.get(unitmarks=marks)
    usert = str(request.user)[0]
    if usert == 'L':
        if request.method == 'POST':
            form = StudentMarks(instance=marks, data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('base:unit', unit.id)
        else:
            form = StudentMarks(instance=marks)

        context = {'form':form, 'usert':usert}
        return render(request, 'accounts/editmarks.html', context)
    else:
        return redirect('base:unit', unit.id)