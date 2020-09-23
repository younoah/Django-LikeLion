from django.shortcuts import render

# Create your views here.

def index(req):
    return render(req, 'index.html')

def about(req):
    return render(req, 'about.html')

def result(req):
    text = req.GET['fulltext']
    words = text.split()
    word_dict = {}
    for word in words:
        if word in word_dict:
            word_dict[word]+=1
        else:
            word_dict[word] = 1

    return render(req, 'result.html', {'text' : text, 'words_number' : len(words), 'word_dict': word_dict.items})