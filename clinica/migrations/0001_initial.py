# Generated by Django 4.1.3 on 2024-07-27 00:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('sobrenome', models.CharField(max_length=100)),
                ('data_nascimento', models.DateField()),
                ('cpf', models.CharField(max_length=11, null=True)),
                ('rg', models.CharField(max_length=8, null=True)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], default='M', max_length=1)),
                ('email', models.EmailField(max_length=100)),
                ('tel_contato', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Veterinario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('crm', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('sexo', models.CharField(choices=[('M', 'Macho'), ('F', 'Femea')], default='M', max_length=1)),
                ('data_nascimento', models.DateField()),
                ('porte', models.CharField(choices=[('M', 'Medio'), ('G', 'Grande'), ('P', 'Pequeno')], default='M', max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinica.tutor')),
            ],
        ),
    ]