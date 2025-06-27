from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


# Create your views here.
def show_main(request):
    print('Success!')
    return render(request, 'main_page.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('show_main')
        else:
            messages.error(request, 'invalid password or username')
            return redirect('login_user')
    return render(request, 'login.html')


def create_user(request):
    if request.method == 'POST':
      
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        validate = User.objects.filter(username=username).exists()
        if validate:
            messages.error(request, 'Username Taken')
            return redirect('create_user')
        # elif not email.endswith('.com'):
        #     messages.error(request, 'Email must end with .com')
        #     return redirect('create_user')
        # elif not email == 'gmail.com':
        #     messages.error(request, 'Email must be gmail.com')
        #     return redirect('create_user')
        else:
            query_set = User.objects.create_user(
                                             username=username,
                                             email=email,
                                             password=password)
            query_set.save()
            messages.success(request, 'Account Created Successfully!')
            return redirect('create_user')
    return render(request, 'user_form.html')


def user_out(request):
        logout(request)
        return redirect('login_user')


@login_required
def delete_user(request):
    if request.method == 'POST':
        request.user.delete()
        return JsonResponse({'success':'Account deleted successfully!'}, status=200)
    return JsonResponse({'error':'something went wrong'}, status=405)


def delete(request):
    if request.method == 'GET':
        for i in User.objects.all():
            if i.email.endswith('.com'):
                continue
            else:
                i.delete()
                return JsonResponse({'success':'Deleted user with invalid email'}, status=200)
    return JsonResponse({'error':'no user with invalid email found'}, status=404)
        
