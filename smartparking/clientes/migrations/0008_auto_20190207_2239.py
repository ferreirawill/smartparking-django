# Generated by Django 2.1.5 on 2019-02-07 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0007_auto_20190207_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tel',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.Cliente'),
        ),
    ]
