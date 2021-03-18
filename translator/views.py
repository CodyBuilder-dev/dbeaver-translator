from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from .models import Property, UploadFileModel, File


# Create your views here.
from .module.property_parser import parse


def index(request):
    file_list = File.objects.order_by()
    template = loader.get_template('translator/index.html')
    form = UploadFileForm()
    context = {
        'form':form,
        'file_list':file_list
    }

    return HttpResponse(template.render(context,request))

def detail(request, file_id):
    # return HttpResponse("You're looking at question %s." % file_id)
    file = File.objects.get(id= file_id)
    context ={
        'file':file
    }
    return HttpResponse(render())

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                file = File.objects.get(package_name = request.POST['package_name']
                                      ,file_name =  request.POST['file_name'])
            except:
                file = File()
                file.package_name = request.POST['package_name']
                file.file_name = request.POST['file_name']
                # file.save()
            # 파일 내용 파싱 및 파일객체에 저장
            # 모델의 다른 값들은 POST에, 파일은 FILES에 저장
            # return HttpResponse(file.package_name)


            properties = parse(request.FILES['file'])
            for key,value in properties:
                property = Property()
                property.file = file
                property.name,property.value_en = key,value
                property.save()
            return HttpResponse(request.FILES['file'])



    else :
        return HttpResponse("Please Use Post Method")
    # else:
    #     form = UploadFileForm()
    # return render(request, 'upload.html', {'form': form})

def google_translation(request):
    return HttpResponse("Google Translation!")
    # if request.method == 'POST':
    #     form = UploadFileForm(request.POST, request.FILES)
    #     form.save()
    #     return HttpResponseRedirect("")

def encoding(request):
    return HttpResponse("Encoding!")