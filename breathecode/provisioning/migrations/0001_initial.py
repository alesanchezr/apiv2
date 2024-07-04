# Generated by Django 3.2.16 on 2023-03-28 00:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("authenticate", "0031_userinvite_syllabus"),
        ("admissions", "0054_cohortuser_history_log"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProvisioningVendor",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=200)),
                ("api_url", models.URLField(blank=True)),
                (
                    "workspaces_url",
                    models.URLField(help_text="Points to the place were you can see all your containers"),
                ),
                (
                    "invite_url",
                    models.URLField(
                        help_text="Some vendors (like Gitpod) allow to share invite link to automatically join"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="ProvisioningProfile",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("academy", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="admissions.academy")),
                (
                    "cohorts",
                    models.ManyToManyField(
                        blank=True,
                        help_text="If set, only these cohorts will be provisioned with this vendor in this academy",
                        to="admissions.Cohort",
                    ),
                ),
                (
                    "members",
                    models.ManyToManyField(
                        blank=True,
                        help_text="If set, only these members will be provisioned with this vendor in this academy",
                        to="authenticate.ProfileAcademy",
                    ),
                ),
                (
                    "vendor",
                    models.ForeignKey(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="provisioning.provisioningvendor",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProvisioningMachineTypes",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=200)),
                ("slug", models.SlugField(max_length=80)),
                ("description", models.CharField(max_length=255)),
                ("cpu_cores", models.IntegerField()),
                ("ram_in_bytes", models.IntegerField()),
                ("disk_in_bytes", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "vendor",
                    models.ForeignKey(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="provisioning.provisioningvendor",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProvisioningContainer",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("web_url", models.URLField()),
                (
                    "status",
                    models.CharField(help_text="We have no control over this. Reported by the vendor", max_length=50),
                ),
                ("display_name", models.CharField(max_length=50)),
                ("last_used_at", models.DateTimeField(blank=True, default=None, null=True)),
                ("provisioned_at", models.DateTimeField(blank=True, default=None, null=True)),
                ("has_unpushed_changes", models.BooleanField(default=False)),
                ("has_uncommitted_changes", models.BooleanField(default=False)),
                ("branch_name", models.CharField(blank=True, default=None, max_length=100, null=True)),
                (
                    "task_associated_slug",
                    models.SlugField(
                        help_text="What assignment was the the student trying to complete with this", max_length=100
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name="ProvisioningBill",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("total_amount", models.FloatField()),
                ("currency_code", models.CharField(default="usd", max_length=3)),
                (
                    "status",
                    models.CharField(
                        choices=[("DUE", "Due"), ("DISPUTED", "Disputed"), ("IGNORED", "Ignored"), ("PAID", "Paid")],
                        default="DUE",
                        max_length=20,
                    ),
                ),
                ("paid_at", models.DateTimeField(blank=True, default=None, null=True)),
                ("status_details", models.TextField(blank=True, default=None, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("academy", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="admissions.academy")),
            ],
        ),
        migrations.CreateModel(
            name="ProvisioningActivity",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "username",
                    models.CharField(
                        help_text="Native username in the provisioning platform, E.g: github username", max_length=80
                    ),
                ),
                (
                    "registered_at",
                    models.DateTimeField(
                        blank=True,
                        default=None,
                        help_text="When the activitiy happened, this field comes form the provisioning vendor",
                        null=True,
                    ),
                ),
                ("product_name", models.CharField(max_length=100)),
                ("sku", models.CharField(max_length=100)),
                ("quantity", models.FloatField()),
                ("unit_type", models.CharField(max_length=100)),
                ("price_per_unit", models.FloatField(help_text="Price paid to the provisioning vendor, E.g: Github")),
                ("currency_code", models.CharField(max_length=3)),
                (
                    "multiplier",
                    models.FloatField(blank=True, help_text="To increase price in a certain percentage", null=True),
                ),
                ("repository_url", models.URLField()),
                (
                    "task_associated_slug",
                    models.SlugField(
                        help_text="What assignment was the the student trying to complete with this", max_length=100
                    ),
                ),
                ("notes", models.TextField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("PENDING", "Pending"), ("PERSISTED", "Persisted"), ("ERROR", "Error")],
                        default="PENDING",
                        max_length=20,
                    ),
                ),
                ("status_text", models.CharField(max_length=255)),
                ("processed_at", models.DateTimeField(blank=True, default=None, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "bill",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="provisioning.provisioningbill",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProvisioningAcademy",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("credentials_key", models.CharField(blank=True, max_length=200)),
                ("credentials_token", models.CharField(blank=True, max_length=200)),
                (
                    "container_idle_timeout",
                    models.IntegerField(
                        default=15, help_text="If the container is idle for X amount of minutes, it will be shut down"
                    ),
                ),
                (
                    "max_active_containers",
                    models.IntegerField(
                        default=2,
                        help_text="If you already have X active containers you wont be able to create new ones. ",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("academy", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="admissions.academy")),
                (
                    "allowed_machine_types",
                    models.ManyToManyField(blank=True, to="provisioning.ProvisioningMachineTypes"),
                ),
                (
                    "vendor",
                    models.ForeignKey(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="provisioning.provisioningvendor",
                    ),
                ),
            ],
        ),
    ]
