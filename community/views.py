from django.shortcuts import render, redirect
from community.forms import *

# Create your views here.
def write(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Form()

    return render(request, 'write.html',{'form':form})

def board_list(request):
    boardList = MainBoard.objects.all()
    return render(request,'BoardListView.html',{'boardList':boardList})

def view(request, num="1"):
    board = MainBoard.objects.get(id=num)
    return render(request,'view.html',{'board':board})

def delete(request, blog_id):
    blog = MainBoard.objects.get(id=blog_id)
    blog.delete()
    return redirect('/board_list')