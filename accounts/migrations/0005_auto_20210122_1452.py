# Generated by Django 3.1.5 on 2021-01-22 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210122_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimage',
            name='profilePic',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
