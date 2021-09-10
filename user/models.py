from django.utils.functional import cached_property
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager
from . import constants

class User(AbstractUser):
    team = models.ForeignKey('Team', on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(unique=True)
    role = models.IntegerField(choices=constants.ROLE_TYPES, default=constants.ROLE_DEVELOPER)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = UserManager()

    @cached_property
    def is_developer(self):
        return self.role == constants.ROLE_DEVELOPER

    @cached_property
    def is_team_manager(self):
        return self.role == constants.ROLE_TEAM_MANAGER

    @cached_property
    def is_admin(self):
        return self.role == constants.ROLE_ADMIN

    def __str__(self):
        return '{} {} ({})'.format(self.first_name, self.last_name, self.email)
    
    @cached_property
    def team_manager(self):
        return self.team.user_set.filter(role=constants.ROLE_TEAM_MANAGER).first()

class Team(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    profile_type = models.IntegerField(choices=constants.PROFILE_TYPES)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=50)
    dob = models.DateField('Date of Birth', null=True)
    gender = models.IntegerField(choices=constants.PROFILE_GENDERS, default=constants.PROFILE_GENDER_MALE)
    extra_info = models.CharField(max_length=1024, null=True)
    
    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Account(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    email = models.EmailField(null=True)
    platform_type = models.CharField(max_length=30, choices=constants.PLATFORM_TYPES)
    password = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    extra_info = models.CharField(max_length=1024, null=True)
    url = models.CharField('URL', max_length=200)
    # TODO: Implement Linked Profile here...

    class Meta:
        unique_together = ('profile', 'email', 'platform_type')
    
    def __str__(self):
        return '{}({})'.format(self.recovery_email, self.platform_type)


class AccountSecurityQA(models.Model):
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)

    def __str__(self):
        return '{} {}'.format(self.question, self.account)
