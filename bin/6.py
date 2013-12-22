import eDraw as edw
import eDraw.drawing as draw

align_and_square = edw.struct(name="align_and_square")
four_crosses = edw.layer(name="four_crosses")
square=edw.layer(name="square", fill_color="#FF0000")
align_and_square.add(four_crosses, square)

four_crosses.add(draw.cross(cx=0,cy=0,size=10))
four_crosses.add(draw.cross(cx=100,cy=0,size=10))
four_crosses.add(draw.cross(cx=0,cy=100,size=10))
four_crosses.add(draw.cross(cx=100,cy=100,size=10))

square.add(edw.rect(x=50,y=50,width=10,height=20))

edw.save(align_and_square, "/Users/erje/Programs/eDraw/data/6", format="ely, svg")
