from django.shortcuts import render
from collections import Counter #两种方法
# Create your views here.


def home(request):
    #    return HttpResponse('hello')
    return render(request, 'start.html')


def count(request):
    user_txet = request.GET['text']
    totalcount = len(request.GET['text'])
    word_dict = {}
    common = Counter(user_txet).most_common()
    for word in user_txet:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    sorted_dict = \
         sorted(word_dict.items(),key=lambda w:w[1],reverse=True)
    return render(request, 'count.html',
                  {'count': totalcount, 'text': user_txet, 'worddict': word_dict,'common':common,'sorted':sorted_dict})
def about(request):
    return render(request, 'about.html')

