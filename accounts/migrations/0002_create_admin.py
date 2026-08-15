from django.db import migrations


def create_admin_user(apps, schema_editor):
    User = apps.get_model("accounts", "User")

    if not User.objects.filter(username="admin").exists():
        user = User.objects.create(
            username="admin",
            email="admin@gmail.com",
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )

        user.set_password("12341234")
        user.save()


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