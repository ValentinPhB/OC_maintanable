# Generated by Django 3.0 on 2022-02-17 12:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('oc_lettings_site', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Letting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Letting', to='oc_lettings_site.Address')),
            ],
            options={
                'verbose_name': 'Letting',
                'verbose_name_plural': 'Lettings',
            },
        ),
    ]
