import datetime
import mimetypes
import os

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from turnir.forms import RegisterFlagForm
from turnir.models import FlagType, Flag, UserAdvice, Advice


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = RegisterFlagForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            flags = Flag.objects.filter(user_id = request.user.id, hash=form.cleaned_data['flag_hash'])
            for e in flags:
                e.captured = True
                e.capture_time = datetime.datetime.now()
                e.save()

    form = RegisterFlagForm()

    captured_flags = Flag.objects.all().filter(user_id=request.user.id, captured=True).values()
    for cf in captured_flags:
        cf['description'] = FlagType.objects.filter(id=cf['type_id_id']).values()[0]['description']

    context = {
        'form': form,
        'cf': captured_flags,

    }

    return render(request, 'index.html', context=context)

def advice(request):
    advices = UserAdvice.objects.filter(user_id=request.user.id).values()
    for e in advices:
        adv = Advice.objects.filter(id=e['advice_id_id']).values()[0]
        e['description'] = adv['description']
        if not e['showed'] and not e['notneed']:
            e['description'] = ''
        e['showtime'] = adv['showtime']
        e['may_take'] = e['showtime'] < timezone.make_aware(datetime.datetime.now(), timezone.get_default_timezone()) and not e['showed'] and not e['notneed']
        e['penalty'] = adv['penalty']
    context = {
        'advices': advices,
    }

    return render(request, 'advice.html', context=context)

def docs(request, filename=''):
    if filename != '':
        # Define Django project base directory
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # Define the full file path
        filepath = BASE_DIR + '/turnir/static/docs/' + filename
        # Open the file for reading content
        path = open(filepath, 'rb')
        # Set the mime type
        mime_type, _ = mimetypes.guess_type(filepath)
        # Set the return value of the HttpResponse
        response = HttpResponse(path, content_type=mime_type)
        # Set the HTTP header for sending to browser
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        # Return the response value
        return response
    else:
        # Load the template
        return render(request, 'docs.html')


def take_advice(request, pk):
    advice = UserAdvice.objects.filter(id=pk)[0]
    adv = Advice.objects.filter(id=advice.advice_id_id).values()[0]
    if adv['showtime'] < timezone.make_aware(datetime.datetime.now(), timezone.get_default_timezone()) and not advice.showed and not advice.notneed:
        advice.showed = True
        advice.take_time = datetime.datetime.now()
        advice.save()

    return HttpResponseRedirect(reverse('advice'))