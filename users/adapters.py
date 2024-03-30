# adapters.py
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.shortcuts import redirect

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        # Check if the provider is Google and if it's the user's first login
        if sociallogin.account.provider == 'google' and not sociallogin.is_existing:
            # Redirect to another page
            print("Redirecting to another page")
            return redirect('other')

        else:
            print("Redirecting to home")
            return redirect('home')
        


