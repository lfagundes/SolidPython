from ...core.object_base import OpenSCADObject, OpenSCADConstant
from ... import import_scad
from pathlib import Path

baseDir = Path(__file__).absolute().parent.parent.parent
importFile = baseDir / "libs" / "BOSL2" / "walls.scad"
_ = import_scad(f"{importFile}", use_not_include=False)

class sparse_wall(OpenSCADObject):
    def __init__(self, h=None, l=None, thick=None, maxang=None, strut=None, max_bridge=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("sparse_wall", {"h" : h, "l" : l, "thick" : thick, "maxang" : maxang, "strut" : strut, "max_bridge" : max_bridge, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class corrugated_wall(OpenSCADObject):
    def __init__(self, h=None, l=None, thick=None, strut=None, wall=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("corrugated_wall", {"h" : h, "l" : l, "thick" : thick, "strut" : strut, "wall" : wall, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class thinning_wall(OpenSCADObject):
    def __init__(self, h=None, l=None, thick=None, ang=None, braces=None, strut=None, wall=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("thinning_wall", {"h" : h, "l" : l, "thick" : thick, "ang" : ang, "braces" : braces, "strut" : strut, "wall" : wall, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class thinning_triangle(OpenSCADObject):
    def __init__(self, h=None, l=None, thick=None, ang=None, strut=None, wall=None, diagonly=None, center=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("thinning_triangle", {"h" : h, "l" : l, "thick" : thick, "ang" : ang, "strut" : strut, "wall" : wall, "diagonly" : diagonly, "center" : center, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class narrowing_strut(OpenSCADObject):
    def __init__(self, w=None, l=None, wall=None, ang=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("narrowing_strut", {"w" : w, "l" : l, "wall" : wall, "ang" : ang, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})
