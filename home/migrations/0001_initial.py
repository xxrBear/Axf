# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-05-08 04:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AxfMainShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=32)),
                ('trackid', models.IntegerField()),
                ('categoryid', models.IntegerField()),
                ('brandname', models.CharField(max_length=32)),
                ('img1', models.CharField(max_length=256)),
                ('childcid1', models.IntegerField()),
                ('productid1', models.IntegerField()),
                ('longname1', models.CharField(max_length=256)),
                ('price1', models.IntegerField()),
                ('marketprice1', models.IntegerField()),
                ('img2', models.CharField(max_length=256)),
                ('childcid2', models.IntegerField()),
                ('productid2', models.IntegerField()),
                ('longname2', models.CharField(max_length=128)),
                ('price2', models.IntegerField()),
                ('marketprice2', models.IntegerField()),
                ('img3', models.CharField(max_length=256)),
                ('childcid3', models.IntegerField()),
                ('productid3', models.IntegerField()),
                ('longname3', models.CharField(max_length=256)),
                ('price3', models.IntegerField()),
                ('marketprice3', models.IntegerField()),
            ],
            options={
                'db_table': 'axf_mainshow',
            },
        ),
        migrations.CreateModel(
            name='AxfMustBuy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=32)),
                ('trackid', models.IntegerField()),
            ],
            options={
                'db_table': 'axf_mustbuy',
            },
        ),
        migrations.CreateModel(
            name='AxfNav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=32)),
                ('trackid', models.IntegerField()),
            ],
            options={
                'db_table': 'axf_nav',
            },
        ),
        migrations.CreateModel(
            name='AxfWheel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=32)),
                ('trackid', models.IntegerField()),
            ],
            options={
                'db_table': 'axf_wheel',
            },
        ),
    ]
