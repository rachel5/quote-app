from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Quote
from .forms import QuoteForm

# Create your views here.

def quote_list(request):
  quotes = Quote.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
  return render(request, 'quotes/quote_list.html', {'quotes': quotes})

def quote_detail(request, pk):
  quote = get_object_or_404(Quote, pk=pk)
  return render(request, 'quotes/quote_detail.html', {'quote': quote})

@login_required
def quote_new(request):
  if request.method == "POST":
    form = QuoteForm(request.POST)
    if form.is_valid():
      quote = form.save(commit=False)
      quote.author = request.user
      quote.save()
      return redirect('quote_detail', pk=quote.pk)
  else:
    form = QuoteForm()
  return render(request, 'quotes/quote_edit.html', {'form': form})

@login_required
def quote_edit(request, pk):
  quote = get_object_or_404(Quote, pk=pk)
  if request.method == "POST":
    form = QuoteForm(request.POST, instance=quote)
    if form.is_valid():
      quote = form.save(commit=False)
      quote.author = request.user
      quote.save()
      return redirect('quote_detail', pk=quote.pk)
  else:
    form = QuoteForm(instance=quote)
  return render(request, 'quotes/quote_edit.html', {'form': form})

@login_required
def quote_draft_list(request):
  quotes = Quote.objects.filter(published_date__isnull=True).order_by('created_date')
  return render(request, 'quotes/quote_draft_list.html', {'quotes': quotes})

@login_required
def quote_publish(request, pk):
  quote = get_object_or_404(Quote, pk=pk)
  quote.publish()
  return redirect('quote_detail', pk=pk)

@login_required
def quote_remove(request, pk):
  quote = get_object_or_404(Quote, pk=pk)
  quote.delete()
  return redirect('quote_list')





