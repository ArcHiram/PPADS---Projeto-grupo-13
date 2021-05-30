# Generated by Django 3.2.3 on 2021-05-29 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_auto_20210529_1719'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='sinopse',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='criador',
            new_name='sub_title',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='titulo',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='post',
            name='nota',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
    ]