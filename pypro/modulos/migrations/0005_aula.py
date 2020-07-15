# Generated by Django 3.0.8 on 2020-07-15 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0004_slug_unico_e_nao_nulo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('titulo', models.CharField(max_length=64)),
                ('slug', models.SlugField(unique=True)),
                ('modulo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='modulos.Modulo')),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
    ]
