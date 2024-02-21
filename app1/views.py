from django.shortcuts import render
from .models import Destination
# Create your views here.
def link1(request):
    des1=Destination()
    des1.name= 'hyderabad'
    des1.img = 'destination_1.jpg'
    des1.desc = 'the place is famaus for biryani'
    des1.prize = 799

    des2=Destination()
    des2.name= 'tirupati'
    des2.img = 'destination_3.jpg'
    des2.desc = 'the place full of devotional peace'
    des2.prize = 777

    des3=Destination()
    des3.name= 'chennai'
    des3.img = 'destination_2.jpg'
    des3.desc = 'the beatiful of water ocean'
    des3.prize = 888

    des4=Destination()
    des4.name= 'bangalore'
    des4.img = 'destination_4.jpg'
    des4.desc = 'the place is beaty for lights'
    des4.prize = 1000

    des5=Destination()
    des5.name= 'andhra'
    des5.img = 'destination_5.jpg'
    des5.desc = 'also called as annapurna state'
    des5.prize = 1111

    des6=Destination()
    des6.name= 'delhi'
    des6.img = 'destination_6.jpg'
    des6.desc = 'capital of our contry hindustan '
    des6.prize = 2020
    abc = [des1, des2, des3, des4, des5, des6]
    return render(request,'index.html',{'dd' : abc})

