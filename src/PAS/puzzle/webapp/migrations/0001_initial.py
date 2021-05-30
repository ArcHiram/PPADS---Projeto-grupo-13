# Generated by Django 3.2.3 on 2021-05-28 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('sub_title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('categories', models.CharField(choices=[('TC', 'Tecnologia'), ('CR', 'Curiosidades'), ('GR', 'Geral')], default='GR', max_length=2)),
                ('deleted', models.BooleanField(default=True)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='posts')),
            ],
        ),
    ]
