# Generated by Django 3.0 on 2022-02-21 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('lettings', '0002_auto_20220221_1842'),
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='letting',
            name='address',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.CreateModel(
            name='AddressReview',
            fields=[
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('lettings.address',),
        ),
        migrations.CreateModel(
            name='LettingReview',
            fields=[
            ],
            options={
                'verbose_name': 'Letting',
                'verbose_name_plural': 'Lettings',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('lettings.letting',),
        ),
        migrations.CreateModel(
            name='ProfileReview',
            fields=[
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('profiles.profile',),
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Letting',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
