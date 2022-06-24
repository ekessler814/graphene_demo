# Generated by Django 4.0.5 on 2022-06-24 09:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calculation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inputs', models.CharField(max_length=200)),
                ('result', models.CharField(max_length=50, null=True)),
                ('datetime_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='CalculatorMemory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('session_name', models.CharField(default='default', max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
        migrations.AddField(
            model_name='calculation',
            name='calculator_memory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calc.calculatormemory'),
        ),
    ]