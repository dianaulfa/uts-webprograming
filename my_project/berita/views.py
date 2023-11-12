from django.shortcuts import render

def beranda(request):
    return render(request, 'berita/beranda.html')

def about(request):
    return render(request, 'berita/about.html')

def coba(request):
    return render(request, 'berita/coba.html')

def index(request):
    return render(request, 'berita/index.html')





