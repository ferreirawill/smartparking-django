# Generated by Django 2.1.5 on 2019-02-11 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0011_auto_20190211_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='image',
            field=models.ImageField(upload_to='clientes_fotos'),
        ),
        migrations.AlterField(
            model_name='tel',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.Cliente'),
        ),
    ]
