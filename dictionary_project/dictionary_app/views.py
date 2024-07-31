from django.shortcuts import render
from .scholarships import schol_type

def search_dictionary(request):
    query = request.GET.get('query', '')
    results = {}
    
    if query:
        results = {k: v for k, v in schol_type.items() if query.lower() in k.lower()}

    return render(request, 'dictionary_app/search.html', {'results': results, 'query': query})
