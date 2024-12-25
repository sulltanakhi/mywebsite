# Generated by Django 5.1.3 on 2024-12-25 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20)),
                ('phone', models.CharField(blank=True, max_length=50)),
                ('subject', models.CharField(blank=True, max_length=50)),
                ('message', models.TextField(blank=True, max_length=255)),
                ('status', models.CharField(choices=[('New', 'New'), ('Read', 'Read'), ('Closed', 'Closed')], default='New', max_length=10)),
                ('ip', models.CharField(blank=True, max_length=20)),
                ('note', models.CharField(blank=True, max_length=100)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('keywords', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=500)),
                ('phone', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('smtp_server', models.CharField(blank=True, max_length=50)),
                ('smtp_email', models.CharField(blank=True, max_length=50)),
                ('smtp_password', models.CharField(blank=True, max_length=10)),
                ('smtp_port', models.CharField(blank=True, max_length=5)),
                ('youtube', models.URLField(blank=True, max_length=50)),
                ('instagram', models.URLField(blank=True, max_length=50)),
                ('facebook', models.URLField(blank=True, max_length=50)),
                ('icon', models.ImageField(blank=True, upload_to='images/')),
                ('aboutus', models.TextField(max_length=500)),
                ('contact', models.TextField(max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='subject',
            name='course',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]