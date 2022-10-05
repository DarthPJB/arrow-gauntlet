# Mike-Bike battery-box casing, by the Astral_3D Team aboard the Astral Ship, 2021-05-15
# Expecting CQ-Editor 0.2.0 or heigher, Cadquery 2.0.0
# This is version 3.0 of the battery-box design, a third prototype based heavily
# on the amazing work of our team!
import os, sys
import math as math
import cadquery as cq
import math as math
from collections import namedtuple
from cadquery import exporters
from cadquery import importers

def phone_cut():

    tolerance = 0.2;
    ## --------------------------- variables
    height = 159 + tolerance;
    width = 77.0 + tolerance;
    thickness = 10 + tolerance;
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
        .rect(height, width)
        .vertices()
        .fillet(outerFillet))
    s2 = (cq.Sketch()
         .rect(height, width/3)
         .vertices()
         .fillet(1))

    # Create phone body
    result = cq.Workplane("XY").placeSketch(phoneEdge).extrude(-thickness).edges(">Z").fillet(topFillet);

    # Add side button space
    result = result.faces("<Y").workplane().moveTo(buttonYOffset,buttonXOffset).box(buttonLength, buttonHeight, buttonOffset,[True, True, False])\
    .edges("<Y").fillet(buttonHeight/3)



    # Create rectangle and phone edge loft.
    BaseTaper = cq.Workplane().workplane(-thickness)\
        .placeSketch(phoneEdge, s2.moved(cq.Location(cq.Vector(0, 0, -baseDistance))))\
        .loft();
    result += BaseTaper

    # Add expansion hole for USB port
    result = result + cq.Workplane("ZY").workplane(offset=height/2)\
    .moveTo(-(USB_CUT.x + USB_cut_offset),0).box(USB_CUT.x, USB_CUT.y, USB_CUT.z,[False,True,True]).edges("|X").fillet(USB_cut_fillet);
    return result;

#show_object(phone_cut(), name='phone_cut', options=dict(color='#3333CC'));
