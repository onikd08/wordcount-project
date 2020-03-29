from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request,'home.html')

def helppage(request):
    return render(request,'help.html')

def aboutpage(request):
    return render(request, 'about.html')

def countwords(request):
    input_text = request.GET['input_text']
    # define punctuation
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    text_without_punc = ""

    if input_text != "":
        for char in input_text:
            if char not in punctuations:
                text_without_punc = text_without_punc+char

        word_list = text_without_punc.split()

        # make all lower case
        converted_list = [x.lower() for x in word_list]
        number_of_words = len(word_list)

        word_counter_dict = {}
        for word in converted_list:
            if word in word_counter_dict:
                word_counter_dict[word] += 1
            else:
                word_counter_dict[word] = 1

        #  getting maximum appeared words.
        max_word_dict = {}
        max_value = max(word_counter_dict.values())
        for keys, values in word_counter_dict.items():
            if values == max_value:
                #print(keys)
                max_word_dict[keys] = values
        sorted_max_word_list = sorted(max_word_dict.items())
        sorted_word_list = sorted(word_counter_dict.items())
        return render(request, 'count.html', {'input_text':input_text, 'total_words':number_of_words, 'max_words':sorted_max_word_list,'word_count':sorted_word_list})

    else:
        return render(request, "home.html")
