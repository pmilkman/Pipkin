from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views import generic

from .models import Person


def index(request):
    num_person = Person.objects.all().count()
    latestAdded = Person.objects.latest('created')
    latestUpdated = Person.objects.latest('modified')

    return render(
        request,
        'pipkin/index.html',
        context={'num_person': num_person,
                 'latestAddedPerson': latestAdded,
                 'latestUpdatedPerson': latestUpdated
                 },
    )


class PersonsListView(generic.ListView):
    model = Person
    template_name = 'pipkin/person_list.html'
    context_object_name = 'my_person_list'
    queryset = Person.objects.all()


class PersonDetailView(generic.DetailView):
    model = Person
    template_name = 'pipkin/person.html'
