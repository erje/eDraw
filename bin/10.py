import eDraw as edw
import eDraw.drawing as draw

four_crosses = edw.layer(name="four_crosses")

four_crosses.add(draw.cross(cx=0,cy=0,size=10))
four_crosses.add(draw.cross(cx=60,cy=0,size=10))
four_crosses.add(draw.cross(cx=0,cy=75,size=10))
four_crosses.add(draw.cross(cx=60,cy=-25,size=10))

edw.save(four_crosses, "/home/erje/Programs/eDraw/data/10.ely", format="ely")
edw.save(four_crosses, "/home/erje/Programs/eDraw/data/10.svg", format="svg")
