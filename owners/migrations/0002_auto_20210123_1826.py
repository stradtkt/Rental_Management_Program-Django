from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
        ('owners', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='reviews',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reviews.review'),
        ),
    ]