from email.mime import image
from pyexpat import model
from tabnanny import verbose
from unicodedata import category
from django.db import models

# Create your models here.

class Home(models.Model):
    description = models.TextField(max_length=100,null=False)

    class Meta:
        verbose_name_plural = 'Home'
        
    def __str__(self):
        return self.description

class HomeServices(models.Model):
    home_services_card_name = models.CharField(max_length=50,null=False)
    home_services_card_description = models.CharField(max_length=250,null=False)

    class Meta:
        verbose_name_plural = 'Home Services'

    def __str__(self):
        return self.home_services_card_name

class HomeDiscover(models.Model):
    home_discover_name = models.CharField(max_length=50,)
    home_discover_role = models.CharField(max_length=50,)
    home_discover_image = models.ImageField(upload_to='media')

    class Meta:
        verbose_name_plural = 'Home Discoveries'

    def __str__(self):
        return f"{self.home_discover_name} | {self.home_discover_role}"

class HomeBlog(models.Model):
    home_blog_role = models.CharField(max_length=50)
    home_blog_image = models.ImageField(upload_to='media')
    home_blog_description = models.TextField(max_length=200)

    class Meta:
        verbose_name_plural = 'Home Blogs'

    def __str__(self):
        return self.home_blog_role
    
    
class AboutUs(models.Model):
    about_blog_name = models.CharField(max_length=100)
    about_blog_image = models.ImageField(upload_to='media')
    about_blog_description = models.TextField(max_length=200)

    class Meta:
        verbose_name_plural = 'About Us'

    def __str__(self):
        return self.about_blog_name
    
class AboutUsProjects(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to="media")
    
    def __str__(self) -> str:
        return f"{self.name} | {self.category}"
    
    class Meta:
        verbose_name_plural = 'About Our Projects'

class Services(models.Model):
    services_service_name = models.CharField(max_length=100)
    services_service_description = models.TextField(max_length=200)

    class Meta:
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.services_service_name

class ServicesGallery(models.Model):
    services_gallery_image = models.ImageField(upload_to='media')

    class Meta:
        verbose_name_plural = 'Services Gallary'
    

class Our_Team(models.Model):
    team_image = models.ImageField(upload_to='media')
    team_name = models.CharField(max_length=50)
    team_role = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Our Teams'

    def __str__(self):
        return f"{self.team_name} | {self.team_role}"
    
class Portfolio(models.Model):
    portfolio_image = models.ImageField(upload_to = 'media')
    portfolio_name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Porfolios'

    def __str__(self):
        return self.portfolio_name  
    

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    user_email = models.CharField(max_length=150,null=False)
    phone_number = models.CharField(max_length=15,null=False)
    project_scope = models.CharField(max_length=150)
    message = models.TextField(max_length=300,null=False)
    
    def __str__(self):
        return f"{self.name} | {self.user_email} | {self.phone_number}"
    
    class Meta:
        verbose_name_plural = 'Contact Us'