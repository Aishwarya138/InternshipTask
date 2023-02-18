from django.shortcuts import render
# from django.http import HttpResponse
from django.core.files import File
from .models import *
import pandas as pd 

# Create your views here.
def create_db(file_path):
  df = pd.read_csv(file_path, delimiter=',')
  print(df.values)
  list_of_candles = list(row for row in df.values)
  # for data in list_of_candles:
    
    # CandleData.objects.create(
    #   open = l[3],
    #   high = l[4],
    #   low = l[5],
    #   close = l[6],
    #   date = l[1],
    # )

def index(request):
  if request.method == 'POST':
    file = request.FILES['file']
    obj = File.objects.create(file=file)
    create_db(obj.file)
    timeframe = request.POST.get('timeframe')
  return render(request, 'index.html')