# Generated by Django 3.1.2 on 2020-10-26 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0002_auto_20201023_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='bb',
            name='kind',
            field=models.CharField(blank=True, choices=[(None, 'Выберите категорию'), ('b', 'Куплю'), ('s', 'Продам'), ('c', 'Обменяю')], max_length=1),
        ),
    ]
