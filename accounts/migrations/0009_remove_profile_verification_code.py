# Generated by Django 4.0 on 2022-05-28 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_profile_verification_code_alter_profile_instagram_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='verification_code',
        ),
    ]
