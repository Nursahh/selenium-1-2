#def factoriel(numara):
#    faktoriyel=1
#    for i in range(1,numara+1):
#        faktoriyel *=i
#    print("Faktoriyel:",faktoriyel)


#sayi=int(input("sayi gir:"))

#factoriel(sayi)
#factoriel(7)


#   ------------------------------------------------------------

#def factoriel(numara):
#    faktoriyel=1
#    for i in range(1,numara+1):
#        faktoriyel *=i
#    return faktoriyel

#sayi=int(input("sayi gir:"))

#a= factoriel(sayi)
#print(a)

#------------------------------------------------------------------


#def kokbul(a,b,c):
#    delta = (b*b - (4*a*c))
#    if(delta < 0):
#        print("reel kok yok!!")
#        return
#    x1=(-b - delta**0.5)/(2*a)
#    x2=(-b + delta**0.5)/(2*a)

#    return (x1,x2)

#a = int(input("a:"))
#b = int(input("b:"))
#c = int(input("c:"))

#sonuc = kokbul(a,b,c)

#print(sonuc)

#--------------------------------------------------------------------
#ödev 1-1

# def fonk(s):
#     if(s=="yes"):
#         print("shut down")
#     elif(s=="no"):
#         print("Shuttig down")
#     else:
#         print("sorry")
#
# soru=input("cevap:")
# fonk(soru)


#------------------------------------------------------------------
#ödev 1-2

# import math
#
# print(math.sqrt(13689))

#------------------------------------------------------------------
#ödev 1-3

# def distance_from_zero(x):
#     if(type(x)==int or type(x)==float):
#         md = abs(x)
#         print(md)
#     else:
#         print("nope")
#
# sonuc = raw_input("sayi gir:")
# distance_from_zero(sonuc)
# print(type(sonuc))

#-----------------------------------------------------------------
#ödev 1-3

# def distance_from_zero(argument):
#     if type(argument) is float or type(argument) is int:
#        print(abs(argument))
#     else:
#         print('Nope')
# distance_from_zero(2)
# distance_from_zero(2.0)
# distance_from_zero(-5.6)
# distance_from_zero('dedsmnksjn')
# distance_from_zero(['asd','dasda'])

#-----------------------------------------------------------------

#ödev 1-4

# def computepa(hours, rate):
#     workDay=40
#     if(hours>workDay):
#         extra=(hours-workDay)*1.5
#         total=(extra+workDay)*rate
#     else:
#         total=hours*rate
#     print('total', total)
#
#
# hours=int(input("saati gir:"))
# rate=int(input("rate degerini gir:"))
#
# computepa(hours,rate)

#------------------------------------------------------------------

#ödev1-5
# def hotel_cost(city_cost, night):
#     return city_cost*night
# def plane_ride_cost(city, days):
#      city_cost={"Charlotte": 183, "Tampa": 220, "Pittsburgh": 222, "Los Angeles": 475}
#      return hotel_cost(city_cost[city], days)
# def rental_cost(days):
#     if(days>=7):
#         total=(40*days)-50
#     elif(3>=days and days<7):
#         total = (40 * days)-20
#     else:
#         total = 40 * days
#     return int(total)
# def trip_cost(city, days):
#     tripCost = plane_ride_cost(city, days)
#     rentalCost = rental_cost(days)
#     spending_money = tripCost + rentalCost
#     print(spending_money)
# city = input("şehri girin:")
# night=int(input("geceyi gir:"))
# trip_cost(city, night)


#---------------------------------------------------------------

#ödev 1-6

# def cube(number):
#     print(number**3)
#
# def by_three(number):
#     if ((number % 3) == 0):
#         cube(number)
#     else:
#         print("false")
#
# sayi=int(input("sayi gir:"))
# by_three(sayi)

#--------------------------------------------------------------
#--------------------------------------------------------------

#ödev 2-1

# class Triangle(object):
#
#     def __init__(self, angle1, angle2, angle3):
#         self.angle1 = angle1
#         self.angle2 = angle2
#         self.angle3 = angle3
#
#     def check_angles(self):
#         return self.angle1+self.angle2+self.angle3 == 180
#
# r = Triangle(90, 60, 30)
# print("Area of Triangle: %s " % (r.check_angles()))

#-----------------------------------------------------------

#ödev 2-2

# class Song(object):
#
#     def __init__(self, lyrics, list):
#         self.lyrics = lyrics
#         self.list = list
#
#     def sing_me_a_songthat(self):
#         print(self.lyrics)
#
# happy_bday = Song(["May god bless you, ",
#                    "Have a sunshine on you,",
#                    "Happy Birthday to you !"], "true")
# print("Area of Triangle: %s " % (happy_bday.sing_me_a_songthat()))

#-----------------------------------------------------------

#ödev 2-3

# class Lunch(object):
#
#     def __init__(self, menu):
#         self.menu = menu
#     def menu_price(self):
#         if(self.menu == "menu 1"):
#             print("price: 12.00")
#         elif(self.menu == "menu 2"):
#             print("price: 13.40")
#         else:
#             print("menude hata")
#
# Paul = Lunch("menu 1")
# Paul.menu_price()

#---------------------------------------------------------------

#ödev 2-4

# class Point3D(object):
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#     def __repr__(self):
#         print("%d, %d, %d", self.x, self.y, self.z)
#
# my_point = Point3D(x=1,y=2,z=3)
# my_point.__repr__()





















