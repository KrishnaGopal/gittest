from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
        print('123')
        return render(request,'home.html')

def count(request):
        fulltext = request.GET['words']
        total_words = fulltext.split()
        count = len(total_words)
        count_discnary = {}
        for word in total_words:
                if word in count_discnary:
                        count_discnary[word] += 1
                else:
                        count_discnary[word] = 1
        count_discnary_list = count_discnary.items()
        dictionary_sort = sorted(count_discnary_list,key=operator.itemgetter(1),reverse=True)
        return render(request,'count.html',{'fulltext':fulltext,'count':count,'count_discnary':dictionary_sort})

def about(request):
        return render(request,'about.html')
        
