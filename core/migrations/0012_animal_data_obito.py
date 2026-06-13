# Generated migration for adding data_obito field

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_animal_raca_pelagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='data_obito',
            field=models.DateField(blank=True, null=True, verbose_name='data de óbito'),
        ),
    ]
