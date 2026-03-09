from django.shortcuts import render,get_object_or_404, redirect
from .models import Post
# Create your views here.
from django.http import HttpResponse
from .forms import PostForm,RegisterForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages

# def index(request):
#     print("Hello this is django server ")
#     return HttpResponse("This is a django line")
@login_required
def home_page(request):
    posts = Post.objects.all().order_by('-id')

    paginator=Paginator(posts,2)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    return render(request, "index.html", {"page_obj": page_obj})




def about_page(request):
    return render(request,'about.html')


def post_details(request,id):
    post=get_object_or_404(Post,id=id)
    return render(request,"post_details.html",{'post':post})

@login_required
def create_post(request):
    if request.method=="POST":
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user

            post.save()
            print(request.FILES)
            messages.success(request,"Post created successfully! ")

            return redirect('index')
    else:
        form=PostForm()
    return render(request,"create_post.html",{'form':form})


def update_post(request,id):
    post=get_object_or_404(Post,id=id)
    if request.method=="POST":
        form=PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            messages.success(request,"Post update successfully")
            return redirect('index')
    else:
        form=PostForm(instance=post)

    return render(request,"edit_post.html",{'form':form})


def delete_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == "POST":
        post.delete()
        messages.success(request,"Post delete successfully ! ")
        return redirect('index')

    return render(request, "delete_confirm.html", {"post": post})


def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=RegisterForm()
    
    return render(request, 'registration/register.html', {'form': form})


def search(request):
    query = request.GET.get('query', '')

    if query != "":
        posts = Post.objects.filter(Title__icontains=query)
    else:
        posts = Post.objects.none()

    return render(request, 'search.html', {'posts': posts, 'query': query})


    # return HttpResponse("This is a search ")

