from django.db import models
# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    Question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text


class Results(models.Model):
    ans1 = models.CharField(max_length=200)
    ans2 = models.CharField(max_length=200)
    ans3 = models.CharField(max_length=200)
    ans4 = models.CharField(max_length=200)
    ans5 = models.CharField(max_length=200)


class Questions(models.Model):
    sex = models.CharField(max_length=500)
    age = models.CharField(max_length=5)
    smoker = models.IntegerField(max_length=5)
    SBP = models.CharField(max_length=5)
    SBP_treatment = models.IntegerField(max_length=5)
    CVD = models.IntegerField(max_length=5)
    AF = models.IntegerField(max_length=5)
    LVH = models.IntegerField(max_length=5)
    DM = models.IntegerField(max_length=5)
