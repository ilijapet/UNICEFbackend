# Generated by Django 4.2.9 on 2024-01-13 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0007_remove_userprofile_nft_metadata"),
        ("dashboard", "0002_rename_price_orderhistory_amount_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="NftMetadata",
        ),
    ]