from django.shortcuts import render
from django.shortcuts import HttpResponse
def index(request):
    params={'name':'Pradumn','place':'Varanasi'}
    return render(request,'index.html',params)
def analize(request):
    dj_text=request.POST.get('text','default')
    remove_punchuation = request.POST.get('remove_punct', 'off')
    upper_case = request.POST.get('upper', 'off')

    if remove_punchuation=='on':
        punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        final_text = ''
        for i in dj_text:
            if i not in punctuation:
                final_text+=i
        params = {'name': 'Pradumn', 'text': final_text}
        dj_text = final_text


    if upper_case=='on':
        final_text = ''
        for i in dj_text:
            final_text+=i.upper()
        params={'name':'Pradumn','text':final_text}


    if remove_punchuation=='off' and upper_case=='off':
        return HttpResponse('<h1>Error</h1>')

    return render(request, 'analize.html', params)


