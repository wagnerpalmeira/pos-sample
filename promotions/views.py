from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Promotion
from .forms import CreatePromotionForm

def promotions_view(request):
    promotions = Promotion.objects.all()
    return render(request, 'promotions/index.html', {
        'promotions': promotions
    })


@login_required
def create_promotion_view(request):
    form = CreatePromotionForm()
    if request.method == 'POST':
        form = CreatePromotionForm(request.POST)
        if form.is_valid():
            promotion = form.save(commit=False)
            promotion.user = request.user
            promotion.save()
            return redirect('promotions_view')
    
    return render(request, 'promotions/register.html', {'form': form})