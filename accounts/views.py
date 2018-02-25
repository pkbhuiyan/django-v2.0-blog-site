from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout

# log user in after sign up
def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():     #validate the form
                user = form.save()
                login(request,user)
                return redirect('articles:list')
        else:
            form = UserCreationForm()
        return render(request,'accounts/signup.html',{'form':form})

# log user in
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)  #authenticate user from post data
            if form.is_valid():
                user = form.get_user()
                login(request,user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('articles:list')
        else:
            form = AuthenticationForm()
        return render(request,'accounts/login.html',{'form':form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:list')
