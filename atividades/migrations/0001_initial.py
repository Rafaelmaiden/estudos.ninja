# Generated by Django 2.0.6 on 2018-06-19 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=500)),
                ('nome_usuario', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=256)),
                ('senha', models.CharField(max_length=16)),
            ],
        ),
    ]
