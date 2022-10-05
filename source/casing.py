import os, sys
import math as math

sys.path.append(os.getcwd());


import cadquery as cq
from cadquery import exporters
from cadquery import importers

from phone_cut import phone_cut

holder_dimensions = cq.Vector(180,100,15)
cut_height_adjust = 0.1;

phone = phone_cut().translate(cq.Vector(0,0,cut_height_adjust))
#debug(phone, name='phone cut');

Holder = cq.Workplane("XY").workplane(-holder_dimensions.z).box(holder_dimensions.x, holder_dimensions.y, holder_dimensions.z, centered=[True,True,False]);
Holder = Holder.edges("|X and >Y and >Z").chamfer(10)
Holder = Holder.edges("|X and <Y and >Z").chamfer(10)
Holder = Holder.cut(phone)
result1 = Holder.faces(">Y").workplane((-holder_dimensions.y)/2).split(keepTop=True)
result2 = Holder.faces(">Y").workplane((-holder_dimensions.y)/2).split(keepBottom=True)

show_object(result1, name='Holder Part A', options=dict(color='#3333CC'))
show_object(result2, name='Holder Part B', options=dict(color='#3333CC'))
