from django.shortcuts import render,redirect
from accounts.forms import RegistrationForm,EditProfileForm,TravForm
from accounts.models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView,View,DeleteView
from django.urls import reverse_lazy
# Create your views here.
# def home(request):
#     numbers = [1,2,3,4,5]
#     name = "Abhishek Nautiyal"
#
#     args = {'myname': name,'numbers': numbers}
#     return render(request,'accounts/home.html',args)

def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:home')
        else:
            args = {'form': form,}
            return render(request, 'accounts/reg_form.html',args)
    else:
        form = RegistrationForm()

        args = {'form': form,}
        return render(request, 'accounts/reg_form.html',args)


@login_required
def view_profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('accounts:view_profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect( 'login')
        else:
            return redirect('/account/change-password')
    else:
        form = PasswordChangeForm(request.user)
        args = {'form': form,}
        return render(request, 'accounts/change_password.html', args)


def HomeView(request):
    template_name = 'accounts/home.html'

    if request.method == 'POST':
        form = TravForm(request.POST)
        if form.is_valid():

            post = form.save(commit=False)
            post.fir = request.user
            post.save()
                # text = form.cleaned_data['post']
                # form = TravForm()
            return redirect('accounts:home')
        else:
            form = TravForm()
            args = {'form': form,}
            return redirect('accounts:view_profile')

    else:
        form = TravForm()
        args = {'form': form,}
        return render(request,'accounts/home.html',args)
    # form_class=TravForm
    # template_name = 'accounts/home.html'

    # def get(self,request):
    #     form = self.form_class(None)
    #     posts = Post.objects.all()
    #     args = {'form':form,'posts':posts}
    #     return render(request,self.template_name,args)
    #
    # def post(self,request):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         user1 = form.save(commit=False)
    #
    #         route = form.cleaned_data['route']
    #         date = form.cleaned_data['date']
    #         time = form.cleaned_data['time']
    #         phone_no = form.cleaned_data['phone_no']
    #         fir = request.user.username
    #         user1.save()
    #
    #         form = self.form_class()
    #         return redirect('accounts:home')
    #
    #     args = {'form': form,}
    #     return render(request,self.template_name,{'form': form,})

# def remove_items(request):
#     if request.method == 'POST':
#         form = TravForm()
#         posti = Post.objects.all()
#         item_id = (request.POST.get('item_id'))
#         item = Post.objects.get(id=item_id)
#         item.delete()
#         return render(request,'accounts/soh.html',{'posti':posti,})

class tasdelevie(DeleteView):
    model = Post
    template_name = 'accounts/delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('accounts:showall')

def showall(request):


    posts = Post.objects.all().order_by('-created')
    ans = request.user
    curuser = Post.objects.filter(fir=request.user)
    # curuser = list(curuser)

    notcuruser = Post.objects.exclude(fir=request.user)
    # notcuruser = list(notcuruser)
    # valid_data = list()
    # for x in curuser:
    #     for y in notcuruser:
    #         g = list()
    #         if x.route==y.route and x.date==y.date:
    #              g=g+y
    #     valid_data= valid_data + (g)


    args = {'posts':posts,'curuser':curuser,'notcuruser':notcuruser}
    return render(request,'accounts/soh.html',args)
