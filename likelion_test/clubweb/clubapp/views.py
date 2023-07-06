from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Club, Comment

# Create your views here.
def home(request):
    clubs = Club.objects.all()
    return render(request, 'home.html', {'clubs' : clubs})

def detail(request, club_id):
    club = get_object_or_404(Club, pk=club_id)
    return render(request, 'detail.html', {'club' : club})

def create(request):
    if request.method == 'POST':
        club = Club()
        club.name = request.POST['name']
        club.description = request.POST['description']
        club.numofpeople = request.POST['numofpeople']
        club.save()
        return redirect('detail', club.id)
    return render(request, 'create.html')

def edit(request, club_id):
    edit_club = Club.objects.get(id = club_id)
    return render(request, 'edit.html', {'club' : edit_club})

def update(request, club_id):
    update_club = Club.objects.get(id = club_id)
    update_club.name = request.POST['name']
    update_club.description = request.POST['description']
    update_club.numofpeople = request.POST['numofpeople']
    update_club.save()
    return redirect('detail', update_club.id)

def delete(request, club_id):
    delete_club = Club.objects.get(id = club_id)
    delete_club.delete()
    return redirect('home')

def comment(request, club_id):
    if request.method == "POST":
        new_comment = Comment()
        new_comment.club = get_object_or_404(Club, pk = club_id)
        new_comment.comment = request.POST['comment']
        new_comment.created_at = timezone.now()
        new_comment.save()
    return redirect('detail', club_id)
