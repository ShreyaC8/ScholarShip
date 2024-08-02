from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, LoginForm, UpdateUserForm, UpdateProfileForm

from django.shortcuts import render


def home(request):
    return render(request, 'users/home.html')


class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'users/register.html'

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})


# Class based view that extends from the built in login view to add a remember me functionality
class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('users-home')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'users/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users-home')


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})

from django.shortcuts import render

# views.py
from django.shortcuts import render
from .scholarship import schol_type  # Ensure you have the correct path to import schol_type

def generic_view(request):
    generic_scholarships = schol_type.get("generic", {})
    return render(request, 'users/generic.html', {'generic_scholarships': generic_scholarships})

def agri_vet_view(request):
    agri_vet_scholarships = schol_type.get("agri_vet", {})
    return render(request, 'users/agri_vet.html', {'agri_vet_scholarships': agri_vet_scholarships})

def comp_math_view(request):
    comp_math_scholarships = schol_type.get("comp_math", {})
    return render(request, 'users/comp_math.html', {'comp_math_scholarships': comp_math_scholarships})

def sci_view(request):
    sci_scholarships = schol_type.get("sci", {})
    return render(request, 'users/sci.html', {'sci_scholarships': sci_scholarships})

def art_design_view(request):
    art_design_scholarships = schol_type.get("art_design", {})
    return render(request, 'users/art_design.html', {'art_design_scholarships': art_design_scholarships})

def engin_tech_view(request):
    engin_tech_scholarships = schol_type.get("engin_tech", {})
    return render(request, 'users/engin_tech.html', {'engin_tech_scholarships': engin_tech_scholarships})

def health_med_view(request):
    health_med_scholarships = schol_type.get("health_med", {})
    return render(request, 'users/health_med.html', {'health_med_scholarships': health_med_scholarships})

def humanities_view(request):
    humanities_scholarships = schol_type.get("humanities", {})
    return render(request, 'users/humanities.html', {'humanities_scholarships': humanities_scholarships})

def law_view(request):
    law_scholarships = schol_type.get("law", {})
    return render(request, 'users/law.html', {'law_scholarships': law_scholarships})

def fitness_view(request):
    fitness_scholarships = schol_type.get("fitness", {})
    return render(request, 'users/fitness.html', {'fitness_scholarships': fitness_scholarships})

def social_comms_view(request):
    social_comms_scholarships = schol_type.get("social_comms", {})
    return render(request, 'users/social_comms.html', {'social_comms_scholarships': social_comms_scholarships})

def trav_tourism_view(request):
    trav_tourism_scholarships = schol_type.get("trav_tourism", {})
    return render(request, 'users/trav_tourism.html', {'trav_tourism_scholarships': trav_tourism_scholarships})
