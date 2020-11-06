from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.utils import timezone
from .models import Bb, Rubric
from .forms import BbForm


# Create your views here.
def main_bboard(request):
    search_query = request.GET.get('search', '')
    if search_query:
        bbs = Bb.objects.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query))
    else:
        bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    return render(request, 'bboard/index.html', {'bbs': bbs,
                                                 'rubrics': rubrics})


def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs,
               'rubrics': rubrics,
               'current_rubric': current_rubric}
    return render(request, 'bboard/by_rubric.html', context)


@login_required
def bb_create(request):
    if request.method == 'POST':
        form = BbForm(request.POST)
        if form.is_valid():
            bb = form.save(commit=False)
            bb.author = request.user
            bb.published = timezone.now()
            bb.save()
            return redirect('main_bboard')
    else:
        form = BbForm()
    return render(request, 'bboard/create.html', {'form': form})


@login_required
def bb_delete(request, pk):
    bb = get_object_or_404(Bb, pk=pk)
    bb.delete()
    return redirect('main_bboard')
