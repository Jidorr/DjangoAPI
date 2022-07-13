import glob
from io import StringIO
import io
from msilib.schema import File
import os
import threading
from urllib.request import HTTPRedirectHandler
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.core.files.storage import FileSystemStorage
import pandas as pd
import dask.dataframe as dd
from asgiref.sync import sync_to_async
import time
import asyncio
import os
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

from BMAT_API.settings import BASE_DIR

from .forms import FileForm
from .models import File

def files_list(request):
    files = File.objects.all()
    return render(request, 'files_list.html', {
        "files": files
    })

async def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        loop = asyncio.get_event_loop()
        loop.create_task(upload_file_async(form))
        return redirect("files_list")
    else:
        form = FileForm()
    return render(request, 'upload_file.html', {
        'form': form
    })

def delete_file(request, pk):
    if request.method == 'POST':
        file = File.objects.get(pk=pk)
        file.delete()
    return redirect('files_list')


async def upload_file_async(form):
    if form.is_valid():
        form.save()
        file_processing()

def file_processing():
    path = os.path.join(BASE_DIR, 'media/files/csvs/*.csv')
    list_of_files = glob.glob(os.path.join(BASE_DIR, 'media/files/csvs/*.csv'))
    latest_file = max(list_of_files, key=os.path.getctime)
    df = dd.read_csv(latest_file)
    df = df.groupby(['Song','Date']).sum().reset_index().compute()
    df.to_csv(latest_file, index=None)
