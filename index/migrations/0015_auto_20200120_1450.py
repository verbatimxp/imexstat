# Generated by Django 2.2.5 on 2020-01-20 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0014_contacts_contactsoffice_contactsofficeimage_contactsphone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactsofficeimage',
            name='office',
        ),
        migrations.RemoveField(
            model_name='contactsphone',
            name='contacts',
        ),
        migrations.DeleteModel(
            name='Contacts',
        ),
        migrations.DeleteModel(
            name='ContactsOffice',
        ),
        migrations.DeleteModel(
            name='ContactsOfficeImage',
        ),
        migrations.DeleteModel(
            name='ContactsPhone',
        ),
    ]
