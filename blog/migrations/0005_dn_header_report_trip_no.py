# Generated by Django 3.0 on 2020-09-28 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200928_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='dn_header_report',
            name='trip_no',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]