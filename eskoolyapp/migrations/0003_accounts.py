# Generated by Django 3.0.5 on 2020-07-01 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eskoolyapp', '0002_auto_20200628_0134'),
    ]

    operations = [
        migrations.CreateModel(
            name='ACCOUNTS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_income', models.DateField()),
                ('income_discription', models.CharField(max_length=5000)),
                ('income_amount', models.FloatField()),
                ('date_expense', models.DateField()),
                ('expense_discription', models.CharField(max_length=5000)),
                ('expense_amount', models.FloatField()),
            ],
        ),
    ]