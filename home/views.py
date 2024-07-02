from django.shortcuts import render, redirect
from .models import Recipe
from django.contrib.auth import login, authenticate, logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

@login_required(login_url='/login/')
def recipes(request):
    if request.method == 'POST':
        data = request.POST
        day = data.get('day')
        name = data.get('name')
        description = data.get('description')
        Recipe.objects.create(
            day=day,
            name=name,
            description=description
        )
        return redirect('recipes')
    
    queryset = Recipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(
            day__contains=request.GET.get('search')
        )

    context = {'recipes': queryset}
    return render(request, 'recipe.html', context)

@login_required(login_url='/login/')
def update(request, id):
    queryset = Recipe.objects.get(id=id)
    if request.method == 'POST':
        data = request.POST
        day = data.get('day')
        name = data.get('name')
        description = data.get('description')

        queryset.day = day
        queryset.name = name
        queryset.description = description
        queryset.save()
        return redirect('recipes')

    context = {'recipe': queryset}
    return render(request, 'update_recipe.html', context)

@login_required(login_url='/login/')
def delete(request, id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    return redirect('recipes')

def login_page(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username)

            if not user_obj.exists():
                messages.error(request, 'Username not found')
                return redirect('login')
            
            user_obj = authenticate(username=username, password=password)

            if user_obj:
                login(request, user_obj)
                return redirect('recipes')
            messages.error(request, "Wrong Password")
            return redirect('login')
        
        except Exception as e:
            messages.error(request, 'Something went wrong')
            return redirect('register')
    return render(request, 'login.html')

def register_page(request):
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username)
            if user_obj.exists():
                messages.error(request, "Username is taken")
                return redirect('register')
            user_obj = User.objects.create(username=username)
            user_obj.set_password(password)
            user_obj.save()
            messages.success(request, "Account created")
            return redirect('login')
        except Exception as e:
            messages.error(request, "Something went wrong")
            return redirect('register')
    return render(request, "register.html")

def logout_view(request):
    django_logout(request)
    return redirect('login')

@login_required(login_url='/login/')
def pdf(request):
    if request.method == 'POST':
        data = request.POST    
        day = data.get('day')
        name = data.get('name')
        description = data.get('description')
         
        Recipe.objects.create(
            day=day,
            name=name,
            description=description,
        )
        return redirect('pdf')
    
    queryset = Recipe.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(
            day__contains=request.GET.get('search')
        )

    context = {'recipes': queryset}
    return render(request, 'pdf.html', context)
