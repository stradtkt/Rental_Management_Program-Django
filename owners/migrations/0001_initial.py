from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=150, unique=True)),
                ('photo', models.ImageField(blank=True, upload_to='photos/owners/%Y/%m/%d/')),
                ('description', models.TextField(default='')),
                ('phone', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('reviews', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='reviews.review')),
            ],
        ),
    ]