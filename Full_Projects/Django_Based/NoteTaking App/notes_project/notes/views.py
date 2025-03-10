from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Note
from .forms import NoteForm
from django.contrib.auth import login
# Create your views here.


# Create Note
@login_required
def new_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'notes/new_note.html', {'form': form})

# List Notes
@login_required
def note_list(request):
    notes = Note.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'notes/note_list.html', {'notes': notes})

# Edit Note
@login_required     
def edit_note(request, id):
    note = get_object_or_404(Note, id=id, user=request.user)
    if request.method =="POST":
        form = NoteForm(request.POST, instnce=note)
        if form.is_calid():
            form.save()
            return redirect('note_list')
        
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/edit_note.html', {'form': form})

# Delete Note
@login_required
def delete_note(request,id):
    note = get_object_or_404(Note, id=id, user=request.user)
    if request.method == "POST":
        note.delete()
        return redirect('note_list')
    return render(request, 'notes/delete_notes.html', {'note': note})

# Search Notes
@login_required
def search_notes(request):
    query = request.GET.get('q')
    notes = Note.objects.filter(user=request.user)
    if query:
        notes = notes.filter(title__icontains=query)  | notes.filter(content__icontains=query) | notes.filter(tags__icontains=query)
    return render(request, 'notes/note_list.html', {'notes': notes, 'query': query})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('note_list')  # Redirect after successful signup
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})