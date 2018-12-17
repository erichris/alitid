# Generated by Django 2.0.7 on 2018-12-04 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlanEscape',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID1', models.CharField(max_length=20)),
                ('ID2', models.CharField(max_length=20)),
                ('created', models.DateTimeField(verbose_name='date published')),
                ('used', models.BooleanField(default=False)),
                ('ID_Movil1', models.CharField(default='null', max_length=50)),
                ('ID_Movil2', models.CharField(default='null', max_length=50)),
                ('ID_Movil3', models.CharField(default='null', max_length=50)),
            ],
        ),
    ]