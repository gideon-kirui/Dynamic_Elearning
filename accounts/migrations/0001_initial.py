# Generated by Django 5.0 on 2023-12-15 14:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='L_register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='users/%y/%m/%d')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='lecturerassigned', to='base.course')),
                ('lecturer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base.school')),
                ('unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base.unit')),
                ('year', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base.year')),
            ],
        ),
        migrations.CreateModel(
            name='S_register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='users/%y/%m/%d')),
                ('registration_number', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='studentincourse', to='base.course')),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base.school')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base.unit')),
                ('year', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base.year')),
            ],
        ),
    ]
