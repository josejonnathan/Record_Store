# Generated by Django 5.0.2 on 2024-02-22 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('genre', models.CharField(default='', max_length=100)),
                ('deezer_id', models.CharField(default='', max_length=50)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('available_units', models.IntegerField(default=0)),
            ],
        ),
    ]
