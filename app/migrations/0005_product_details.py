# Generated by Django 3.2.9 on 2021-12-28 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='PRODUCT_DETAILS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('extra', models.CharField(choices=[('A', 'EXTRA A'), ('B', 'EXTRA B'), ('C', 'EXTRA C')], max_length=3)),
            ],
        ),
    ]