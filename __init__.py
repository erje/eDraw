from .shapes import rect, crect, poly, line
from .io import save
from .errors import AddError

class Project:
    """
    A group of samples with an interrelated purpose. Corresponds to one eDraw ".ely" file. Contains many structures. Attributes which don't belong in the object-hierarchy (but which eDraw nevertheless requires, such as display grid attributes) are held as properties in the Project class.
    """

    def __init__(self, structures = None, name = "Project", locked = False, version = 1.0, grid_horizontal = 1, grid_vertical = 1, grid_show = True, grid_snap_to = False):
        if structures == None:
            self.structures = []
        self.name = name
        self.locked = locked
        self.version = version
        self.grid_horizontal = grid_horizontal
        self.grid_vertical = grid_vertical
        self.grid_show = grid_show
        self.grid_snap_to = grid_snap_to
    def __iter__(self):
        self.structures_index = 0
        return self
    def __next__(self):
        if self.structures_index == len(self.structures):
            raise StopIteration
        self.structures_index += 1
        return self.structures[self.structures_index - 1]

    def add(self, *args, **kwargs):
        """
        If Structure attributes are passed, instantiates the Structure and adds it to the Project. If one or more structures are passed, they are added to the Project. Don't pass Structures as keyword arguments! Dont't pass Structures AND keyword arguments! If a Structure is instantiated, it is returned. If not, nothing is returned.
        """
        if any(kwargs):
            tmp = Structure(**kwargs)
            self.structures.append(tmp)
            return tmp
        else:
            for structure in args:
                if (structure.__class__.__name__ != "Structure"):
                    raise AddError("Attempting to add non-structure of class *" + structure.__class__.__name__ + "* to project")
                self.structures.append(structure)
            return

class Structure:
    """
    A single sample. Corresponds to one eDraw structure. Contains Layers.
    """

    def __init__(self, layers = None, name = "Structure", locked = False):
        if layers == None:
            self.layers = []
        self.name = name
        self.locked = locked
    def __iter__(self):
        self.layers_index = 0
        return self
    def __next__(self):
        if self.layers_index == len(self.layers):
            raise StopIteration
        self.layers_index += 1
        return self.layers[self.layers_index - 1]

    def add(self, *args, **kwargs):
        if any(kwargs):
            tmp = Layer(**kwargs)
            self.layers.append(tmp)
            return tmp
        else:
            for layer in args:
                if (layer.__class__.__name__ != "Layer"):
                    raise AddError("Attempting to add non-layer of class *" + layer.__class__.__name__ + "* to structure")
                self.layers.append(layer)
            return

class Layer:
    """
    A single process in the SEM. Corresponds to one eDraw layer. Can contain many Shapes.
    """

    def __init__(self, shapes=None, fill_color="#00FF00", fill_opacity=0.5, hidden=False, locked=False, name="Layer", frame_cx=0.0, frame_cy=0.0, frame_size=1.0):
        if shapes == None:
            self.shapes = []
        self.fill_color = fill_color
        self.fill_opacity = fill_opacity
        self.hidden = hidden
        self.locked = locked
        self.name = name
        self.frame_cx = frame_cx
        self.frame_cy = frame_cy
        self.frame_size = frame_size
        self.bbox = (0,0,0,0)
    def __iter__(self):
        self.shapes_index = 0
        return self
    def __next__(self):
        if self.shapes_index == len(self.shapes):
            raise StopIteration
        self.shapes_index += 1
        return self.shapes[self.shapes_index - 1]
    
    def add(self, *args):
        for shape in args:
            if (shape.__class__.__name__ not in ["Rect", "Polygon", "Lines"]):
                raise AddError("Attempting to add non-shape of class *" + shape.__class__.__name__ + "* to layer")
            self.shapes.append(shape)
        return self

    def write_field(self):
        if (len(self.shapes) == 0):
            return (0,0,0,0)
        for i, shape in enumerate(self):
            if (i==0):
                (min_x,max_x,min_y,max_y) = shape.bounding_box()
                continue
            (mn_x, mx_x, mn_y, mx_y) = shape.bounding_box()
            min_x = min(min_x, mn_x)
            max_x = max(max_x, mx_x)
            min_y = min(min_y, mn_y)
            max_y = max(max_y, mx_y)

        self.frame_cx = (max_x + min_x)/2.0
        self.frame_cy = (max_y + min_y)/2.0
        self.frame_size = max(abs(max_x - min_x), abs(max_y - min_y))
        self.bbox=(min_x,max_x,min_y,max_y)
        return (min_x,max_x,min_y,max_y)

class Array:
    pass

def proj(**kwargs):
    return Project(**kwargs)

def struct(**kwargs):
    return Structure(**kwargs)

def layer(**kwargs):
    return Layer(**kwargs)

def array(**kwargs):
    pass
