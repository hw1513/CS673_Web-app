

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Programs',
            fields=[
                ('project_name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('start_date', models.DateField(verbose_name='date started')),
                ('project_description', models.CharField(max_length=200)),
                ('project_members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
