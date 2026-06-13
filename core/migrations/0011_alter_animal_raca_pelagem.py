# Generated migration for removing choices from raca and pelagem fields

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_animal_fotos_att'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='raca',
            field=models.CharField(blank=True, max_length=120, verbose_name='raça'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='pelagem',
            field=models.CharField(blank=True, max_length=80, verbose_name='pelagem'),
        ),
    ]
