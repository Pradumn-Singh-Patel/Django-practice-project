# this is self made
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    params={'name':'Pradumn','place':'Varanasi'}
    return render(request,'index.html',params)
#     return HttpResponse('''<Button> <a href="http://127.0.0.1:8000/next">Next</Button>''''''<Button> <a href="http://127.0.0.1:8000/previous">Previous</Button>''')
#     #return HttpResponse('''<Button> <a href="http://127.0.0.1:8000/next">Next</Button>''')
def analize(request):
    dj_text=request.POST.get('text','default')
    punchua = request.POST.get('remove_punct', 'off')
    char_count = request.POST.get('char_count', 'off')
    upper_case = request.POST.get('upper', 'off')
    print(punchua)
    final_text=''
    if punchua=='on':
        for i in dj_text:
         punct = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
         if i not in punct:
             final_text+=i


    if char_count=='on':
        count=len(final_text)
    duplicate=''
    if upper_case=='on':
        for i in final_text:
            duplicate+=i.upper()
    params={'name':'Pradumn singh patel','text':final_text,'count':count,'upper_case':duplicate}
    return render(request,'analize.html',params)
# def previous(request):
#     return HttpResponse("previous <a href='/'>back</a>")