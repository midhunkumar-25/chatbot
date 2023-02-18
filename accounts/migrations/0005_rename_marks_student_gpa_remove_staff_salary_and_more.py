# Generated by Django 4.1.6 on 2023-02-11 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_staff_account'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='marks',
            new_name='gpa',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='salary',
        ),
        migrations.AddField(
            model_name='student',
            name='department',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
