# Generated by Django 3.1.1 on 2020-09-29 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sabor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_do_sabor', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sorvete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidade', models.PositiveIntegerField(verbose_name='Unidades')),
                ('preco_de_venda', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Preço de Venda')),
                ('preco_de_custo', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Preço de Custo')),
                ('sabores', models.ManyToManyField(to='core.Sabor')),
            ],
        ),
    ]
