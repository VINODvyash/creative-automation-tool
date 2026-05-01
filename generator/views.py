import zipfile
from django.http import FileResponse

from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
import os
from .services import generate_creative


# Create your views here.

@api_view (['POST'])
def generate_creatives(request):
    background = request.FILES.get('background')
    logo = request.FILES.get('logo')
    

    if not background:
        return Response({"error": "Background image required"}, status=400)
    
    #Save background temporarily

    bg_path = os.path.join(settings.MEDIA_ROOT, 'backgrounds', background.name)

    os.makedirs(os.path.dirname(bg_path), exist_ok=True)

    with open(bg_path, 'wb+') as f:
        for chunk in background.chunks():
            f.write(chunk)

    #Save Logo

    logo_path = None
    if logo:
        logo_path = os.path.join(settings.MEDIA_ROOT, 'logos', logo.name)

        os.makedirs(os.path.dirname(logo_path), exist_ok=True)

        with open(logo_path, 'wb+') as f:
            for chunk in logo.chunks():
                f.write(chunk)

    #PANEL SETUP 
    panel_folder = os.path.join(settings.MEDIA_ROOT, 'panels')
    panel_files = os.listdir(panel_folder)

    if not panel_files:
        return Response({"error": "No panel images found"}, status=400)
    
    
    #BULK GENERATION 

    output_files = []


    for i , panel_file in enumerate(panel_files):

        panel_path = os.path.join(panel_folder, panel_file) 


        output_path = os.path.join(settings.MEDIA_ROOT, 'outputs', f"output_{i}.png")
        os.makedirs (os.path.dirname(output_path), exist_ok=True)

        generate_creative(bg_path, logo_path, panel_path, output_path)
        output_files.append(f"/media/outputs/output_{i}.png")


    # 🔥 ADD ZIP CODE HERE
    zip_path = os.path.join(settings.MEDIA_ROOT, 'outputs', 'creatives.zip')

    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for file in output_files:
            file_path = os.path.join(settings.BASE_DIR, file.strip("/"))
            zipf.write(file_path, os.path.basename(file_path))


    return Response({
        "message": "Creatives generated",
        "outputs": output_files,
        "zip": "/media/output/creatives.zip"
    })












    # #Output file
    # output_path = os.path.join (settings.MEDIA_ROOT, "output.png")

    # os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # generate_creative(bg_path, logo_path, output_path)

    # return Response({
    #     "message": "Creative generated",
    #     "output": f"/media/output.png"
    # })