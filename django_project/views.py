# views.py

from django.shortcuts import render, redirect
from .models import MyUser, Gift


def home(request):
    if 'user_id' in request.session:
        user = MyUser.objects.get(id=request.session['user_id'])
        return render(request, 'home.html', {'user': user})
    return render(request, 'error.html', {'message': 'Login is required.'})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = MyUser.objects.get(username=username, password=password)
            request.session['user_id'] = user.id
            return redirect('home')
        except MyUser.DoesNotExist:
            return render(request, 'home.html',
                          {'error': 'Invalid username or password.'})
    return render(request, 'login.html')


def registration(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = MyUser.objects.create(email=email,
                                         username=username,
                                         password=password)
            request.session['user_id'] = user.id
            return redirect('home')
        except Exception as e:
            return render(request, 'registration.html',
                          {'error': f'Error during registration: {str(e)}'})
    return render(request, 'registration.html')


def users(request):
    if 'user_id' in request.session:
        # Get all other users
        users = MyUser.objects.exclude(id=request.session['user_id'])

        if request.method == 'POST':
            selected_user_id = request.POST.get('selected_user')
            return redirect('other_users_gifts', user_id=selected_user_id)

        return render(
            request, 'users.html', {
                'users': users,
                'user': MyUser.objects.get(id=request.session['user_id'])
            })
    return render(request, 'error.html', {'message': 'Login is required.'})


def gifts(request):
    if 'user_id' in request.session:
        user = MyUser.objects.get(id=request.session['user_id'])
        gifts = Gift.objects.filter(user=user)

        if request.method == 'POST':
            # Handle adding a new gift logic here
            gift_name = request.POST['gift_name']
            Gift.objects.create(user=user, name=gift_name)
            return redirect('gifts')

        return render(request, 'gifts.html', {'user': user, 'gifts': gifts})
    return render(request, 'error.html', {'message': 'Login is required.'})


def other_users_gifts(request, user_id):
    if 'user_id' in request.session:
        try:
            other_user = MyUser.objects.get(id=user_id)
            gifts = Gift.objects.filter(user=other_user)
            return render(request, 'other_users_gifts.html', {
                'other_user': other_user,
                'gifts': gifts
            })
        except MyUser.DoesNotExist:
            return render(request, 'error.html',
                          {'message': 'User not found.'})
        except Exception as e:
            return render(request, 'error.html',
                          {'message': f'Error: {str(e)}'})
    return render(request, 'error.html', {'message': 'Login is required.'})


def error(request):
    return render(request, 'error.html', {'message': 'Login is required.'})
