# Generated by Django 3.0 on 2020-09-26 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200926_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dn',
            name='actual',
        ),
        migrations.RemoveField(
            model_name='dn',
            name='order',
        ),
        migrations.RemoveField(
            model_name='dn',
            name='order_no',
        ),
        migrations.RemoveField(
            model_name='dn',
            name='package_no',
        ),
        migrations.RemoveField(
            model_name='dn',
            name='remark',
        ),
        migrations.RemoveField(
            model_name='dn',
            name='seq',
        ),
        migrations.CreateModel(
            name='dn_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField(verbose_name='No.')),
                ('order_no', models.CharField(max_length=5, verbose_name='Order No.')),
                ('order', models.IntegerField(verbose_name='Order')),
                ('actual', models.IntegerField(verbose_name='Actual')),
                ('remark', models.TextField(max_length=200, verbose_name='Remark')),
                ('package_no', models.ManyToManyField(to='blog.master_package', verbose_name='Package Code')),
            ],
        ),
        migrations.AddField(
            model_name='dn',
            name='dn_list',
            field=models.ManyToManyField(to='blog.dn_list'),
        ),
    ]
