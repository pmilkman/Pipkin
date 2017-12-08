from django.contrib import admin

# Register your models here.
from .models import Person, Address, AddressForm, Contact, ContactForm


class AddressInline(admin.TabularInline):
    model = Address
    form = AddressForm
    extra = 1


class ContactInline(admin.TabularInline):
    model = Contact
    form = ContactForm
    extra = 1


class PersonAdmin(admin.ModelAdmin):
    list_display = ('person_display', 'email', 'birthday')
    readonly_fields = ['created','modified']
    techFields = [('created', 'modified'), 'token']
    stammFields = [('firstname', 'name', 'akdmTitle'),
                   ('sex', 'birthday', 'sv'),
                   ('telefon', 'email'), ]
    inlines = [AddressInline, ContactInline]

    fieldsets = (
        # Stamm-Sektion
        (None, {'fields': stammFields}),
        # Technische Sektion
        ('Technisches', {'fields': techFields}),
    )


admin.site.register(Person, PersonAdmin)

# admin.site.register(Person)
