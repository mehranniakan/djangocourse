# m
# django.contrib.auth
# import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
# from django.shortcuts import render, redirect, HttpResponseRedirect
# from django.urls import reverse
# from email_validator import validate_email, EmailNotValidError
# from django.contrib import messages
#
# # Create your views here.
# from prf.forms import SignUpForm
#
#
# def Login_View(request):
#     email_v = ''
#     if request.user.is_authenticated:
#         return redirect('/')
#
#     if request.method == 'POST':
#
#         email = request.POST['email']
#         pass_word = request.POST['password']
#
#         try:
#             email_v = validate_email(email)
#         except EmailNotValidError as e:
#             email_v = {'email': None}
#
#         if email_v['email'] == email:
#             get_user = User.objects.filter(email=email)
#             get_user = get_user[0]
#             get_user = get_user.username
#
#             user = authenticate(username=get_user, password=pass_word)
#
#             if user is not None:
#                 login(request, user)
#                 return redirect('/')
#             else:
#                 print('email or pass is wrong')
#                 return render(request, 'account/Login.html')
#         else:
#
#             user = authenticate(username=email, password=pass_word)
#
#             if user is not None:
#                 login(request, user)
#                 return redirect('/')
#             else:
#                 print('user or pass is wrong')
#                 return render(request, 'account/Login.html')
#     elif request.method == 'GET':
#         return render(request, 'account/Login.html')
#
#
# def SignUp_View(request):
#     if request.user.is_authenticated:
#         return redirect('/')
#
#     if request.method == 'POST':
#
#         form = SignUpForm(request.POST)
#
#         if form.is_valid():
#             email = form.cleaned_data.get('email')
#             get_user = User.objects.filter(email=email).count()
#
#             if get_user == 1:
#                 messages.add_message(request, messages.ERROR, "This Email is already exist !")
#             else:
#                 form.save()
#                 return HttpResponseRedirect(reverse('account:login'))
#
#         else:
#             messages.add_message(request, messages.ERROR, "Please check input Parameters !")
#
#     return render(request, 'account/SignUp.html')
#
#
# @login_required
# def Logout(request):
#     if request.user.is_authenticated:
#         logout(request)
#         return redirect('/')
#     else:
#         return render(request, 'account/Login.html')
#
#
# from django.test import TestCase
#
# # Create your tests here.
