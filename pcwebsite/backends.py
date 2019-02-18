from django_cas_ng.backends import CASBackend
from django.contrib import messages
from django.conf import settings

from users.models import Member

class CustomCASBackend(CASBackend):
    def user_can_authenticate(self, user):

        if user is not None:
            if isinstance(user, Member): # Check if the user has an account on the website
                if user.is_active: # Check if the user has an active account (not "deleted" or deactivated)
                    return True
                else:
                    return False
            else:
                return False

        else:
            return False
