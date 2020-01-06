from django.shortcuts import render
from .models import MyProfile, MyPost, PostLike, PostComment, FollowUser
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http.response import HttpResponseRedirect
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = "social/home.html"


class AboutView(TemplateView):
    template_name = "social/about.html"


class ContactView(TemplateView):
    template_name = "social/contact.html"


# @method_decorator(login_required, name='dispatch')
# class NoticeListView(ListView):
#     model = Notice
#
#     def get_queryset(self):
#         si = self.request.GET.get('si')
#         if si == None:
#             si = ""
#         if self.request.user.is_superuser:
#             return Notice.objects.filter(Q(subject__icontains = si) | Q(msg__icontains = si)).order_by("-id")
#         else:
#             return Notice.objects.filter(Q(branch=self.request.user.profile.branch)|Q(branch__isnull=True))\
#                 .filter(Q(subject__icontains = si) | Q(msg__icontains = si)).order_by("-id")
#
#
# @method_decorator(login_required, name='dispatch')
# class NoticeDetailView(DetailView):
#     model = Notice
#
#
# @method_decorator(login_required, name='dispatch')
# class ProfileUpdateView(UpdateView):
#     model = Profile
#     fields = ["branch", "sem", "marks_10", "marks_12", "marks_aggr", "myimg", "myresume", "skills", "rn"]
#
#
# @method_decorator(login_required, name='dispatch')
# class QuestionCreate(CreateView):
#     model = Question
#     fields = ["subject", "msg"]
#
#     def form_valid(self, form):
#         self.object = form.save()
#         self.object.user = self.request.user
#         self.object.save()
#         return HttpResponseRedirect(self.get_success_url())
#
#
# @method_decorator(login_required, name='dispatch')
# class MyList(TemplateView):
#     template_name = "college/mylist.html"
#
#     def get_context_data(self, **kwargs):
#         context = TemplateView.get_context_data(self, **kwargs)
#         context["notices"] = Notice.objects.order_by("-id")[:3]
#         context["questions"] = Question.objects.order_by("-id")[:3]
#         return context;