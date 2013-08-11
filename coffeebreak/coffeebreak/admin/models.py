from django.db import models

Status = (
       ('active','Active'),
       ('#','In-Active'),
)

Icons = (
       ('foundicon-thumbup','foundicon-thumbup'),
       ('foundicon-thumbdown','foundicon-thumbdown'),
       ('foundicon-rss','foundicon-rss'),
       ('foundicon-facebook','foundicon-facebook'),
       ('foundicon-twitter','foundicon-twitter'),
       ('foundicon-pinterest','foundicon-pinterest'),
       ('foundicon-github','foundicon-github'),
       ('foundicon-path','foundicon-path'),
       ('foundicon-linkedin','foundicon-linkedin'),
       ('foundicon-dribble','foundicon-dribble'),
       ('foundicon-stumble-upon','foundicon-stumble-upon'),
       ('foundicon-behance','foundicon-behance'),
       ('foundicon-reddit','foundicon-reddit'),
       ('foundicon-google-plus','foundicon-google-plus'),
       ('foundicon-youtube','foundicon-youtube'),
       ('foundicon-vimeo','foundicon-vimeo'),
       ('foundicon-clickr','foundicon-clickr'),
       ('foundicon-slideshare','foundicon-slideshare'),
       ('foundicon-picassa','foundicon-picassa'),
       ('foundicon-skype','foundicon-skype'),
       ('foundicon-instagram','foundicon-instagram'),
       ('foundicon-foursquare','foundicon-foursquare'),
       ('foundicon-delicious','foundicon-delicious'),
       ('foundicon-chat','foundicon-chat'),
       ('foundicon-torso','foundicon-torso'),
       ('foundicon-tumblr','foundicon-tumblr'),
       ('foundicon-video-chat','foundicon-video-chat'),
       ('foundicon-digg','foundicon-digg'),
       ('foundicon-wordpress','foundicon-wordpress'),
)

Disqus = (
       ('On','On'),
       ('Off','Off'),
)

class my_constant(models.Model):
   header = models.CharField(max_length=100)
   footer = models.CharField(max_length=100)
   page_title = models.CharField(max_length=100) 
   page_note = models.CharField(max_length=100,blank=True)
   base_site = models.URLField(max_length=100)
   date = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return "%s" %(self.header)

class my_menu(models.Model):
   menu = models.CharField(max_length=50,primary_key=True)
   menu_link = models.URLField(max_length=200)
   menu_status = models.CharField('Status',max_length=10,choices=Status,blank=True)
   menu_icons = models.CharField('Icons',max_length=50,choices=Icons,blank=True)
   date = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return "%s" %(self.menu.lower())

class my_pages(models.Model):
   my_menu = models.ForeignKey(my_menu)
   Topic_Header = models.CharField('Header',max_length=55)
   Topic_Detail = models.TextField('Detail',max_length=2000)
   Topic_In_Depth = models.TextField('Detail',max_length=10000,blank=True)
   disqus_status = models.CharField('Status',max_length=10,choices=Disqus,blank=True)
   date = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return "%s" %(self.my_menu)
