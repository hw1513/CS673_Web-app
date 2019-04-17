

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('programs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=35)),
                ('completed', models.BooleanField(default=False)),
                ('belongs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programs.Programs')),
            ],
        ),
    ]
