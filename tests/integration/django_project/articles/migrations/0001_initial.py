from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("slug", models.SlugField(unique=True)),
                ("summary", models.TextField()),
                ("author", models.CharField(max_length=100)),
                ("published", models.DateTimeField()),
                ("draft", models.BooleanField(default=False)),
            ],
        ),
    ]
