# Generated by Django 2.1.7 on 2019-05-11 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20190510_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='native_language',
            field=models.ForeignKey(help_text='Selecciona el lenguage nativo de escritura del autor', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Language'),
        ),
    ]
