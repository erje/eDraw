import eDraw as edw
import eDraw.drawing as draw

two_crosses = edw.layer(name="two_crosses") 

two_crosses.add(draw.cross(cx=0,cy=0,size=50))
two_crosses.add(draw.cross(cx=0,cy=0,size=50).rotate(45).move(200, 100))

edw.save(two_crosses, "/home/erje/Programs/eDraw/data/20.ely", format="ely")
edw.save(two_crosses, "/home/erje/Programs/eDraw/data/20.svg", format="svg")
