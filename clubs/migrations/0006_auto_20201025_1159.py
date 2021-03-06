# Generated by Django 3.0.8 on 2020-10-25 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0005_auto_20201025_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bigrecruitment',
            name='urlfield',
            field=models.URLField(blank=True, default='', editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='clubaccount',
            name='imgurl',
            field=models.URLField(blank=True, default='', editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='clubbigevent',
            name='urlfield',
            field=models.URLField(blank=True, default='', editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='clubevent',
            name='imgurl',
            field=models.URLField(blank=True, default='', editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='recruitment',
            name='urlfield',
            field=models.URLField(blank=True, default='', editable=False, null=True),
        ),
    ]
