# Generated by Django 4.0.6 on 2022-08-03 11:55

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('edu', '0001_initial'), ('edu', '0002_alter_course_course_number_alter_course_group_number'), ('edu', '0003_alter_course_second_day'), ('edu', '0004_alter_course_first_day_alter_course_second_day'), ('edu', '0005_alter_course_course_number_alter_course_group_number'), ('edu', '0006_alter_course_first_day_alter_course_second_day'), ('edu', '0007_alter_course_first_day_alter_course_second_day'), ('edu', '0008_alter_course_course_number_alter_course_department_and_more'), ('edu', '0009_alter_course_first_day_alter_course_second_day'), ('edu', '0010_account'), ('edu', '0011_alter_account_bio_alter_account_gender'), ('edu', '0012_alter_account_bio_alter_account_gender'), ('edu', '0013_alter_account_gender')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(limit_value=1, message='1')])),
                ('name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(limit_value=1, message='2')])),
                ('course_number', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(limit_value=1, message='3')])),
                ('group_number', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(limit_value=1, message='4')])),
                ('teacher', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(limit_value=1, message='5')])),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('first_day', models.CharField(choices=[('0', 'saturday'), ('1', 'sunday'), ('2', 'monday'), ('3', 'tuesday'), ('4', 'wednesday')], default=0, max_length=2)),
                ('second_day', models.CharField(choices=[('0', 'saturday'), ('1', 'sunday'), ('2', 'monday'), ('3', 'tuesday'), ('4', 'wednesday'), ('7', '-')], default=0, max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, default='', max_length=250)),
                ('gender', models.CharField(choices=[('undefined', 'undefined'), ('male', 'male'), ('female', 'female')], default='undefined', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]