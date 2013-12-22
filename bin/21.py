import eDraw as edw
import eDraw.drawing as draw

two_mms = edw.layer(name="two_mms") 

two_mms.add(draw.mm_rect_closed(30, 2, 1.5, 0.25))
two_mms.add(draw.mm_rect_closed(30, 2, 1.5, 0.25).rotate(45).move(200, 100))

edw.save(two_mms, "/Users/erje/Programs/eDraw/data/21", format="ely, svg")
