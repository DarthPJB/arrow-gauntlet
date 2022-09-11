# Mike-Bike battery-box casing, by the Astral_3D Team aboard the Astral Ship, 2021-05-15
# Expecting CQ-Editor 0.2.0 or heigher, Cadquery 2.0.0
# This is version 3.0 of the battery-box design, a third prototype based heavily
# on the amazing work of our team!

import cadquery as cq
import math as math
from collections import namedtuple
from cadquery import exporters
from cadquery import importers

def phone_cut()

    ## --------------------------- variables
    height = 60.0
    width = 80.0
    thickness = 10.0

    # The intention here is to create the 'blank' that will be removed from the insert.

    result = cq.Workplane("XY").box(height, width, thickness)
    return result;

#debug(Cut_Edge, name='cut edge');

#show_object(result, name='phone_cut', options=dict(color='#3333CC'));
