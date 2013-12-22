import eDraw as edw
import eDraw.drawing as draw

four_crosses = edw.layer(name="four_crosses")

four_crosses.add(draw.cross(cx=0,cy=0,size=10))
four_crosses.add(draw.cross(cx=25,cy=0,size=10))
four_crosses.add(draw.cross(cx=0,cy=25,size=10))
four_crosses.add(draw.cross(cx=25,cy=25,size=10))

edw.save(four_crosses, "/Users/erje/Programs/eDraw/data/5", format="ely, svg")
