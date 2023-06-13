# from django.urls import reverse
# from django.utils.text import slugify  # converts into slug format


# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator, RegexValidator
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser


class ScribbleQuest_User(AbstractUser):
    FName = models.CharField(max_length=50, verbose_name="First Name")
    LName = models.CharField(max_length=50, verbose_name="Last Name")
    email = models.EmailField(max_length=254, verbose_name="Email", unique=True)
    grade = models.IntegerField(MinValueValidator(0))
    password = models.CharField(
        max_length=125,
        verbose_name="Password",
        validators=[
            MinLengthValidator(
                8, message="Password must be at least 8 characters long."),
            RegexValidator(
                regex=r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]+$',
                message="Password must contain at least one letter and one number."
            ),
        ],
    )


    def __str__(self):
        return f"{self.FName} {self.LName} {self.email}"

    def save(self, *args, **kwargs):
         # Hash the password before saving
        self.password = make_password(self.password)
    
        created = not self.pk  # Check if the User is being created for the first time
        super().save(*args, **kwargs)  # Save the User instance

        if created:  # if new user is created, score tables with 0 points at 0 level will be setup
            Maths_Score.objects.create(user=self)
            Words_Score.objects.create(user=self)
    
   

class Maths_Score(models.Model):
    point = models.IntegerField(default=0, validators=[
                                MinValueValidator(0)], verbose_name="Points")
    level = models.IntegerField(default=0, validators=[
                                MinValueValidator(0)], verbose_name="Level")
    user = models.OneToOneField(ScribbleQuest_User, on_delete=models.CASCADE, primary_key=True, related_name='maths_score')

    def __str__(self):
        return f"{self.user} {self.point} {self.level}"


class Words_Score(models.Model):
    point = models.IntegerField(default=0, validators=[
                                MinValueValidator(0)], verbose_name="Points")
    level = models.IntegerField(default=0, validators=[
                                MinValueValidator(0)], verbose_name="Level")
    user = models.OneToOneField(ScribbleQuest_User, on_delete=models.CASCADE, primary_key=True, related_name='words_score')

    def __str__(self):
        return f"{self.user} {self.point} {self.level}"



# Iterate over user records
# for user in User.objects.all():
#     # Hash the password and update the user record
#     user.password = make_password(user.password)
#     user.save()
