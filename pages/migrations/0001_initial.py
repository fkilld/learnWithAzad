# Generated by Django 3.0.10 on 2020-10-01 18:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(blank=True, max_length=200, null=True)),
                ('last', models.CharField(blank=True, max_length=200, null=True)),
                ('photo', models.ImageField(blank=True, default='user.png', null=True, upload_to='photos/%Y/%m')),
                ('speaks', models.CharField(blank=True, max_length=200, null=True)),
                ('is_learning', models.CharField(blank=True, max_length=200, null=True)),
                ('friends', models.ManyToManyField(blank=True, related_name='_profile_friends_+', to='pages.Profile')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
