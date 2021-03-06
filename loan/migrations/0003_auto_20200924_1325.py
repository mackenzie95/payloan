# Generated by Django 3.1.1 on 2020-09-24 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0002_userprofile_bank'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='app_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='loan_amount',
            field=models.CharField(choices=[('10,000', 'N10,000'), ('20,000', 'N20,000'), ('30,000', 'N30,000'), ('40,000', 'N40,000'), ('50,000', 'N50,000'), ('60,000', 'N60,000'), ('70,000', 'N70,000'), ('80,000', 'N80,000'), ('90,000', 'N90,000'), ('100,000', 'N100,000'), ('200,000', 'N200,000'), ('300,000', 'N300,000'), ('400,000', 'N400,000'), ('500,000', 'N500,000'), ('600,000', 'N600,000'), ('700,000', 'N700,000'), ('800,000', 'N800,000'), ('900,000', 'N900,000'), ('1,000,000', 'N1,000,000')], max_length=12),
        ),
    ]
