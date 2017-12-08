'''run this py with django shell
   $ python manage.py shell
   $ exec(open('./pipkin/console/createPerson.py').read())
'''
from pipkin.models import Person

person = Person(firstname="Lukas", name="Schreier_Del")

person.save()


print(person.id)
