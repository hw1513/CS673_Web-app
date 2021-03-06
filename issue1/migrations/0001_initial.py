# Generated by Django 2.1.7 on 2019-04-17 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('programs', '0003_auto_20190416_2312'),
    ]

    operations = [
        migrations.CreateModel(
            name='iList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=35)),
                ('completed', models.BooleanField(default=False)),
                ('issuebelongs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programs.Programs')),
            ],
        ),
    ]
