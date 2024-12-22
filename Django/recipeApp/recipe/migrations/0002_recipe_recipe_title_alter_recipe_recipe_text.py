# Generated by Django 4.2.6 on 2023-10-22 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_title',
            field=models.CharField(default='Title', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipe_text',
            field=models.CharField(max_length=1000),
        ),
    ]