# Generated by Django 3.1.5 on 2021-01-22 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20210122_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimage',
            name='profilePic',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]
