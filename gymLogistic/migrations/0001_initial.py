# Generated by Django 4.2.3 on 2023-08-28 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Miembros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCompleto', models.CharField(max_length=200)),
                ('Tierlist', models.CharField(choices=[('visitante', 'visitante'), ('miebro', 'miembro'), ('VIP', 'VIP')], default='', max_length=20)),
                ('Fecha', models.DateField(auto_now_add=True)),
                ('monto', models.IntegerField()),
            ],
        ),
    ]