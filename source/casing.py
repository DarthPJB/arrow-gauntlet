import os, sys
import math as math

# helper to allow imports outside of cq-editor
sys.path.append(os.getcwd());

import cadquery as cq
from cadquery import exporters
from cadquery import importers

from phone_cut import phone_cut

Holder_Dimension = cq.Vector(160,80,13)

Holder = cq.Workplane("XY").box(Holder_Dimension.x, Holder_Dimension.y, Holder_Dimension.z).cut(phone_cut())
#debug(phone_cut(), name='cut edge');
result1 = Holder.faces(">Y").workplane((-Holder_Dimension.x)/4).split(keepTop=True)
result2 = Holder.faces(">Y").workplane((-Holder_Dimension.x)/4).split(keepBottom=True)

show_object(result1, name='Holder Part A', options=dict(color='#3333CC'))
show_object(result2, name='Holder Part B', options=dict(color='#3333CC'))
