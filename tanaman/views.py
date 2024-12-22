from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Tumbuhan
from .forms import PostForm
# Create your views here.

#--------------- Admin login -------------
@login_required
def home(request):
    plants = Tumbuhan.objects.all()
    context = {'plants': plants}
    
    if request.user.is_superuser:
        return render(request, 'tanaman/admin_home.html', context)
        
    
    return render(request, 'tanaman/home.html', context)
    
    # return render(request, 'tanaman/admin_home.html', context)

@login_required
def delete_plant(request, id):
    plant = get_object_or_404(Tumbuhan, pk=id)
    context = {'plant': plant}

    if request.method == 'GET':
        return render(request, 'tanaman/post_confirm_delete.html', context)
      
    elif request.method == 'POST':
        plant.delete()
        messages.success(request, 'The post has been deleted successfully.')
        return redirect('plants')

@login_required
def edit_plant(request, id):
    plant = get_object_or_404(Tumbuhan, id=id)

    if request.method == 'GET':
        context = {'form': PostForm(instance=plant), 'id': id}
        return render(request, 'tanaman/post_form.html', context)

    elif request.method == 'POST':
        form = PostForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'The post has been updated successfully.')
            return redirect('plants')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'tanaman/post_form.html', {'form': form})


@login_required
def create_plant(request):
    if request.method == 'GET':
        context = {'form': PostForm()}
        return render(request, 'tanaman/post_form.html', context)
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'The post has been created successfully.')
            return redirect('plants')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'tanaman/post_form.html', {'form': form})