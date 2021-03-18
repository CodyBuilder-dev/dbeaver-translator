# Generated by Django 3.0.7 on 2021-03-18 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translator', '0002_remove_uploadfilemodel_some_field'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='property_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='property',
            old_name='property_en',
            new_name='value_en',
        ),
        migrations.RenameField(
            model_name='property',
            old_name='property_ko',
            new_name='value_ko',
        ),
        migrations.RenameField(
            model_name='property',
            old_name='property_ko_utf',
            new_name='value_ko_utf',
        ),
        migrations.AlterField(
            model_name='uploadfilemodel',
            name='title',
            field=models.CharField(default='org.jkiss.dbeaver', max_length=200),
        ),
    ]
