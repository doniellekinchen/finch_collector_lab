from django.shortcuts import render

def about(request):
    context = {
        'app_name': 'finchcollector',
        'description': 'A collection of finch data.',
    }
    return render(request, 'finches/about.html', context)

def all_finches(request):
    finches_data = [
        {'name': 'Zebra Finch', 'color': 'Black and White', 'size': 'Small'},
        {'name': 'Gouldian Finch', 'color': 'Various', 'size': 'Small'},
        {'name': 'Canary', 'color': 'Yellow', 'size': 'Small'},
    ]
    context = {'finches_data': finches_data}
    return render(request, 'finches/all_finches.html', context)

