# Generated by Django 3.2.3 on 2021-06-23 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_profile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_pictures', verbose_name='Profile image'),
        ),
    ]