# Generated by Django 4.1.3 on 2024-08-06 03:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TipoProduto',
            new_name='CategoriaProduto',
        ),
        migrations.AlterModelOptions(
            name='categoriaproduto',
            options={'verbose_name': 'Categoria de produto', 'verbose_name_plural': 'Categorias de produto'},
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='tipo',
            new_name='categoria',
        ),
    ]
