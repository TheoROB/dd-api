# Generated by Django 4.1.5 on 2023-01-06 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pseudo', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('popularity', models.PositiveBigIntegerField()),
                ('attack', models.PositiveBigIntegerField()),
                ('defense', models.PositiveBigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pseudo', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player1', to='ddev.player')),
                ('player2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player2', to='ddev.player')),
                ('winner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ddev.player')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ddev.user'),
        ),
    ]