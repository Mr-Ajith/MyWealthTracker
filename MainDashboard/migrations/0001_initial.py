# Generated by Django 4.1 on 2022-08-21 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainDashboard',
            fields=[
                ('userId', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('savings', models.FloatField(blank=True, null=True)),
                ('fixedDeposit', models.FloatField(blank=True, null=True)),
                ('mutualFund', models.FloatField(blank=True, null=True)),
                ('stock', models.FloatField(blank=True, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]