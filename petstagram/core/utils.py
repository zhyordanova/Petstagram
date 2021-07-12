from petstagram.pets.models import Pet


def get_pet_by_pk(pk):
    return Pet.objects.get(pk=pk)
