# Generated by Django 5.1.3 on 2024-12-04 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoginRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=100, verbose_name='Email or Phone')),
                ('password', models.CharField(max_length=100, verbose_name='Password')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]