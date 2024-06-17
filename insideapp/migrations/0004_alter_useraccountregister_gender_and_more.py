# Generated by Django 4.1.3 on 2023-02-25 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insideapp', '0003_alter_useraccountregister_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccountregister',
            name='Gender',
            field=models.CharField(choices=[('other', 'other'), ('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=20),
        ),
        migrations.AlterField(
            model_name='useraccountregister',
            name='State',
            field=models.CharField(choices=[('Punjab', 'Punjab'), ('Delhi', 'Delhi'), ('West Benagal', 'West Bengal')], default='Punjab', max_length=20),
        ),
        migrations.AlterField(
            model_name='useraccountregister',
            name='city',
            field=models.CharField(choices=[('Delhi', 'Delhi'), ('Patiala', 'Patiala'), ('kolkota', 'kolkota')], default='patiala', max_length=20),
        ),
        migrations.AlterField(
            model_name='workeraccountregister',
            name='Gender',
            field=models.CharField(choices=[('other', 'other'), ('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=20),
        ),
        migrations.AlterField(
            model_name='workeraccountregister',
            name='State',
            field=models.CharField(choices=[('Punjab', 'Punjab'), ('Delhi', 'Delhi'), ('West Benagal', 'West Bengal')], default='Punjab', max_length=20),
        ),
        migrations.AlterField(
            model_name='workeraccountregister',
            name='city',
            field=models.CharField(choices=[('Delhi', 'Delhi'), ('Patiala', 'Patiala'), ('kolkota', 'kolkota')], default='patiala', max_length=20),
        ),
    ]