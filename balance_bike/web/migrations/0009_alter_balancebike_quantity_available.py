# Generated by Django 4.1.3 on 2022-11-21 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_balancebike_quantity_available_checkoutdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balancebike',
            name='quantity_available',
            field=models.IntegerField(default=1),
        ),
    ]