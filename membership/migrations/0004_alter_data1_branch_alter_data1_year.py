# Generated by Django 4.0.4 on 2022-09-30 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0003_alter_data1_branch_alter_data1_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data1',
            name='branch',
            field=models.CharField(choices=[('1', 'CSE'), ('2', 'EC'), ('3', 'EE'), ('4', 'ME'), ('5', 'CE')], default='---', max_length=100),
        ),
        migrations.AlterField(
            model_name='data1',
            name='year',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='---', max_length=100),
        ),
    ]
