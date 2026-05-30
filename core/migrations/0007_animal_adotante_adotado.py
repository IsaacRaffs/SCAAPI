from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_animal_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='adotado',
            field=models.BooleanField(default=False, verbose_name='adotado'),
        ),
        migrations.AddField(
            model_name='animal',
            name='adotante',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET_NULL, related_name='animais', to='core.adotante', verbose_name='adotante'),
        ),
    ]
