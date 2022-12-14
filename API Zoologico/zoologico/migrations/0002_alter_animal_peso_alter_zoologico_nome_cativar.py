# Generated by Django 4.1.2 on 2022-11-09 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zoologico', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='peso',
            field=models.DecimalField(decimal_places=3, max_digits=6),
        ),
        migrations.AlterField(
            model_name='zoologico',
            name='nome',
            field=models.CharField(max_length=30),
        ),
        migrations.CreateModel(
            name='Cativar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.CharField(choices=[('M', 'matutino'), ('V', 'vespertino'), ('N', 'noturno')], max_length=1)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zoologico.animal')),
                ('zoo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zoologico.zoologico')),
            ],
            options={
                'verbose_name_plural': 'Cativos',
            },
        ),
    ]
