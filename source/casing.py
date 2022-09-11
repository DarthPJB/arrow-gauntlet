# Mike-Bike battery-box casing, by the Astral_3D Team aboard the Astral Ship, 2021-05-15
# Expecting CQ-Editor 0.2.0 or heigher, Cadquery 2.0.0
# This is version 3.0 of the battery-box design, a third prototype based heavily
# on the amazing work of our team!

import cadquery as cq
import math as math
from collections import namedtuple
from cadquery import exporters
from cadquery import importers
import os, sys
# helper to get correct path on NixOs
path = os.path.dirname(os.path.abspath(sys.argv[1]));
print(path);
sys.path.append(path)


from phone_cut import phone_cut
DEBUG_MODE = True;

result = phone_cut();


#debug(Cut_Edge, name='cut edge');

show_object(result, name='Printed_Tip', options=dict(color='#3333CC'));
