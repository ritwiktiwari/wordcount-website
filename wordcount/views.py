from django.shortcuts import render, redirect


def index(request):
    if request.method == 'POST':
        words = request.POST['fulltext']
        word_list = words.split()
        count = len(word_list)
        lexicon = {}
        for word in word_list:
            if word in lexicon:
                lexicon[word] += 1
            else:
                lexicon[word] = 1
        context = {
            'words': words,
            'count': count,
            'lexicon': list(lexicon.items()),
        }
        return render(request, 'index.html', context)
    return render(request, 'index.html')
