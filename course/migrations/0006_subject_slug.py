# Generated by Django 5.1.3 on 2024-12-28 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_student_tutor'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
    ]