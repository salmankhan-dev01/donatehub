from django.db import migrations
from django.contrib.auth.hashers import make_password


def create_admin_user(apps, schema_editor):
    User = apps.get_model("accounts", "User")

    if not User.objects.filter(username="admin").exists():
        User.objects.create(
            username="admin",
            email="admin@gmail.com",
            password=make_password("12341234"),
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )


def remove_admin_user(apps, schema_editor):
    User = apps.get_model("accounts", "User")
    User.objects.filter(username="admin").delete()


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(
            create_admin_user,
            remove_admin_user,
        ),
    ]