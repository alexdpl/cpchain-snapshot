# Generated by Django 2.0.3 on 2018-05-16 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_summarycomment_sales_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='summarycomment',
            name='sales_number',
        ),
    ]
