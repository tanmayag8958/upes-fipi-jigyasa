# Generated by Django 2.1.7 on 2019-03-09 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_auto_20190310_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paytm_history',
            name='TXNID',
            field=models.IntegerField(max_length=50, verbose_name='TXN ID'),
        ),
    ]
