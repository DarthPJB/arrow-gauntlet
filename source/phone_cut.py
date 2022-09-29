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

    ## --------------------------- variables
    height = 160
    width = 78.0
    thickness = 11.5
    ## outer-fillet
    outerFillet=10
    topFillet=2
    baseDistance=3


    # The intention here is to create the 'blank' that will be removed from the insert.

    phoneEdge = (cq.Sketch()
        .rect(height, width)
        .vertices()
        .fillet(outerFillet))
    s2 = (cq.Sketch()
         .rect(height, width/3)
         .vertices()
         .fillet(1))
    result = cq.Workplane("XY").placeSketch(phoneEdge).extrude(thickness);
    BaseTaper = (cq.Workplane()
        .placeSketch(phoneEdge, s2.moved(cq.Location(cq.Vector(0, 0, -baseDistance))))
        .loft())
    result += BaseTaper
    result = result.edges(">Z").fillet(topFillet)
    result = result.faces("<X").workplane().moveTo(0,thickness/3).box(18,10,100)
    return result;

#show_object(phone_cut(), name='phone_cut', options=dict(color='#3333CC'));
