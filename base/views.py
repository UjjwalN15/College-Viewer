# from django.shortcuts import render
# from .models import *
# from .serializers import *
# from django.core.paginator import Paginator #For Pagination

# # Create your views here.

# # class CollegeApiViewsets(viewsets.ModelViewSet):
# #     queryset = College.objects.all()
# #     serializer_class = CollegeSerializer

# # def home(request):
# #     colleges = College.objects.all().order_by('name')  # Get all colleges
    
# #     # # Set up pagination
# #     # paginator = Paginator(colleges, 10)  # Show 10 colleges per page
# #     # page_number = request.GET.get('page')
# #     # page_obj = paginator.get_page(page_number)
# #     SEARCH_FIELDS = 'name'
# #     return render(request, 'index.html', {'college': colleges})

# # def search_colleges(request):
# #     query = request.GET.get('q')  # Get the search query
# #     colleges = College.objects.all()  # Default to all colleges

# #     if query:
# #         colleges = colleges.filter(name__icontains=query)  # Filter by name

# #     return render(request, 'index.html', {
# #         'colleges': colleges,
# #         'query': query
# #     })

# def home (request):
#     query = request.GET.get('q', '')  # Get the search query, default to empty string
#     if query:
#         colleges = College.objects.filter(name__icontains=query)  # Filter colleges by query
#     else:
#         colleges = College.objects.all()  # Get all colleges if no query

#     return render(request, 'index.html', {
#         'colleges': colleges,
#         'query': query
#     })
from django.shortcuts import render
from .models import College  # Adjust the import based on your app structure

def home(request):
    query = request.GET.get('q', '')  # Get the search query from GET parameters
    if query:
        colleges = College.objects.filter(name__icontains=query)  # Filter colleges by name
    else:
        colleges = College.objects.all().order_by("name")  # Get all colleges if no query

    return render(request, 'index.html', {
        'college': colleges,  # Make sure the context variable matches what you're using in the template
        'query': query  # Pass the query back to the template
    })

