# Generated by Django 2.2.6 on 2019-12-04 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12)),
                ('work', models.CharField(max_length=15)),
                ('experience', models.IntegerField()),
                ('total_salery', models.DecimalField(decimal_places=2, max_digits=10)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]