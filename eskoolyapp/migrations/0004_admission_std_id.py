# Generated by Django 3.0.5 on 2020-07-14 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eskoolyapp', '0003_employee_emp_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='admission',
            name='std_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
