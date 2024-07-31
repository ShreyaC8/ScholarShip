from django.shortcuts import render
from .scholarships import generic
from .scholarships import agri_vet

def search_dictionary(request):
    query = request.GET.get('query', '')
    results = {}
    
    if query:
        results = {k: v for k, v in generic.items() or v in agri_vet.items() if query.lower() in k.lower()}

    return render(request, 'dictionary_app/search.html', {'results': results, 'query': query})
