from django.http import HttpResponse

# This is like controller in java
def index(reqiest):
    return HttpResponse("<h1>Yo world, whats up?")

def indexi(reqiest):
    return HttpResponse("<h1>Hey user what do u want?")