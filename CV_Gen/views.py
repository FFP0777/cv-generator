# CV_Gen/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
import pdfkit
import urllib.parse
from .models import Profile

def accept(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')

        photo_file = request.FILES.get('photo')
        photo_position = request.POST.get('photo_position', 'center')

        profile = Profile(name=name, email=email, phone=phone, photo=photo_file)
        additional_sections = []
        section_index = 1

        while True:
            title_key = f'section_title_{section_index}'
            content_key = f'section_content_{section_index}'
            if title_key not in request.POST or content_key not in request.POST:
                break
            title = request.POST.get(title_key, '')
            content = request.POST.get(content_key, '')
            if title or content:
                additional_sections.append({
                    'title': title,
                    'content': content,  
                })
            section_index += 1

        profile.additional_sections = additional_sections
        profile.save()

        
        request.session[f"photo_position_{profile.id}"] = photo_position
        return redirect('list_profiles')
    else:
            return render(request, 'CV_Gen/accept.html')

def list_profiles(request):
    profiles = Profile.objects.all()
    return render(request, 'CV_Gen/list.html', {'profiles': profiles})

def resume(request, id):
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template('CV_Gen/resume.html')
    photo_position = request.session.get(f"photo_position_{id}", "center")

    photo_url = ''
    if user_profile.photo:
        import urllib.parse
        photo_path = user_profile.photo.path.replace("\\", "/")
        encoded_path = urllib.parse.quote(photo_path)
        photo_url = f"file:///{encoded_path}"

    html = template.render({
        'user_profile': user_profile,
        'photo_position': photo_position,
        'photo_url': photo_url,
    })

    options = {
        'page-size': 'Letter',
        'encoding': "UTF-8",
        'enable-local-file-access': None,  
    }
    config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
    pdf = pdfkit.from_string(html, False, options=options, configuration=config)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
    return response



from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  
def preview_pdf(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        
        html = f"""
        <!DOCTYPE html>
        <html><body>
            <h1>{name}</h1>
            <p>Email: {email}</p>
            <p>Phone: {phone}</p>
        </body></html>
        """
        
        import pdfkit
        options = {
            'page-size': 'Letter',
            'encoding': "UTF-8",
            'enable-local-file-access': None,
        }
        config = pdfkit.configuration(wkhtmltopdf=r'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
        pdf = pdfkit.from_string(html, False, options=options, configuration=config)

        return HttpResponse(pdf, content_type='application/pdf')
from django.template.loader import render_to_string
   
from django.core.files.storage import default_storage
import os

def preview_pdf(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        photo_position = request.POST.get("photo_position", "center")
        photo_caption = request.POST.get("photo_caption", "")
        sections = []
        for key in request.POST:
            if key.startswith("section_title_"):
                suffix = key.split("section_title_")[1]
                title = request.POST.get(key)
                content = request.POST.get("section_content_" + suffix, "")
                sections.append({'title': title, 'content': content})

        photo_file = request.FILES.get("photo")
        photo_url = None

        if photo_file:
            temp_path = default_storage.save("temp_photos/" + photo_file.name, photo_file)
            abs_path = default_storage.path(temp_path)
            photo_url = "file:///" + abs_path.replace("\\", "/")

        html = render_to_string("CV_Gen/resume.html", {
            "user_profile": {
                "name": name,
                "email": email,
                "phone": phone,
                "additional_sections": sections,
            },
            "photo_position": photo_position,
            "photo_url": photo_url, 
        })

        config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
        options = {
            'page-size': 'Letter',
            'encoding': "UTF-8",
            'enable-local-file-access': None,  
        }

        pdf = pdfkit.from_string(html, False, options=options, configuration=config)
        return HttpResponse(pdf, content_type='application/pdf')

