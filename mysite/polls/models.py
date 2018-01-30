from django.db import models
from django.forms import ModelForm


# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date publsihed')
    def __str__(self):
        return self.question_text



class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Comment(models.Model):
    comment_text = models.TextField(max_length= 500)
    comment_question = models.ForeignKey(Question,default=1,on_delete=models.CASCADE)
    comment_likes = models.IntegerField(default= 0)
    def __str__(self):
        return self.comment_question

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']



