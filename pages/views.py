from django.shortcuts import render

# Create your views here.


def index_page_view(request):
    context = {}
    return render(request, "pages/index.html", context)
