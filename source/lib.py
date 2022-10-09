# ------ General use library
# My hope is to implement useful joints, connections, or repeated parts into
# this library

# The general rule of thumb is, such fittings should take a face, or edge, then
# generate the required connection.

import os, sys
import math as math
import cadquery as cq
import math as math
from collections import namedtuple
from cadquery import exporters
from cadquery import importers

# ----- Global variables
tolerance = 0.2;

def snap_fit_cut(Edges):
    # This function expects two edges, between witch the snap-Interlock will be generated

    # we begin by checking for them.
    print(Edges)

    return cq.Workplane().box(10,10,10)
