from django.shortcuts import render, redirect

from petstagram.pets.forms import PetForm
from petstagram.pets.models import Pet, Like


def list_pets(request):
    all_pets = Pet.objects.all()

    context = {
        'pets': all_pets,
    }

    return render(request, 'pets/pet_list.html', context)


def pet_details(request, pk):
    pet = Pet.objects.get(pk=pk)
    pet.likes_count = pet.like_set.count()

    context = {
        'pet': pet,
    }

    return render(request, 'pets/pet_detail.html', context)


def like_pet(request, pk):
    pet_to_like = Pet.objects.get(pk=pk)
    like = Like(
        pet=pet_to_like,
    )
    like.save()

    return redirect('pet details', pet_to_like.id)


def create_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list pets')
    else:
        form = PetForm()

    context = {
        'form': form,
    }

    return render(request, 'pets/pet_create.html', context)
