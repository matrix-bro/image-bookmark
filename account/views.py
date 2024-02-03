from django.shortcuts import render
from account.forms import RegistrationForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'account/index.html')

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)

            new_user.set_password(form.cleaned_data['password'])
            new_user.save()

            return render(request, 'account/login.html')

    else:
        form = RegistrationForm()

    return render(request, 'account/register.html', {
        "form": form,
    })

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html')