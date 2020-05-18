from django.shortcuts import render, redirect


def index(request):
    if request.method == 'POST':
        text = request.POST['fulltext']
        lexicon = {}

        text = text.lower()
        chars_to_remove = ['\n', '.', ':', '-', ',', '\'', '…']
        word_list = text.split()

        for i in range(len(word_list)):
            for letter in word_list[i]:
                if letter in chars_to_remove:
                    print(letter, True)
                    word_list[i] = word_list[i].replace(letter, '')

        for word in word_list:
            if word in lexicon:
                lexicon[word] += 1
            else:
                lexicon[word] = 1

        count = len(word_list)

        new_lexicon = sorted(lexicon.items(), key=lambda x: x[1], reverse=True)

        context = {
            'words': text,
            'count': count,
            'lexicon': new_lexicon,
        }
        return render(request, 'index.html', context)
    return render(request, 'index.html')
