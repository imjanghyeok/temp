from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog
from .forms import BlogForm


def home(request):
    blogs = Blog.objects.all()
    return render(request,'home.html',{'blogs':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request,'detail.html',{'blog':blog})

def new(request):
    return render(request,'new.html')

def create(request):
    form = BlogForm(request.POST)

    if form.is_valid():
        new_blog = form.save(commit=False)
        new_blog.save()
        return redirect('detail', new_blog.id)

    return render(request, 'new.html')

def edit(request, blog_id):
    edit_blog = get_object_or_404(Blog, pk=blog_id) # print() 해보기
    return render(request, 'edit.html', {'edit_blog':edit_blog})


def update(request, blog_id):
    old_blog = get_object_or_404(Blog, pk=blog_id)
    form = BlogForm(request.POST, instance=old_blog)

   
    if form.is_valid():
        new_blog = form.save(commit=False)
        new_blog.save()
        return redirect('detail', old_blog.id)

    return render(request, 'new.html', {'old_blog':old_blog})


def delete(request, blog_id):
    delete_blog = get_object_or_404(Blog, pk=blog_id)
    delete_blog.delete()
    return redirect('home')


def declaration(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request,'declaration.html', {'blog':blog})

def declare(request, blog_id):
    declare_blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        declare_reason = request.POST.get('dcl')
        declare_causes = ["씨발", "병신", "주민번호", "fuck"]
        for cause in declare_causes:
            print(cause)
            declare_title = Blog.objects.filter(title__contains=cause)
            declare_content = Blog.objects.filter(content__contains=cause)
        return render(request,'warning.html', {'declare_blog':declare_blog}, {'declare_title':declare_title},{'declare_content':declare_content})
    
    else:
        return redirect('home')
    
def search(request):
    searched = request.POST.get('searched')
    print(searched)
    ss = request.POST['searched']
    print(ss)
    search_result = Blog.objects.filter(title__contains=searched)
    print(search_result)
    print(len(search_result))
    if len(search_result) != 0:
        return render(request, 'search.html', {'searched':searched, 'search_result':search_result})
    else:
         return render(request, 'search.html', {'searched':searched})


