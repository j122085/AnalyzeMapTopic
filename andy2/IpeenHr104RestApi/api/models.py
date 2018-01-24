# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# from django.db import models
#
#
# class Hr104(models.Model):
#     id = models.TextField(unique=True, primary_key=True)
#     appear_data = models.TextField(blank=True, null=True)
#     job = models.TextField(blank=True, null=True)
#     job_descript = models.TextField(blank=True, null=True)
#     lat = models.FloatField(blank=True, null=True)  # This field type is a guess.
#     lng = models.FloatField(blank=True, null=True)  # This field type is a guess.
#     name = models.TextField(blank=True, null=True)
#     salary_high = models.IntegerField(blank=True, null=True)
#     salary_low = models.IntegerField(blank=True, null=True)
#     address = models.TextField(blank=True, null=True)
#     big_add = models.TextField(blank=True, null=True)
#     small_add = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'hr104'
#
#
# class Ipeen(models.Model):
#     id = models.TextField(unique=True,primary_key=True)
#     name = models.TextField()
#     address = models.TextField(blank=True, null=True)
#     tele = models.TextField(blank=True, null=True)
#     averagecost = models.TextField(blank=True, null=True)
#     viewcount = models.IntegerField(blank=True, null=True)
#     ncomment = models.IntegerField(db_column='Ncomment', blank=True, null=True)  # Field name made lowercase.
#     bigstyle = models.TextField(blank=True, null=True)
#     smallstyle = models.TextField(blank=True, null=True)
#     bigadd = models.TextField(blank=True, null=True)
#     smalladd = models.TextField(blank=True, null=True)
#     # lat = models.TextField(blank=True, null=True)  # This field type is a guess.
#     # lng = models.TextField(blank=True, null=True)  # This field type is a guess.
#     lat = models.FloatField(blank=True, null=True)  # This field type is a guess.
#     lng = models.FloatField(blank=True, null=True)  # This field type is a guess.
#     class Meta:
#         managed = False
#         db_table = 'ipeen'
