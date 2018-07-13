from django_cas_ng.backends import CASBackend
from django.contrib import messages
from django.conf import settings

from users.models import Member

class CustomCASBackend(CASBackend):
    def user_can_authenticate(self, user):

        if user is not None:

            if isinstance(user, Member):
                return True
            else:
                return False

        else:
            return False
