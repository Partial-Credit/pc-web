from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime



class Member(AbstractUser):

    SOPRANO = 'S'
    ALTO    = 'A'
    TENOR   = 'T'
    BASS    = 'B'

    VOICE_PART_CHOICES = (
        (SOPRANO, 'Soprano'),
        (ALTO, 'Alto'),
        (TENOR, 'Tenor'),
        (BASS, 'Bass'),
    )

    current_member = models.BooleanField(default=False)
    bio = models.TextField(blank=True)
    nickname = models.CharField(max_length=250, blank=True)
    voice_part = models.CharField(
        max_length=1,
        choices=VOICE_PART_CHOICES,
        blank=True,
    )
    major = models.CharField(max_length=100, blank=True)

    other_email = models.EmailField(max_length=254, blank=True)

    class_year = models.PositiveSmallIntegerField (
        validators=[ MinValueValidator(2000) ],
        blank=True,
        null=True,
        help_text = "Please use the following format: <em>YYYY</em>."
    )

    profile = models.ImageField(blank=True, default='default.png')

    def __str__(self):
        return self.username

    class Meta:
        app_label = 'users'
        verbose_name = "Member"

