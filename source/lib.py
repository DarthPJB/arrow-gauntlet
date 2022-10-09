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
from cadquery import cqgi
from cadquery import exporters
from cadquery import importers


# --- Convert the numpy array into cadquery vectors so they can be used as locations
# random_vectors = [cq.Vector(*tuple(p), 0) for p in points]
# --- Convert the numpy array into cadquery vertices so they can be seen in cq-editor
# random_vertices = [cq.Vertex.makeVertex(*tuple(p), 0) for p in points]

# ----- Global variables
tolerance = 0.2;

def snap_fit_cut(Edges):
    # This function expects two edges, between witch the snap-Interlock will be generated

    # we begin by checking for both edges.
    if Edges.edges().size() != 2:
        raise NameError('Object does not contain correct geometry:' + __file__)

    #Grab points
    Points = Edges.vertices();
    #print("lockon!")
    print(dir(Points))
    return Points;
