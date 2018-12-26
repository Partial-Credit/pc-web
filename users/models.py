from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.postgres.fields import ArrayField
from multiselectfield import MultiSelectField
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

    POSITION_CHOICES = (
        ('MD', 'Musical Director'),
        ('AMD', 'Assistant Musical Director'),
        ('Secretary', 'Secretary'),
        ('Business Manager', 'Business Manager'),
        ('Treasurer', 'Treasurer'),
        ('Webmaster', 'Webmaster'),
        ('Public Relations Director', 'Public Relations Director'),
    )

    current_member = models.BooleanField(default=False)
    bio = models.TextField(blank=True)
    nickname = models.CharField(max_length=250, blank=True)
    position = MultiSelectField(max_length=30, choices=POSITION_CHOICES,blank=True, default=False)
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

    hidden = models.BooleanField(default=False)

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)

    class Meta:
        app_label = 'users'
        verbose_name = "Member"
        permissions = [
            ('change_other_member', 'can change other users'),
        ]
