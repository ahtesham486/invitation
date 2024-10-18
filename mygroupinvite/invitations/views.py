from django.shortcuts import render, redirect
from .forms import InvitationForm

def invite_member(request):
    if request.method == 'POST':
        form = InvitationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the invitation to the database
            return redirect('success')  # Redirect to a success page or display a message
    else:
        form = InvitationForm()
    return render(request, 'invite_member.html', {'form': form})

def success(request):
    return render(request, 'success.html')
