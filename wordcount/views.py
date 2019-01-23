from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):return render(request,'home.html',{'hit':'Hidden text here'})
def count(request):
    txt=request.GET['fulltext']
    # print(txt)
    count=len(txt.split())
    # print(txt)
    dictionary={}
    for i in txt.split():
        if i in dictionary:
            dictionary[i]+=1
        else: dictionary[i]=1
    return render(request,'count.html',{'text':txt,'msg':count,'dic':sorted(dictionary.items(),key=operator.itemgetter(1),reverse=True)})
def textpage(request):return HttpResponse('<h1>Home page</h1>')
def about(r):return render(r,'about.html')
