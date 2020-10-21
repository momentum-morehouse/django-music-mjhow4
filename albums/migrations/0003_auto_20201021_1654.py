# Generated by Django 3.1.2 on 2020-10-21 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0002_album_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('biography', models.CharField(max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='albums.artist'),
        ),
    ]
