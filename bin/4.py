import eDraw as edw
import eDraw.drawing as draw

edw.save(draw.cross(cx=10,cy=10,size=50), "/home/erje/Programs/eDraw/data/4.ely", format="ely")
edw.save(draw.cross(cx=10,cy=10,size=50), "/home/erje/Programs/eDraw/data/4.svg", format="svg")
