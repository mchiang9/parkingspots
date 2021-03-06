# Generated by Django 2.0.5 on 2018-05-25 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='spots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identity', models.IntegerField()),
                ('lat', models.DecimalField(decimal_places=2, max_digits=7)),
                ('lon', models.DecimalField(decimal_places=2, max_digits=7)),
                ('reserved', models.BooleanField()),
            ],
        ),
    ]
