# Generated by Django 4.2.3 on 2023-07-28 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_alter_profile_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationship',
            name='status',
            field=models.CharField(choices=[('send', 'send'), ('accepted', 'accepted')], max_length=8),
        ),
    ]