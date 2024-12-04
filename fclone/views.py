from django.shortcuts import render
from django.http import HttpResponse
from .forms import LogiForm

from django.shortcuts import render
from .forms import LogiForm

def login(request):
    if request.method == "POST":
        form = LogiForm(request.POST)
        if form.is_valid():
            form.save()  # Automatically saves to the database
            return render(request, 'hk.html')  # Redirect to success page
    else:
        form = LogiForm()
    return render(request, 'login.html', {'form': form})




def display_data(request):
    data_lines = []
    try:
        # Open the file and read lines
        with open('form_data.txt', 'r') as file:
            data_lines = [line.strip().split(',') for line in file.readlines() if ',' in line]
    except FileNotFoundError:
        data_lines = [["No data available yet."]]
    
    return render(request, 'display_data.html', {'data_lines': data_lines})




