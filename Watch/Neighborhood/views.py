from .forms import UserProfileForm,NeighborhoodForm,PostForm,BusinessForm,ServiceForm
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile,Neighborhood,Business,Post,Services
from django.http import Http404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

# Create your views here.
@login_required(login_url='/accounts/login/')
def update_profile(request):
    '''
    function to update the profile form
    '''
    title="Neighborhood | Profile Edit "
    current_user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user=current_user
            if UserProfile.objects.filter(user_id=current_user.id).exists():
                UserProfile.objects.filter(user_id=current_user.id).delete()
            profile.save()
            return redirect('/')

    else:
        form = UserProfileForm()

    return render(request, 'editprofile.html', {"title":title,"form": form})

@login_required(login_url='/accounts/login/')
def profile(request,id):
    '''
    function to display the user profile
    '''
    current_user = request.user
    current_user.id = request.user.id
    current_profile = UserProfile.objects.get(user_id = current_user.id)
    try:
        profile = UserProfile.objects.get(user_id = current_user.id)
        

        return render(request, 'profile.html', {"profile":profile,"id":current_user.id})


    except ValueError:
        raise Http404()

def neighborhood(request):
    '''
    function to fill the neighborhood form
    '''
    current_user = request.user
    try:
        if request.method == 'POST':
            form = NeighborhoodForm(request.POST,request.FILES)
            if form.is_valid():
                neighborhood = form.save(commit = False)
                neighborhood.user = current_user
                neighborhood.save()
            return redirect('/profile')
        else:
            form = NeighborhoodForm()

    except ValueError:
        Http404
    return render(request,'neighborhood.html',{"form":form,})

def index(request):
    neighborhood = Neighborhood.objects.all()
    return render(request,'index.html',{"neighborhood":neighborhood})

def landing(request):
    return render(request,'landing.html')

def post(request):
    '''
    function to create a new post
    '''
    current_user = request.user
    try:
        if request.method == 'POST':
            form = PostForm(request.POST,request.FILES)
            if form.is_valid():
                post = form.save(commit = False)
                post.user = current_user
                post.save()
            return redirect('/viewpost')
        else:
            form = PostForm()

    except ValueError:
        Http404
    return render(request,'post.html',{"form":form,})

def viewPost(request):
    '''
    function to view posts
    '''
    posts= Post.objects.all()
    return render(request,'viewpost.html',{"posts":posts})

def business(request):
    '''
    function to create a new business
    '''
    current_user = request.user
    try:
        if request.method == 'POST':
            form = BusinessForm(request.POST,request.FILES)
            if form.is_valid():
                post = form.save(commit = False)
                post.user = current_user
                post.save()
            return redirect('/viewbusiness')
        else:
            form = BusinessForm()

    except ValueError:
        Http404
    return render(request,'business.html',{"form":form,})

def viewBusiness(request):
    '''
    function to view business
    '''
    business = Business.objects.all()
    return render(request,'viewbusiness.html',{"business":business})

def services(request):
    '''
    function to create a new business
    '''
    current_user = request.user
    try:
        if request.method == 'POST':
            form = ServiceForm(request.POST,request.FILES)
            if form.is_valid():
                post = form.save(commit = False)
                post.user = current_user
                post.save()
            return redirect('/viewservices')
        else:
            form = ServiceForm()

    except ValueError:
        Http404
    return render(request,'services.html',{"form":form,})

def viewServices(request):
    '''
    function to view business
    '''
    services = Services.objects.all()
    return render(request,'viewservices.html',{"services":services})

def search_business(request):
    '''
    function to search by business name
    '''
    if 'name' in request.GET and request.GET["name"]:
        searched_business = request.GET.get("name")
        business = Business.search_business(searched_business)
        message = f"{searched_business}"

        return render(request, 'search.html', {"message": message, "business":business})

    else:
        message = "Sorry, No one by this username"
        return render(request, 'search.html', {"message": message})

