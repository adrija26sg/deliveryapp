# Generated by Django 4.1.3 on 2023-02-25 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insideapp', '0012_alter_useraccountregister_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccountregister',
            name='Gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('other', 'other')], default='Male', max_length=20),
        ),
        migrations.AlterField(
            model_name='useraccountregister',
            name='State',
            field=models.CharField(choices=[('Delhi', 'Delhi'), ('West Benagal', 'West Bengal'), ('Punjab', 'Punjab')], default='Punjab', max_length=20),
        ),
        migrations.AlterField(
            model_name='workeraccountregister',
            name='Gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('other', 'other')], default='Male', max_length=20),
        ),
        migrations.AlterField(
            model_name='workeraccountregister',
            name='State',
            field=models.CharField(choices=[('Delhi', 'Delhi'), ('West Benagal', 'West Bengal'), ('Punjab', 'Punjab')], default='Punjab', max_length=20),
        ),
    ]
