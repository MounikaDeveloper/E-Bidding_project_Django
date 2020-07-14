# Generated by Django 2.2.3 on 2019-12-18 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_productmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel1',
            fields=[
                ('pno', models.IntegerField(primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=30)),
                ('bidprice', models.FloatField()),
                ('information', models.TextField()),
                ('image', models.ImageField(upload_to='productmodel')),
                ('status', models.CharField(max_length=30)),
                ('sellerinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.RegisterModel')),
            ],
        ),
        migrations.DeleteModel(
            name='ProductModel',
        ),
    ]