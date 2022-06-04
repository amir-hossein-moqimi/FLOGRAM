# Generated by Django 4.0 on 2022-05-28 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_profile_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='verification_code',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Instagram',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=50, null=True),
        ),
    ]