from django.http import HttpResponseRedirect
from django.core.cache import cache
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.simple import direct_to_template
from django.db.models import get_app, get_models
from admin.forms import CreateMenuForm,CreatemypagesForm,CreateConstForm
from admin.models import my_menu,my_pages,my_constant
from django.core.mail import send_mail

def Manage_const():
   header=""
   footer=""
   Slogan=""
   Title=""
   basesite=""
   for const in my_constant.objects.all().order_by('date'):
     header = const.header
     footer = const.footer
     Slogan = const.page_note
     Title = const.page_title
     basesite = const.base_site
   return header,footer,Slogan,Title,basesite

def Manage_menu():
   Menu = []
   Menu_Icons = {}
   Menu_Status = {}
   for menu in my_menu.objects.all().order_by('date'):
      Menu.append({menu.menu:menu.menu_link})
      Menu_Icons[menu.menu]=menu.menu_icons
      Menu_Status[menu.menu]=menu.menu_status
   return Menu,Menu_Icons,Menu_Status

def Manage_pages(offset):
   Pages = []
   for page in my_pages.objects.filter(Ref_Page=offset).order_by('date'):
      Pages.append({page.Topic_Header:page.Topic_Detail})
   return Pages

def create_new_user(request):
    bread_crumbs=[]
    header,footer,Slogan,Title,BASE_SITE = Manage_const()
    if request.method == 'POST':
      form = UserCreationForm(request.POST)
      if form.is_valid():
        user = form.save(commit=False)
        user.is_active = True
        user.save()
        return HttpResponseRedirect('/accounts/login/')
      else:
        return render_to_response('user_create_form.html',locals())
    else:
      form = UserCreationForm()
      return render_to_response('user_create_form.html',locals())

def menu_admin(request):
  bread_crumbs=[]
  menu,icons,status=Manage_menu()
  header,footer,Slogan,Title,BASE_SITE = Manage_const()
  bread_crumbs.append({"Admin":"admin/config"})
  bread_crumbs.append({"Menu Administration":"admin/my_menu/"})
  if request.method == 'POST':
    if request.user.is_authenticated():
      user = User.objects.get(username = request.user)
      if user.is_superuser:
        form = CreateMenuForm(request.POST)
        if form.is_valid():
          try:
             menu=form.save(commit=False)
             menu.save()
             return HttpResponseRedirect('/admin/my_menu/')
          except ValueError:
             return HttpResponsRedirect('/admin/my_menu/')
        else:
          return render_to_response('menu_form.html',locals())
      else:
        return HttpResponseRedirect('/accounts/login/')
    else:
      Failure_Flag = 1
      Message = "User authentication failed."
      form = UserCreationForm()
      return render_to_response('user_create_form.html',locals())
  else:
    form = CreateMenuForm()
    return render_to_response('menu_form.html',locals())

def page_admin(request):
  bread_crumbs=[]
  menu,icons,status=Manage_menu()
  bread_crumbs.append({"Admin":"admin/config"})
  bread_crumbs.append({"WebPage Administration":"admin/my_pages/"})
  header,footer,Slogan,Title,BASE_SITE = Manage_const()
  if request.method == 'POST':
    if request.user.is_authenticated():
      user = User.objects.get(username = request.user)
      if user.is_superuser:
        form = CreatemypagesForm(request.POST)
        if form.is_valid():
          try:
             menu=form.save(commit=False)
             menu.save()
 #            send_mail('Subject', 'Details/Content of Email', 'From_address',['To_address'], fail_silently=False)
             return HttpResponseRedirect('/admin/my_pages/')
          except ValueError:
             return HttpResponsRedirect('/admin/my_pages/')
        else:
          return render_to_response('page_form.html',locals())
      else:
        Message = user + 'is not authenticated to login here.'
        return HttpResponseRedirect('/accounts/login/')
    else:
      form = UserCreationForm()
      Message = "User authentication failed."
      return render_to_response('user_create_form.html',locals())
  else:
    form = CreatemypagesForm()
    return render_to_response('page_form.html',locals())

def const_admin(request):
  bread_crumbs=[]
  menu,icons,status=Manage_menu()
  bread_crumbs.append({"Admin":"admin/config"})
  bread_crumbs.append({"Site Constants Administration":"admin/my_constant/"})
  header,footer,Slogan,Title,BASE_SITE = Manage_const()
  if request.method == 'POST':
    if request.user.is_authenticated():
      user = User.objects.get(username = request.user)
      if user.is_superuser:
        form = CreateConstForm(request.POST)
        if form.is_valid():
          try:
             const=form.save(commit=False)
             const.save()
             return HttpResponseRedirect('/admin/my_constant/')
          except ValueError:
             return HttpResponsRedirect('/admin/my_constant/')
        else:
          return render_to_response('const_form.html',locals())
      else:
        Message = str(user) + 'is not authenticated to login here.'
        return HttpResponseRedirect('/accounts/login/')
    else:
      Message = "User authentication failed."
      form = UserCreationForm()
      return render_to_response('user_create_form.html',locals())
  else:
    form = CreateConstForm()
    return render_to_response('const_form.html',locals())

def admin(request):
   bread_crumbs=[]
   menu,icons,status=Manage_menu()
   header,footer,Slogan,Title,BASE_SITE = Manage_const()
   Models=[]
   if request.method == 'GET':
     if request.user.is_authenticated():
       user = User.objects.get(username = request.user)
       if user.is_superuser:
         app = get_app('admin')
         for model in get_models(app):
           detail ="%s" %(model._meta.verbose_name)
           Models.append(detail)
         return render_to_response('admin_site.html',locals())
       else:
        Message = str(user) + 'is not authenticated to login here.'
        return HttpResponseRedirect('/accounts/login/')
     else:
        form = UserCreationForm()
        Message = "User authentication failed."
        return render_to_response('user_create_form.html',locals())
   else:
     return HttpResponseRedirect('/accounts/login/')

