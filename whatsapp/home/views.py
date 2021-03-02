from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main(request):
    return render(request,"home/home.html")

def WhatsappData(Ph,Message):
    import time
    import webbrowser as web
    import pyautogui as pg
    Phone = "+91"+Ph
    web.open("https://web.whatsapp.com/send?phone="+Phone+"&text="+Message)
    time.sleep(30)
    pg.press("enter")
def SendData(request):
    if request.method == "POST":
        Ph = request.POST["Phone"]
        Message = request.POST["Message"]
        #print(Ph, Message)
        WhatsappData(Ph,Message)
        msg = "Message has successfully sent..."
        return render(request, "home/home.html", {"msg":msg})
    else:
        return HttpResponse("<h1>404 - Not Found :)</h1>")