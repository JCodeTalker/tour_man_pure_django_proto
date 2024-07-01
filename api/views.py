from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .models import DecksModel
from .forms import DecksForm, NewUserForm, UpdateUserForm, ImageForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def image_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/list')
    else:
        form = ImageForm()
    return render(request, 'image_upload.html', {'form': form})

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		
		if form.is_valid():
			print('redirecting')
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/list")
		else:
			print('form is not valid')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})


@login_required
def update_profile(request):
    print('update call')
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        print(user_form.is_valid())
        if user_form.is_valid(): 
            user_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('/list')
    else:
        user_form = UpdateUserForm(instance=request.user)
    return render(request, 'update_view.html', {
        'form': user_form,
    })


def user_detail_view(request):
    context ={}
    data = DecksModel.objects.get(id = 7)
    current_user = request.user
    context["data"] = User.objects.get(id=current_user.id)
    print(context["data"].email)
         
    return render(request, "user_detail_view.html", context)


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/list")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("/list")

def create_deck(request):
	context ={}
	if request.method == 'POST':
		form = DecksForm(request.POST, request.FILES or None)
		if form.is_valid():
			deck = form.save(commit=False)
			deck.owner = request.user
			deck.save()
			return redirect("/list")
	else:
		form = DecksForm(None)
			
	context['form']= form
	return render(request, "create_deck.html", context={"register_form":form})


def list_view(request):
    context ={}
    print('list view call')
    context["dataset"] = DecksModel.objects.all()
    return render(request, "list_view.html", context)


def detail_view(request, id):
    context ={}
    context["data"] = DecksModel.objects.get(id = id)
    return render(request, "detail_view.html", context)


def update_view(request, id):
    print("update call")
    context ={}
    obj = get_object_or_404(DecksModel, id = id)
 
    form = DecksForm(request.POST or None, instance = obj)   
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+str(id)+"/detail")
 
    context["form"] = form
    print(form.is_valid())
    return render(request, "update_view.html", context)


def update_user(request, id):
    context ={}
    obj = get_object_or_404(DecksModel, id = id)
    form = DecksForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
    context["form"] = form
    return render(request, "update_view.html", context)


def delete_view(request, id):
    context ={}
    obj = get_object_or_404(DecksModel, id = id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/list")
    return render(request, "delete_view.html", context)



def delete_user_view(request):
    context ={}
    obj = get_object_or_404(User, id = request.user.id)
    if request.method == "POST":
        logout(request)
        obj.delete()
        return HttpResponseRedirect("/list")
    return render(request, "delete_view.html", context)