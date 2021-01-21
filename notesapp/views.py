from django.shortcuts import render , redirect
from django.views.generic import  ListView ,View , DetailView , TemplateView
from django.views.generic.edit import UpdateView
from .models import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import  authenticate ,login ,logout
from django.db.models import Q

#------------------------------------------------ start Word ----------------------------------

class Home(TemplateView):
    template_name = 'main/home.html'


class Header(TemplateView):
    template_name = 'main/hader.html'



class About(TemplateView):
    template_name = 'main/about.html'


class UserRegistation(View):
    def get(self,request):
        form = UserRegistationForm()
        data = {"form":form }
        return render(request, 'main/signup.html', data)

    def post(self,request):
        form = UserRegistationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('login')



class Login(View):
    def get(self,request):
        return render(request, 'main/home.html')

    def post(self,request):
        username = request.POST.get('email')
        password = request.POST.get('password')

        try:
            username = User.objects.get(email = username)
            user = authenticate(username=username.username, password=password)
        except:
            return redirect('login')

        if user is not None:
            login(request,user)
            userdetail = UserDetail.objects.filter(user=request.user).count()

            if (userdetail == 1):
                return redirect('profile')
            else:
                return redirect('adduserprofile')
        return render(request,'main/home.html')


class Logout(View):
    def get(self,request):
        logout(request)
        return render(request,'main/hader.html')



class AddUserProfile(LoginRequiredMixin,View):
    def get(self,request):
        form = AddProfileDetailForm()
        data = {"forms":form}
        return render(request, 'main/addprofiledetal.html', data)
    def post(self,request):
        form = AddProfileDetailForm(request.POST or None , request.FILES or None)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            return redirect('profile')



class Profile(LoginRequiredMixin,View):
    def get(self,request,*args,**kwargs):
        data = {"profile":UserDetail.objects.get(user = request.user)}
        return render(request, 'users/profile.html',data)



class AllUser(LoginRequiredMixin,ListView):
    model = UserDetail
    template_name = 'users/all_user.html'
    context_object_name = 'alluser'



class SendNote(LoginRequiredMixin,View):
    def get(self,request,pk):
        form = NoteForm()
        data = {"forms":form ,"pk":pk}
        return render(request, 'users/sand_note_form.html', data)

    def post(self,request,pk):
        user = UserDetail.objects.get(user = request.user).ud_id
        form = NoteForm(request.POST or None , request.FILES or None)
        if form.is_valid():
            f = form.save(commit=False)
            f.sender_id = UserDetail(user)
            f.reciver_id = UserDetail(pk)
            f.save()
            return redirect('allsendnote')
        return render(request,'users/profile.html')



class AllSandNotes(LoginRequiredMixin,View):
    def get(self,request):
        data = NoteShare.objects.filter(sender_id__user = request.user)
        context = {"sendnote":data}
        return render(request,'users/all_sand_notes.html',context)



class AllReviedNotes(LoginRequiredMixin,View):
    def get(self,request):
        data  = NoteShare.objects.filter(reciver_id__user = request.user)
        return render(request,'users/all_recived_notes.html',{"recivednote":data})



class SearchFirend(LoginRequiredMixin,View):
    def get(self,request):
        id = request.GET.get('search')

        try:
            data = int(id)
        except:
            return redirect('alluser')

        data = UserDetail.objects.filter(ud_id = id)
        return render(request,'users/all_user.html',{"alluser":data })



class SearchReciver(LoginRequiredMixin,View):
    def get(self, request):
        search = request.GET.get('search')
        cond = Q(Q(title__icontains=search)|Q(sender_id__name__icontains = search)) & Q(reciver_id__user = request.user)
        data = NoteShare.objects.filter(cond)
        return render(request, 'users/all_recived_notes.html', {"recivednote": data})


class ProfileUpdate(LoginRequiredMixin,UpdateView):
    model = UserDetail
    form_class = AddProfileDetailForm
    template_name = 'users/profileupdate.html'

    def form_valid(self, form):
        form.save()
        return redirect('profile')






