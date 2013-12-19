import eDraw as edw
import eDraw.drawing as draw

edw.save(draw.cross(size=100).rotate(45), "/home/erje/Programs/eDraw/data/16.ely", format="ely")
edw.save(draw.cross(size=100).rotate(45), "/home/erje/Programs/eDraw/data/16.svg", format="svg")
