# Generated by Django 5.0.2 on 2024-03-04 09:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0002_rename_books_book_reg"),
    ]

    operations = [
        migrations.CreateModel(
            name="Issued_Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("bookTitle", models.CharField(max_length=100)),
                ("studentId", models.CharField(max_length=100)),
                ("studentName", models.CharField(max_length=100)),
                ("bookCondition", models.CharField(max_length=100)),
                ("issuedBy", models.CharField(max_length=100)),
                ("issueDate", models.DateField()),
                ("returnDate", models.DateField()),
                (
                    "bookId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="base.book_reg"
                    ),
                ),
            ],
        ),
    ]