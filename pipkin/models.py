from django.db import models
import datetime
from django import forms
from django.core.urlresolvers import reverse
# Create your models here.


class Person(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    INTER = 'X'

    SEX_CHOICES = (
                  (MALE, 'männlich'),
                  (FEMALE, 'weiblich'),
                  (INTER, 'inter'),
    )

    firstname = models.CharField('Vorname', blank=False, max_length=100)
    name = models.CharField('Nachname', blank=False, max_length=100)
    aliasName = models.CharField(
        'Alias-Name', blank=True, max_length=100)
    akdmTitle = models.CharField('Akadem. Titel', blank=True, max_length=50)
    sex = models.CharField('Geschlecht', max_length=1,
                           choices=SEX_CHOICES, default=INTER)
    birthday = models.DateField(
        'Geburtsdatum', default=datetime.date(1900, 1, 1))

    email = models.EmailField('Email', max_length=50, blank=True)
    telefon = models.CharField('Telefon', max_length=15, blank=True)

    sv = models.IntegerField('SV#', blank=True)

    # Technische Felder
    token = models.CharField(blank=True, max_length=6)

    created = models.DateTimeField(
        'Angelegt am', blank=False, auto_now_add=True)
    modified = models.DateTimeField('Geändert am', blank=False, auto_now=True)

    def __str__(self):
        output = self.firstname

        if(bool(self.aliasName)):
            output += ' "' + self.aliasName + '" '
        else:
            output += ' '

        output += self.name

        return output

    def person_display(self):
        return self

    person_display.short_description = 'Person'

    def get_absolute_url(self):
        return reverse('pipkin:person', args=[str(self.id)])


class Address(models.Model):
    MAIN = 'M'
    SIDE = 'S'

    TYPES_CHOICES = ((MAIN, 'Hauptadresse'), (SIDE, 'Nebenadresse'), )

    addressLine = models.CharField('Adresse', max_length=100, blank=False)
    addressType = models.CharField(
        'Type', max_length=1, choices=TYPES_CHOICES, default=MAIN)
    zipCode = models.CharField('PLZ', max_length=6, blank=False)
    city = models.CharField('Ort', max_length=30, blank=False)
    country = models.CharField('Land', max_length=50, blank=True)

    person = models.ForeignKey(Person)

    def __str__(self):
        return self.addressLine + ' , ' + self.zipCode + ' , ' + self.city


class Contact(models.Model):
    MAIN = 'M'
    SIDE = 'S'
    EMERCENCY = 'E'

    MAIL = 'M'
    PHONE = 'P'

    SEVERITY_CHOICES = ((MAIN, 'Hauptkontakt'),
                        (SIDE, 'Nebenkontakt'), (EMERCENCY, 'Notfallskontakt'))
    TYPE_CHOICES = ((MAIL, 'Email'), (PHONE, 'Telefon'))

    contactSeverity = models.CharField(
        'Dringlichkeit', max_length=1, choices=SEVERITY_CHOICES, default=MAIN, help_text='Zeigt die Relevanz des Kontakts'
        )
    contactType = models.CharField(
        'Type', max_length=1, choices=TYPE_CHOICES, default=MAIN)
    contactData = models.CharField('Kontaktdaten', max_length=200)
    spaContact = models.BooleanField('SPA Kontak', default=False)
    person = models.ForeignKey(Person)

    class Meta:
    	ordering: ["contactSeverity"]

class Tag(models.Model):
    tagName = models.CharField('Tag', max_length=50, blank=False)
    tagCategory = models.CharField('Kategorie', max_length=50, blank=False)





class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['addressType', 'addressLine', 'zipCode', 'city', 'country']
        widgets = {
            'zipCode': forms.TextInput(attrs={'size': 7}),
            'city': forms.TextInput(attrs={'size': 30})
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['contactSeverity', 'contactType',
                  'contactData', 'spaContact']
        widgets = {
            'contactData': forms.Textarea(attrs={'rows': 4, 'col': 50})
        }
