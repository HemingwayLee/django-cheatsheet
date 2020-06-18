from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core.files.storage import FileSystemStorage
from .task import uploadInBackground


@require_http_methods(["GET"])
def upload(request):
    return render(request, 'upload.html')

@require_http_methods(["GET"])
def dashboard(request):
    return render(request, 'dashboard.html')

@require_http_methods(["POST"])
def do_upload(request):
    uploadedFile = request.FILES['myfile'] if 'myfile' in request.FILES else False
    if uploadedFile:
        fss = FileSystemStorage()
        filename = fss.save(uploadedFile.name, uploadedFile)
        uploadInBackground(filename)
        return render(request, 'upload.html', {'filename': filename})

    return render(request, 'upload.html')
