# Generated by Django 3.0.6 on 2020-05-06 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('orgid', models.CharField(db_column='id', max_length=60, primary_key=True, serialize=False)),
                ('orgname', models.CharField(db_column='name', max_length=128)),
                ('address', models.CharField(max_length=128)),
                ('country', models.CharField(max_length=128)),
                ('province', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=128)),
                ('zipcode', models.CharField(max_length=128)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('category', models.CharField(max_length=128, null=True)),
                ('rating', models.SmallIntegerField()),
                ('logoimage', models.CharField(max_length=512)),
            ],
        ),
    ]