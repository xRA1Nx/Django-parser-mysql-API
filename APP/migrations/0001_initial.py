# Generated by Django 4.1 on 2022-08-25 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('text', models.TextField(max_length=10000)),
                ('date', models.DateField(auto_now=True)),
                ('source', models.CharField(choices=[('oz', 'ozon'), ('ya', 'yandex')], max_length=2)),
                ('tags', models.ManyToManyField(through='APP.NewsTags', to='APP.tag')),
            ],
        ),
        migrations.AddField(
            model_name='newstags',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP.post'),
        ),
        migrations.AddField(
            model_name='newstags',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP.tag'),
        ),
    ]
