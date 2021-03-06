from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Note
from .forms import NoteForm

# Create your views here.

def notes_list(request):
    # django ORM
    notes = Note.objects.all() 
    return render(request, 'core/notes_list.html', context={'notes': notes})

def notes_detail(request, pk):
    note = Note.objects.get(pk=pk)
    return render(request, 'core/notes_detail.html', {'note': note})

def note_new(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect('notes_list')
            # return redirect('notes-detail', pk=note.pk)
    else:        
        form = NoteForm()
    return render(request, 'core/note_new.html', {'form': form})

def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect('notes-detail', pk=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'core/note_edit.html', {'form':form})

def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('notes_list')




       

