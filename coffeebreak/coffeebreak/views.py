from django.shortcuts import render_to_response
from admin.models import my_menu,my_pages,my_constant
from django.core.paginator import Paginator
import urllib2

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
   Ref_pointer={}
   for page in my_pages.objects.all().order_by('date'):
     if str(page.my_menu) in offset:
       if page.Topic_In_Depth:
         Pages.append({page.Topic_Detail:'True'})
         Ref_pointer[page.Topic_Detail]=page.Topic_Header
       else:
         Pages.append({page.Topic_Detail:'False'})
   return Ref_pointer,Pages

def Manage_Detail_Pages(offset,detail_topic):
   Pages = []
   Disqus_status=""
   for page in my_pages.objects.all().order_by('date'):
      if str(page.my_menu) in offset:
         if str(page.Topic_Header) == detail_topic:
           Pages.append({page.Topic_Detail:page.Topic_In_Depth})
           Disqus_status=str(page.disqus_status)
   return Disqus_status,Pages

def Home(request,offset):
   header,footer,Slogan,Title,BASE_SITE = Manage_const()
   Pages=[]
   bread_crumbs=[]
   menu,icons,status=Manage_menu()
   Ref_pointer,Pages=Manage_pages(offset)
   paginator=Paginator(Pages,5)
   try:
     page = int(request.GET.get("page", '1'))
   except ValueError:
     page=1
   try:
     Pages = paginator.page(page)
   except (InvalidPage,EmptyPage):
     Pages = paginator.page(paginator.num_pages)
   return render_to_response('home.html',locals())

def Detail(request,offset,detail_topic):
   header,footer,Slogan,Title,BASE_SITE = Manage_const()
   Detail_Pages=[]
   bread_crumbs=[]
   menu,icons,status=Manage_menu()
   bread_crumbs.append({offset:offset + "/"})
   bread_crumbs.append({detail_topic:offset +"/"+ detail_topic})
   Disqus_status,Detail_Pages=Manage_Detail_Pages(offset,detail_topic)
   print Disqus_status
   return render_to_response('detail_pages.html',locals())
