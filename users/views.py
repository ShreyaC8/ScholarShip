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


# from .scholarship import schol_type

# def search_schol(request):
#      query = request.GET.get('query', '')
#      results = {}

#      if query:
#          # Iterate through the main categories
#          for category in schol_type.items():
#              for schol in category.items():
#                 if query.lower() in category.lower():
#                     if category not in results:
#                         results[category] = {}
#                     results[category] = schol_type[category][schol]
#      # Debug: Print the results to the console for troubleshooting
#      return render(request, 'users/search.html', {'results': results, 'query': query})

# import logging
# from django.shortcuts import render
# from .scholarship import get_generic_scholarships

# logger = logging.getLogger(__name__)

# def search_scholarships(request):
#     generic_scholarships = get_generic_scholarships()
#     logger.info(f"Generic scholarships: {generic_scholarships}")
#     query = request.GET.get('q')
#     if query:
#         filtered_scholarships = {
#             name: details for name, details in generic_scholarships.items()
#             if query.lower() in name.lower() or query.lower() in details['desc'].lower()
#         }
#     else:
#         filtered_scholarships = generic_scholarships
#     return render(request, 'search.html', {'scholarships': filtered_scholarships})

# from django.http import HttpResponse

# def test_view(request):
#     return HttpResponse("Test view is working!")


