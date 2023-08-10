from django.urls import path
#let import views.py from 'myapp' Application
from myapp import views
urlpatterns = [
    #preparing to write urls the application will use to manage.
    path('index/',views.index,name='index'),
    path('about/',views.about,name='about')
]












'''
In this Django `urlpatterns` configuration, we are setting up URL patterns for the application using the `path` function from `django.urls`. Let's break down each part and its purpose:

1. `from django.urls import path`
   - This line imports the `path` function from `django.urls`. 
   The `path` function is used to define URL patterns and map them to corresponding view functions.

2. `from myapp import views`
   - This line imports the `views.py` module from the `myapp` application. 
   It assumes that there is an application named `myapp` within the Django project, and the `views.py` file in that application contains the view functions for handling these URL patterns.

3. `urlpatterns = [ ... ]`
   - This is a list called `urlpatterns` that holds the URL patterns for the application. 
   Each element of this list represents a URL pattern along with its associated view function.

4. `path('index/', views.index, name='index')`
   - This line defines a URL pattern for the path `/index/`. 
   When a user accesses this path on the web application, Django will call the `views.index` function to handle the request. The `name='index'` part provides a unique name to this URL pattern, which can be used to reverse-resolve URLs in the templates or views.

5. `path('about/', views.about, name='about')`
   - This line defines another URL pattern for the path `/about/`. 
   When a user accesses this path, Django will call the `views.about` function to handle the request. The `name='about'` part assigns the name "about" to this URL pattern.

In summary:

- The `urlpatterns` list is where you define all the URL patterns for your application. Each URL pattern is specified using the `path()` function.
- The first argument of the `path()` function is the URL path as a string.
- The second argument is the view function that will be called when a request matches the specified URL pattern.
- The optional `name` argument gives a name to the URL pattern, allowing you to refer to it in templates or views using the `reverse()` function for URL reversing.

'''