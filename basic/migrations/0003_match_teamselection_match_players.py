# Generated by Django 4.2.2 on 2023-06-24 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0002_player_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_date', models.DateField()),
                ('match_type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TeamSelection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starting', models.BooleanField()),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic.match')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic.player')),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='players',
            field=models.ManyToManyField(through='basic.TeamSelection', to='basic.player'),
        ),
    ]
