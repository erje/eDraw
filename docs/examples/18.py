import eDraw as edw
import eDraw.drawing as draw

edw.save(draw.mm_rect_closed(30, 2, 1.5, 0.25).rotate(45), "/Users/erje/Programs/eDraw/data/18", format="ely, svg")
