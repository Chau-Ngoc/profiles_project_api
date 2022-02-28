from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.conf import settings


class UserProfileManager(BaseUserManager):
    """Manager for user profiles."""

    def create_user(self, email, first_name, last_name, password=None):
        """Create a new user profile.

        :param email: the user's email.
        :type email: str
        :param first_name: the user's first name.
        :type first_name: str
        :param last_name: the user's last name.
        :type last_name: str
        :param password: the password used for authentication, defaults to None.
        :type password: str, optional
        :return: a user
        :rtype: UserProfile
        """
        if not email:
            raise ValueError("User must have an email address")

        email = self.normalize_email(email)
        user = self.model(
            email=email, last_name=last_name, first_name=first_name
        )

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, first_name, last_name, password):
        """Create a superuser with the given details.

        :param email: the superuser's email
        :type email: str
        :param first_name: the superuser's first name
        :type first_name: str
        :param last_name: the superuser's last name
        :type last_name: str
        :param password: the superuser's password.
        :type password: str
        :return: a superuser
        :rtype: UserProfile
        """
        user = self.create_user(email, first_name, last_name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for the users in the system."""

    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def get_full_name(self):
        """Retrive the full name of user."""
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        """Retrive the last name of user."""
        return self.last_name

    def __str__(self) -> str:
        """Return string representation for our user.

        :return: the email address of the user.
        :rtype: str
        """
        return self.email


class Feed(models.Model):
    """The user's status feed."""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status_text = models.TextField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """Return the status text as a string representation of the model."""
        return self.status_text
