from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Petition, Votes, User
from django.shortcuts import get_object_or_404, redirect

# Create your views here.

def index(request):
    petitions = Petition.objects.all()
    for petition in petitions:
        petition.vote_count = vote_count(petition)
    template_data = {}
    template_data['title'] = 'Petitions'
    template_data['petitions'] = petitions
    template_data['vote_count'] = vote_count
    return render(request, 'petitions/index.html', {'template_data': template_data})

@login_required
def create_petition(request):
    if request.method == 'GET':
        template_data = {}
        template_data['title'] = 'Create Petition'
        return render(request, 'petitions/create_petition.html', {'template_data': template_data})
    elif request.method == 'POST' and request.POST['title'] != '' and request.POST['description'] != '':
        petition = Petition()
        petition.title = request.POST['title']
        petition.description = request.POST['description']
        petition.user = request.user
        petition.save()
        return redirect('petitions.index')
    else:
        return redirect('petitions.create_petition')

@login_required
def edit_petition(request, petition_id):
    petition = get_object_or_404(Petition, id=petition_id)
    if request.user != petition.user:
        return redirect('petitions.index')

    if request.method == 'GET':
        template_data = {}
        template_data['title'] = 'Edit Petition'
        template_data['petition'] = petition
        return render(request, 'petitions/edit_petition.html', {'template_data': template_data})
    elif request.method == 'POST' and request.POST['title'] != '' and request.POST['description'] != '':
        petition.title = request.POST['title']
        petition.description = request.POST['description']
        petition.save()
        return redirect('petitions.index')
    else:
        return redirect('petitions.edit_petition', petition_id=petition_id)

@login_required
def delete_petition(request, petition_id):
    petition = get_object_or_404(Petition, id=petition_id)
    if request.user != petition.user:
        return redirect('petitions.index')

    petition.delete()
    return redirect('petitions.index')

@login_required
def vote_petition(request, petition_id):
    petition = get_object_or_404(Petition, id=petition_id)
    user = request.user

    existing_vote = Votes.objects.filter(user=user, petition=petition).first()
    if existing_vote:
        existing_vote.delete()
    else:
        vote = Votes()
        vote.user = user
        vote.petition = petition
        vote.save()

    return redirect('petitions.index')

def vote_count(petition):
    return Votes.objects.filter(petition=petition).count()


