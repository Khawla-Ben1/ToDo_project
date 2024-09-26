# backends.py
from django.contrib.auth.backends import ModelBackend
from .models import UserAccount

class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        print(f"Attempting to authenticate user: {email}")
        try:
            user = UserAccount.objects.get(email=email)
            print(f"User found: {user.email}")
        except UserAccount.DoesNotExist:
            print("User not found")
            return None
        
        if user.check_password(password):
            print("Password is correct")
            return user
        else:
            print("Password is incorrect")
            return None
