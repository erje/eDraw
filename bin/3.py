import eDraw as edw

four_rects = edw.layer(name="four_rects")

four_rects.add(edw.rect(x=0,y=0,width=10,height=20))
four_rects.add(edw.rect(x=0,y=50,width=10,height=20))
four_rects.add(edw.rect(x=50,y=0,width=10,height=20))
four_rects.add(edw.rect(x=50,y=50,width=10,height=20))

edw.save(four_rects, "/Users/erje/Programs/eDraw/data/3", format="ely, svg")
