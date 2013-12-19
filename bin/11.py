import eDraw as edw

tree = edw.layer(name="fractal_tree", fill_color="#000000")

def frtree(layer, x1=300, y1=550, angle=-90, depth=9):
    import numpy as np
    if depth:
        x2 = x1 + int(np.cos(np.radians(angle)) * depth * 10.0)
        y2 = y1 + int(np.sin(np.radians(angle)) * depth * 10.0)
        layer.add(edw.line(points=[(x1, y1), (x2, y2)]))
        frtree(layer, x2, y2, angle - 20, depth - 1)
        frtree(layer, x2, y2, angle + 20, depth - 1)

frtree(tree, x1=300, y1=550, angle=-90, depth=12)

edw.save(tree, "/home/erje/Programs/eDraw/data/11.ely", format="ely")
edw.save(tree, "/home/erje/Programs/eDraw/data/11.svg", format="svg")
