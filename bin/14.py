import eDraw as edw

four_crects = edw.layer(name="four_rects")

four_crects.add(edw.crect(cx=0,y=50,width=5,height=10))
four_crects.add(edw.crect(cx=-100,cy=150,width=15,height=20))
four_crects.add(edw.crect(cx=200,cy=-250,width=25,height=30))
four_crects.add(edw.crect(cx=-300,cy=-350,width=35,height=40))

edw.save(four_crects, "/home/erje/Programs/eDraw/data/13.ely", format="ely")
edw.save(four_crects, "/home/erje/Programs/eDraw/data/13.svg", format="svg")
