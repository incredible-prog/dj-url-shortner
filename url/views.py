from django.shortcuts import render, redirect
import uuid
from django.views.decorators.csrf import csrf_exempt
from .models import Url


def index(request):
    urls = Url.objects.all().order_by('-id')[:5]
    return render(request, 'index.html', context={'urls': urls})


@csrf_exempt
def generate(request):
    if request.method == 'GET':
        url, i, msg = Url(), [], ''
        url.link = str(request.GET.get('link')).strip()
        url.uid = str(uuid.uuid4())[:5]

        # Getting all urls in the database and appending them to "i".
        for item in Url.objects.all():
            i.append(item.link)

        # Checking if url already exist in "i" or not.
        if url.link in i:
            url = Url.objects.get(link=url.link)
            msg = "Looks like your link already exist in our database! click 'verify' to check."
            return render(request, 'index.html', context={'link': f'{url.uid}'.strip(), 'msg': msg})
        else:
            url.save()

        context = {'link': f'{url.uid}'}
        return render(request, 'index.html', context)
    else:
        return redirect('/')


# Redirecting to the raw url
def go(request, uid):
    link = ''
    for obj in Url.objects.all():
        if obj.uid == uid:
            link = str(obj.link)

    if link.startswith('http'):
        return redirect(link)
    else:
        return redirect(f'https://{link}')
