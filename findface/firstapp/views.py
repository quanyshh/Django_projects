from django.shortcuts import render
from django.http import HttpResponseRedirect
import os
from .models import UploadWorkSheetForm
from .findface import FaceControl
from .models import WorkSheet

def upload(request):
    fc = FaceControl()
    if request.method == 'POST':
        form = UploadWorkSheetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #worksheet_id = request.session['worksheet_id']
            worksheets = WorkSheet.objects.values('model_pic').last()
            count = fc.faces(worksheets)
            print(count)
            url_name = worksheets['model_pic'].split('/')[0]
            url_type = worksheets['model_pic'].split('/')[1].split('.')[1]
            urls = []
            for i in count:
                url = url_name + '/face-'+str(i)+ '.' +url_type
                urls.append(url)
            print(urls)
            context = {
                'urls':urls
            }
            return render(request, 'firstapp/index.html', {'urls': urls})
    else:
        form = UploadWorkSheetForm()

    return render(request, 'firstapp/index.html', {'form': form})
