# Phone negative cutaway geometry

# This file contains two functions which should contain all variables for the creation of the phone.
# phone_cut will return the geometry of the phone negative
# phone_size will return a vector containing the size of the phone-body (as a bounding box)

import os, sys
import math as math
import cadquery as cq
import math as math
from collections import namedtuple
from cadquery import cqgi


# ----- Global variables
tolerance = 0.2;

def phone_size():
    return cq.Vector(78.5 + tolerance, 159 + tolerance, 10 + tolerance);

def phone_cut():

    ## --------------------------- variables
    phonesize = phone_size();
    ## outer-fillet
    outerFillet=10
    topFillet=2
    baseDistance=3
    USB_CUT=cq.Vector(10,10,30);
    USB_cut_offset = 1 + tolerance;
    USB_cut_fillet = 3 + tolerance;

    buttonLength = 50;
    buttonHeight = 5;
    buttonOffset = 4;
    buttonXOffset = -6.5;
    buttonYOffset = 40

    # The intention here is to create the 'blank' that will be removed from the insert.

    phoneEdge = (cq.Sketch()
        .rect(phonesize.y, phonesize.x)
        .vertices()
        .fillet(outerFillet))
    s2 = (cq.Sketch()
         .rect(phonesize.y, phonesize.x/3)
         .vertices()
         .fillet(1))

    # Create phone body
    result = cq.Workplane("XY").placeSketch(phoneEdge).extrude(-phonesize.z).edges(">Z").fillet(topFillet);

    # Add side button space
    result = result.faces("<Y").workplane().moveTo(buttonYOffset,buttonXOffset).box(buttonLength, buttonHeight, buttonOffset,[True, True, False])\
    .edges("<Y").fillet(buttonHeight/3)



    # Create rectangle and phone edge loft.
    BaseTaper = cq.Workplane().workplane(-phonesize.z)\
        .placeSketch(phoneEdge, s2.moved(cq.Location(cq.Vector(0, 0, -baseDistance))))\
        .loft();
    result += BaseTaper

    # Add expansion hole for USB port
    result = result + cq.Workplane("ZY").workplane(offset=phonesize.y/2)\
    .moveTo(-(USB_CUT.x + USB_cut_offset),0).box(USB_CUT.x, USB_CUT.y, USB_CUT.z,[False,True,True]).edges("|X").fillet(USB_cut_fillet);

    #Deep call to debug for local editing
    cqgi.ScriptCallback().debug(obj=result);
    return result;

cqgi.ScriptCallback().show_object(phone_cut(), name='phone_cut', options=dict(color='#3333CC'));
