from django.contrib.auth import login # 追加
from django.contrib.auth.forms import UserCreationForm # 追加
from django.shortcuts import render, redirect ,resolve_url,get_object_or_404# redirectをインポート
from django.contrib.auth.decorators import login_required # 追加
from django.contrib.auth.models import User # 追加
from .models import Card
from django.views.generic import DetailView , UpdateView,CreateView ,ListView,DeleteView# 追加
from .mixins import OnlyYouMixin
from django.contrib.auth.mixins import LoginRequiredMixin # 追加
from .forms import UserForm,CardForm # 追加
from django.http import HttpResponse
from django.urls import reverse_lazy


def index(request):
    return render(request,"youtubedevice/index.html")

@login_required # 追加
def home(request):
    return render(request,"youtubedevice/home.html")

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user_instance = form.save()
            login(request,user_instance)
            return redirect('YoutubeDevice:home')
    else:
        form = UserCreationForm()
    
    context = {
        "form":form
    }
    return render(request,'youtubedevice/signup.html',context)

class UserDetailView(DetailView):
    model = User
    template_name = "youtubedevice/users/detail.html"
    form_class = UserForm

    def get_success_url(self):
        return resolve_url('YoutubeDevice:users_detail',pk=self.kwargs['pk'])

class UserUpdateView(OnlyYouMixin,UpdateView):
    model = User
    template_name = "youtubedevice/users/update.html"
    form_class = UserForm

    def get_success_url(self):
        return resolve_url('YoutubeDevice:users_detail',pk=self.kwargs['pk'])

class CardCreateView(LoginRequiredMixin,CreateView):
    model = Card
    template_name = "youtubedevice/cards/create.html"
    form_class = CardForm
    success_url = reverse_lazy("YoutubeDevice:cards_list")

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CardListView(ListView):
    model = Card
    template_name = "youtubedevice/cards/list.html"


class CardDetailView(DetailView):
    model = Card
    template_name = "youtubedevice/cards/detail.html"



class CardUpdateView(LoginRequiredMixin,UpdateView):
    model = Card
    template_name = "youtubedevice/cards/update.html"
    form_class = CardForm

    def get_success_url(self):
        return resolve_url('YoutubeDevice:cards_detail',pk=self.kwargs['pk'])

class CardDeleteView(LoginRequiredMixin,DeleteView):
    model = Card
    template_name = "youtubedevice/cards/delete.html"
    form_class = CardForm
    success_url = reverse_lazy("YoutubeDevice:cards_list")