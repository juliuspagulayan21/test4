from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(
        upload_to='profile_images/',
        blank=True,
        null=True,
        default='profile_images/default_profile.jpg'
    )
    role = models.CharField(
        max_length=20,
        choices=[
            ('Resident', 'Resident'),
            ('LGU Member', 'LGU Member'),
        ],
        blank=True,
        null=True,
    )
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username