# Generated by Django 4.0.5 on 2022-07-15 17:19

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0015_rename_percenttprotein_food_percentprotein'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='text1',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
