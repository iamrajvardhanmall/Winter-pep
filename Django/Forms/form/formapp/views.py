from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Note

# Create your views here.
def Raj(request):
    return HttpResponse("This is raj")

def form(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        
        # Form validation
        if not title or not description:
            messages.error(request, 'Please fill the form')
        else:
            # Save the note to database
            try:
                Note.objects.create(title=title, description=description)
                messages.success(request, 'Your form is submitted')
                return redirect('form_save_data')  # Redirect to avoid form resubmission
            except Exception as e:
                messages.error(request, 'An error occurred while saving your note. Please try again.')
    
    # Get all notes to display on the page
    notes = Note.objects.all().order_by('-created_at')
    
    context = {
        'notes': notes
    }
    
    return render(request, 'form.html', context)

def edit_note(request, note_id):
    # Get the note object or return 404 if not found
    note = get_object_or_404(Note, id=note_id)
    
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        
        # Form validation
        if not title or not description:
            messages.error(request, 'Please fill all fields')
        else:
            # Update the note in database
            try:
                note.title = title
                note.description = description
                note.save()
                messages.success(request, 'Note updated successfully!')
                return redirect('form_save_data')
            except Exception as e:
                messages.error(request, 'An error occurred while updating your note. Please try again.')
    
    context = {
        'note': note
    }
    
    return render(request, 'edit_note.html', context)

def delete_note(request, note_id):
    # Get the note object or return 404 if not found
    note = get_object_or_404(Note, id=note_id)
    
    try:
        # Delete the note from database
        note_title = note.title  # Store title for success message
        note.delete()
        messages.success(request, f'Note "{note_title}" deleted successfully!')
    except Exception as e:
        messages.error(request, 'An error occurred while deleting the note. Please try again.')
    
    return redirect('form_save_data')