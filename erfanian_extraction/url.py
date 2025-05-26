from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about-us',views.about_us,name='about-us'),
    path('services-1',views.services_1,name='services-1'),
    path('carpet-rugs',views.carpet_rugs,name='carpets-rugs'),
    # path('our-history',views.our_history,name='our-history'),
    path('our-team',views.our_team,name='our-team'),
    path('our-blog',views.our_blog,name='our-blog'),
    path('contact-us',views.contact_us,name='contact-us'),
    path('portfolio-single',views.portfolio_single,name='portfolio-single'),
    
]