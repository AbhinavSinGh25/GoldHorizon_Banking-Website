# Generated by Django 4.1b1 on 2023-10-01 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0009_account_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(default='null', max_length=100)),
                ('lastname', models.CharField(default='null', max_length=100)),
            ],
        ),
    ]
