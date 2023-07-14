# Generated by Django 4.2.3 on 2023-07-13 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jugadores',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('posicion', models.CharField(max_length=2)),
                ('fecha_deb', models.DateField()),
                ('fecha_ret', models.DateField()),
            ],
            options={
                'db_table': 'jugadores',
            },
        ),
    ]