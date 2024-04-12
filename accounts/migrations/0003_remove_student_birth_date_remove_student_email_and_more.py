# Generated by Django 5.0.3 on 2024-04-12 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_create_initial_subjects'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
        migrations.RemoveField(
            model_name='student',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='student',
            name='second_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='third_name',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='email',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='second_name',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='third_name',
        ),
        migrations.AddField(
            model_name='user',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='second_name',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='third_name',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
