from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
def index(request):
    return render(request,'myfolder/index.html')

def about(request):
    return render(request,'myfolder/about.html')

def register(request):
    return render(request,'myfolder/register.html')




'''
From the code above,
views is a function responsible for user requests and generating appropriate responses.
the purpose views.py file is to define view functions which are responsible for processing
user requests and returning HTTP response.
1. `from django.shortcuts import render, redirect`
   - This line imports two functions, `render` and `redirect`, 
   from the `django.shortcuts` module. These functions are commonly used in Django views to render HTML templates or redirect the user to a different URL.

2. `from django.http import HttpResponse, HttpResponseRedirect`
   - This line imports two classes, `HttpResponse` and `HttpResponseRedirect`, 
   from the `django.http` module. These classes are used to handle HTTP responses in Django views. `HttpResponse` is used to return a basic HTTP response with content, while `HttpResponseRedirect` is used to perform a redirect to another URL.

3. `def index(request):`
   - This is a Django view function named `index`.
    It takes a `request` object as a parameter, which represents the user's request made to this view. The view processes the request and returns an HTTP response. In this case, it renders the 'myfolder/index.html' template.

4. `return render(request, 'myfolder/index.html')`
   - This line returns an HTTP response using the `render` function. It takes two arguments: the `request` object and the template name ('myfolder/index.html'). The `render` function processes the template and returns an HTTP response with the rendered content.

5. `def about(request):`
   - This is another Django view function named `about`. 
   It also takes a `request` object as a parameter.

6. `return render(request, 'myfolder/about.html')`
   - This line is the return statement for the `about` view function. 
   It uses the `render` function to render the 'myfolder/about.html' template and return an HTTP response with the rendered content.

7. `def register(request):`
   - This is a third Django view function named `register`, again taking a `request` object as a parameter.

8. `return render(request, 'myfolder/register.html')`
   - This line is the return statement for the `register` view function. 
   It uses the `render` function to render the 'myfolder/register.html' template and return an HTTP response with the rendered content.

'''







# Create your views here.
