# Generated by Django 3.1.2 on 2020-10-26 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0003_bb_kind'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bb',
            name='kind',
            field=models.CharField(blank=True, choices=[(None, 'Выберите категорию'), ('b', 'Куплю'), ('s', 'Продам'), ('c', 'Обменяю')], max_length=1, verbose_name='Категория'),
        ),
    ]
