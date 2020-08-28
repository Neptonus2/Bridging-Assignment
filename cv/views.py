# IT DOESN'T MATTER WHETHER YOU WRITE SOMETHING HERE. DJANGO WILL ONLY LOOK AT BLOG.VIEWS.py FOR SOME REASON

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect

from .models import Traits
from .forms import TraitsForm

def cv(request):
   # traits = Traits.objects.all() 'traits' : traits
    return render(request, 'cv.html', {})

def cv_edit(request, pk):
    trait = get_object_or_404(Traits, pk=pk)
    if request.method == "POST":
        form = TraitsForm(request.POST, instance=trait)
        if form.is_valid():
            trait = form.save(commit=False)
            trait.save()
            return redirect('cv_edit', pk=trait.pk)
    else:
        form = TraitsForm(instance=trait) 
    return render(request, 'cv/cv_edit.html', {'form': form})