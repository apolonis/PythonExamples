from django.http import HttpResponse
from . import models

# This is like controller in java
def index(request):
    return HttpResponse("<h1>Yo world, whats up?")

def create(request):
    user1 = models.User("David","Beckham","https://www.google.com/imgres?imgurl=https%3A%2F%2Fimagesvc.meredithcorp.io%2Fv3%2Fmm%2Fimage%3Furl%3Dhttps%253A%252F%252Fcdn-img.instyle.com%252Fsites%252Fdefault%252Ffiles%252Fstyles%252F684xflex%252Fpublic%252Fimages%252F2019%252F01%252F010718-david-beckham-lead.jpg%253Fitok%253D7Jzsa4t-%26w%3D400%26c%3Dsc%26poi%3Dface%26q%3D85&imgrefurl=https%3A%2F%2Fwww.instyle.com%2Fnews%2Fdavid-beckham-love-magazine-cover&tbnid=C1-BpG1yEVP32M&vet=12ahUKEwil__r7jPvlAhVKelAKHaMOBa8QMygAegUIARDuAQ..i&docid=M3X57YnRiwHJSM&w=400&h=533&q=beckham%20image&ved=2ahUKEwil__r7jPvlAhVKelAKHaMOBa8QMygAegUIARDuAQ")
    return HttpResponse(f"<h1>Hey {user1.image_url} what do u want?")

