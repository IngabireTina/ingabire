# Generated by Django 3.0.8 on 2020-07-30 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('serialNumber', models.CharField(max_length=200, null=True, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('code', models.CharField(max_length=200, null=True)),
                ('category', models.CharField(choices=[('Computer Laptop', 'Computer Laptop'), ('Computer Desktop', 'Computer Desktop'), ('4G Router', '4G Router'), ('Printer', 'Printer'), ('Scanner', 'Scanner'), ('Television', 'Television'), ('Decoder', 'Decoder')], max_length=200, null=True)),
                ('quantity', models.IntegerField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Work', 'Work'), ('Not Work', 'Not Work'), ('Submitted', 'Submitted')], default='work', max_length=200, null=True)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('person', models.CharField(max_length=200, null=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('device', models.ForeignKey(max_length=200, null=True, on_delete=django.db.models.deletion.SET_NULL, to='registerItem.Stock')),
            ],
        ),
    ]
