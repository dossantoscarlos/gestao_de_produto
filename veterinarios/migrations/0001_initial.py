# Generated by Django 4.1.3 on 2024-07-26 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Veterinario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sobrenome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11, null=True)),
                ('rg', models.CharField(max_length=8, null=True)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], default='M', max_length=1)),
                ('email', models.EmailField(max_length=100)),
                ('tel_contato', models.CharField(max_length=20)),
                ('cns', models.CharField(max_length=100)),
                ('data_nascimento', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField()),
            ],
        ),
    ]