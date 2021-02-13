from graphics.threeD_graphics import cuboid as cb
from graphics.threeD_graphics import sphere as sp
from graphics import rectangle
from graphics import circle as cr;

r=int(input("enter the radius of circle : "))
cr.carea(r)
cr.cperi(r)

l=int(input("enter the Length of Reactangle : "))
b=int(input("enter the Breadth of Reactangle : "))
rectangle.rarea(l,b)
rectangle.rperi(l,b)

s=int(input("enter the radius of Sphere : "))
sp.spr_circum(s)
sp.spr_area(s)

lc=int(input("enter the Length  of Cuboid : "))
wc=int(input("enter the Width  of Cuboid : "))
hc=int(input("enter the Height  of Cuboid : "))
cb.cubarea(lc,wc,hc)
cb.cubperi(lc,wc,hc)