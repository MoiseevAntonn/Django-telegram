from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User


# Create your models here.

class My_user_form(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class Link_with_email(models.Model):
    email = models.EmailField(max_length=250)
    chat_id = models.IntegerField()
    get_notice = models.BooleanField(default=True)

	
