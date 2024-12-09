from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    # return HttpResponse("""<h1>testing HTTP response from Django server</h1>
    # <p>Hi welcome to the django server</p>
    # <hr>
    # <p>This is demo template to demonstrate that complex html page cannot be represented using HttpResponse feasibly.""")

    people = [
        {'name': 'Harsh', 'age': 25},
        {'name': 'Tanya', 'age': 25},
        {'name': 'Karishma', 'age': 24},
        {'name': 'Swati', 'age': 23},
        {'name': 'Manaswi', 'age':25}
    ]

    text = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptas quibusdam esse nihil est ad itaque, beatae soluta saepe omnis ratione nulla consequatur deleniti labore architecto sit amet natus, repudiandae aspernatur quidem ducimus ea excepturi quae. Ipsam deleniti dolor corrupti. Totam eum quasi tempore cupiditate ex aspernatur ipsam blanditiis illum animi tenetur officia quos sed nesciunt unde earum, cum temporibus dolorum id. Nisi modi, eaque animi commodi, dolorem non omnis iure sed eum quaerat numquam mollitia vero illum, odio rerum dolorum nostrum aut sapiente tenetur. Necessitatibus dignissimos quaerat commodi alias. Maiores alias vitae voluptatum quae laborum! Repudiandae illum quasi saepe dolor?"

    return render(request, 'home/index.html', context={'people': people, 'text': text, 'page': 'Django tutorial Home'})

def about(request):
    return render(request, "home/about.html", context={'page': 'about page'})

def contact(request):
    return render(request, "home/contact.html", context={'page': 'contact'})

def success_page(request):
    print('*'*10)
    return HttpResponse('<h1>Success page reached</h1>')
