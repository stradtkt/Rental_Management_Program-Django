# Generated by Django 3.1.5 on 2021-03-31 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Renter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=150, unique=True)),
                ('description', models.TextField(default='')),
                ('kids', models.IntegerField(default=0)),
                ('martial_status', models.CharField(default='', max_length=100)),
                ('income', models.CharField(default='', max_length=100)),
                ('picture', models.ImageField(blank=True, upload_to='photos/renters/%Y/%m/%d/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
