from django.shortcuts import render, get_object_or_404

from .forms import EntryForm, ProjectForm, ClientForm
from .models import Client, Entry, Project



def clients(request):

    if request.method == "POST":
        client_form = ClientForm(request.POST)
        if client_form.is_valid():
            client = Client()
            client.name = client_form.cleaned_data['name']
            client.save()
            #empty form
            client_form = ClientForm()  
    else:
        client_form = ClientForm(request.POST)


    client_list = Client.objects.all()
    return render(request, 'clients.html', {
        'client_list': client_list,
        'client_form' : client_form,
    })


def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'client_detail.html', {
        'client': client,
    })


def entries(request):
    if request.method == 'POST':
        # Create our form object with our POST data
        entry_form = EntryForm(request.POST)
        if entry_form.is_valid():
            # If the form is valid, let's create and Entry with the submitted data
            entry = Entry()
            entry.start = entry_form.cleaned_data['start']
            entry.end = entry_form.cleaned_data['end']
            entry.project = entry_form.cleaned_data['project']
            entry.description = entry_form.cleaned_data['description']
            entry.save()
            #create empty form
            entry_form = EntryForm()
    else:
        entry_form = EntryForm()

    entry_list = Entry.objects.all()
    return render(request, 'entries.html', {
        'entry_list': entry_list,
        'entry_form': entry_form,
        #'start' : entry_form.cleaned_data['start'],
    })


def projects(request):
    if request.method == 'POST':
        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            project = Project()
            project.client = project_form.cleaned_data['client']
            project.name = project_form.cleaned_data['name']
            project.save()
            #empty form
            project_form = ProjectForm()
    else:
        project_form = ProjectForm(request.POST)

    project_list = Project.objects.all()
    return render(request, 'projects.html', {
        'project_list': project_list,
        #this is important
        'project_form' : project_form,
    })
