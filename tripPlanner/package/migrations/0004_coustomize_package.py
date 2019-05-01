# Generated by Django 2.2 on 2019-04-30 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0003_auto_20190430_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coustomize_package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Days', models.IntegerField()),
                ('Budget', models.IntegerField()),
                ('Cities', models.ManyToManyField(to='package.City')),
                ('Keys', models.ManyToManyField(to='package.Key_Features')),
            ],
        ),
    ]
