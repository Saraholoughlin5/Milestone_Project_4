from django.shortcuts import render

# Adapted from Boutique Ado project


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')
