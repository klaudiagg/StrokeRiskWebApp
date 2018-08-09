from django.db import models
# Create your models here.


class Questions(models.Model):
    sex = models.IntegerField()
    age = models.IntegerField()
    smoker = models.IntegerField()
    SBP = models.IntegerField()
    SBP_treatment = models.IntegerField()
    CVD = models.IntegerField()
    AF = models.IntegerField()
    LVH = models.IntegerField()
    DM = models.IntegerField()
    sleep = models.IntegerField(default=None, null=True)
    add_question2 = models.IntegerField(default=None, null=True)
