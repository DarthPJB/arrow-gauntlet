# Arrow phone-casing assembly
# These peices form the hard-casing around the computer-unit (smartphone) fitted
# into the gauntlet


import os, sys
import math as math

sys.path.append(os.getcwd());


import cadquery as cq
from cadquery import exporters
from cadquery import importers

# load the phone-cut module
from phone_cut import phone_cut, phone_size
from lib import snap_fit_cut

# ----------- Aquire cutaway size
phoneSize = phone_size();
# ----------- Define holder holder_dimensions
holder_dimensions = cq.Vector(180,100,15)
# ----------- Adjustment for cut-position
cut_height_adjust = 0.1;

# Generate geometry of phone for removal
phone = phone_cut().translate(cq.Vector(0,0,cut_height_adjust))

# debug(phone, name='phone cut');

# ----- Create the initial holder using a box
Cradle = cq.Workplane("XY").workplane(-holder_dimensions.z).box(holder_dimensions.x, holder_dimensions.y, holder_dimensions.z, centered=[True,True,False]);
# ----- Add edge chamfers to provide slope
Cradle = Cradle.edges("|X and >Y and >Z").chamfer(10)
Cradle = Cradle.edges("|X and <Y and >Z").chamfer(10)
# ----- remove the phone geometry from the cradle
Cradle = Cradle.cut(phone)
# ----- split the cradle into two *snap together* parts.
SnapCut = snap_fit_cut(Cradle.faces("<Z").edges("|Y"));

debug(SnapCut);
result1 = Cradle.faces(">Y").workplane((-holder_dimensions.y)/2).split(keepTop=True)
result2 = Cradle.faces(">Y").workplane((-holder_dimensions.y)/2).split(keepBottom=True)

show_object(result1, name='Cradle Part A', options=dict(color='#3333CC'))
show_object(result2, name='Cradle Part B', options=dict(color='#3333CC'))
