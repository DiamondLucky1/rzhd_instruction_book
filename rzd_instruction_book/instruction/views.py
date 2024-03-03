from django.shortcuts import render, get_object_or_404
from polls.models import *
from instruction.models import *
from django.db.models import Q

menu = [{"title": "Инструкции", "url_name": "instruction"},
        {"title": "Электрические и пневмотческие схемы электропоезда", "url_name": "scheme"},
        {"title": "Неисправности электропоезда", "url_name": "malfunctions"},

]

list_of_instruction = Instruction.objects.all()

# def index(request):
#     data = {"title": "Главная",
#             "menu": menu,
#             # "list_of_contents": list_of_instruction,
#     }
#     return render(request, 'instruction/index.html', context=data)


def instruction_page(request):
    topics_test = Test.objects.all()
    # print(topics_test)
    data = {"menu": menu,
            "list_of_instruction": list_of_instruction,
            "title": "Инструкции",
            "topics_test": topics_test
    }


    return render(request, 'instruction/instruction_page.html', context=data)



def instruction_show(request, inst_slug):


    # return HttpResponse(f"Отображение инструкции: {inst_slug}")
    instuction = get_object_or_404(Instruction, slug=inst_slug)
    data = {'title': f'Инструкция по: {instuction.title}',
            'instruction': instuction,
            "menu": menu,
            }
    # print(instuction)
    # print(data)
    return render(request, 'instruction/selection_of_instructions.html', context=data)


def scheme_page(request):

    all_scheme = Sсheme.objects.all()
    # all_scheme = get_object_or_404(Sсheme, slug=)
    data = {"menu": menu,
            "all_scheme": all_scheme
    }
    # print(all_scheme)
    return render(request, 'instruction/choose_scheme.html', context=data)

def scheme_show(request, scheme_slug):
    scheme = get_object_or_404(Sсheme, slug=scheme_slug)
    data = {"title": f'Схема {scheme.name}',
            "scheme": scheme,
    }
    return render(request, 'instruction/show_scheme.html', context=data)


def malfunctions_page(request):
    all_malfunctions = Malfunctions.objects.all()
    data = {"menu": menu,
            "all_malfunctions": all_malfunctions,
    }

    return render(request, 'instruction/choose_malfunction.html', context=data)

def malfunctions_show(request, malfunctions_slug):
    malfunctions = get_object_or_404(Malfunctions, slug=malfunctions_slug)
    data = {
        "title": malfunctions.name,
        "malfunctions": malfunctions,
    }

    return render(request, 'instruction/show_malfunction.html', context=data)



# def search(request):
#     search_query = request.GET.get('search', None)
#     # print(request.GET)
#     if search_query:
#         instruct = Instruction.objects.filter(
#             Q(title__iregex=search_query) | Q(slug__iregex=search_query)
#         )
#     else:
#         return render(request, 'instruction/index.html' )
#
#     if instruct:
#         data = {'instruct': instruct}
#         return render(request, 'instruction/selection_of_instructions.html', context=data)
#     else:
#         return render(request, 'instruction/index.html')


def search(request):
    search_query = request.GET.get('search', None)

    if search_query:
        query_sets = []  # Total QuerySet
        query_sets.append(Instruction.objects.filter(Q(title__iregex=search_query) | Q(slug__iregex=search_query)))
        query_sets.append(Sсheme.objects.filter(Q(name__iregex=search_query) | Q(slug__iregex=search_query)))
        query_sets.append(Malfunctions.objects.filter(Q(name__iregex=search_query) | Q(slug__iregex=search_query)))
        instruct = []
        for item in query_sets:
            if item:
                instruct.append(item)
        print(instruct)
        if instruct:
            data = {'instruct': instruct,
                    'menu': menu}

            return render(request, 'instruction/search.html', context=data)

        else:
            data = {'menu': menu,
                    'answer': f'по вашему запросу ничего не найдено'
                    }
            return render(request, 'instruction/search.html', context=data)


    else:
        data = {'menu': menu,
                'answer': f'по вашему запросу ничего не найдено'
                }
        return render(request, 'instruction/index.html', context=data)