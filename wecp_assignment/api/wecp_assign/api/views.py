from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import pycode_similar

# Create your views here.

@csrf_exempt 
def show(request):
	if request.method == "POST":
	    file1 = request.FILES['file1']
	    file2 = request.FILES['file2']
	    handle_file1(file1)
	    handle_file2(file2)
	    f1 = open('./api/source_code.txt','r')
	    f2 = open('./api/reference_code.txt','r')
	    results = pycode_similar.detect([f1.read(),f2.read()])
	    result = 0

	    for index, func_ast_diff_list in results:
	    	sum_total_count = sum(func_diff_info.total_count for func_diff_info in func_ast_diff_list)
	    	sum_plagiarism_count = sum(func_diff_info.plagiarism_count for func_diff_info in func_ast_diff_list)
	    	result = ('{:.2f} % ({}/{}) of ref code structure is plagiarized by candidate.'.format(sum_plagiarism_count / float(sum_total_count) * 100,sum_plagiarism_count,sum_total_count))

	    return JsonResponse({'results':str(result)})

def handle_file1(f):
    with open('./api/source_code.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def handle_file2(f):
    with open('./api/reference_code.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
