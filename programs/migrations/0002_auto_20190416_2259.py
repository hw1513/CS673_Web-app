# Generated by Django 2.1.7 on 2019-04-17 02:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('programs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programs',
            name='project_members',
        ),
        migrations.AddField(
            model_name='programs',
            name='project_members',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
