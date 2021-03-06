# Generated by Django 2.1.7 on 2019-02-20 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsanImza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asan_imza', models.IntegerField(unique=True, verbose_name='Asan imza')),
                ('asan_nomre', models.CharField(max_length=20, unique=True, verbose_name='Asan nomre')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies_app.Company', verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyContacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contacnt_type', models.IntegerField(choices=[(1, 'Telefon'), (2, 'email'), (3, 'address')])),
                ('comtact', models.CharField(max_length=255, verbose_name='elaqe')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies_app.Company')),
            ],
        ),
    ]
