# Generated by Django 3.0.5 on 2020-06-27 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eskoolyapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='joining_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='mobile_no',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='institutechange',
            name='location',
            field=models.CharField(choices=[('us', 'United States'), ('uk', 'United Kingdom'), ('afg', 'Afghanistan'), ('albania', 'Albania'), ('Algeria', 'Algeria'), ('as', 'American Samoa'), ('Andorra', 'Andorra'), ('Angola', 'Angola'), ('Anguilla', 'Anguilla'), ('Antarctica', 'Antarctica'), ('ab', 'Antigua and Barbuda'), ('Argentina', 'Argentina'), ('Armenia', 'Armenia'), ('Australia', 'Australia'), ('Austria', 'Austria'), ('ind', 'INDIA')], max_length=10),
        ),
    ]
