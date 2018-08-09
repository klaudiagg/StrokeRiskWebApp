from django.db import models
# Create your models here.


class Questions(models.Model):
    sex = models.IntegerField(db_column='sex')
    age = models.IntegerField(db_column='age')
    smoker = models.IntegerField(db_column='smoker')
    SBP = models.IntegerField(db_column='SBP')
    SBP_treatment = models.IntegerField(db_column='SBP_tr')
    CVD = models.IntegerField(db_column='CVD')
    AF = models.IntegerField(db_column='AF')
    LVH = models.IntegerField(db_column='LVH')
    DM = models.IntegerField(db_column='DM')
    sleep = models.IntegerField(db_column='sleep')
    add_question2 = models.IntegerField(db_column='question')
