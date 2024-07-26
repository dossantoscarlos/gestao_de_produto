# Generated by Django 4.1.3 on 2024-07-26 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('formacao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('crm', models.CharField(max_length=11)),
                ('formacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formacao.formacao')),
            ],
        ),
    ]
