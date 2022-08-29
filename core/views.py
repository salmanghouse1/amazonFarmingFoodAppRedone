from django.shortcuts import render
import mailbox
import pandas as pd
import matplotlib.pyplot as plt
import folium

import csv
# from pathlib import Path
# from brukeropusreader import read_file
# from tqdm import tqdm_notebook as tqdm
# from django.http import HttpResponse
from django.template import loader
# from unicodedata import name
# from django.shortcuts import redirect, render
# from django.http import HttpResponse
# from django.template import context
from unicodedata import name
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import context

# from unicodedata import name
# from django.shortcuts import redirect, render
# from django.http import HttpResponse
# from django.template import context
import csv
# add this line
# from django.templatetags.static import static
from django.http import HttpResponse
from django.template import loader
# import csv
        
def home(request):
    context=""

    df = pd.read_csv('static/railway_stations.csv')
    return render(request, 'index.html', {'columns': df.columns, 'rows': df.to_dict('records')})
    # with open('static/railway_stations') as f:
    #     for line in csv.DictReader(f, fieldnames=()):
    # with open('static/railway_stations.csv', mode='r') as infile:
    #     reader = csv.reader(infile)
    #     mydict = {rows[1]:rows[4] for rows in reader}          
    #     context=mydict
    # return render(request, 'index.html',context)

    
