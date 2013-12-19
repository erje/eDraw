import eDraw as edw
import eDraw.drawing as draw

mm_rc_a = edw.layer(name="mm_rect_closed_array", fill_color="#7F2AFF")

width=30.0
w=width
bar=2.0
b=bar
gap=1.5
g=gap
chamfer=0.25
c=chamfer

nx=10
ny=9 
mulx=4
muly=4
dx=25.0
dy=25.0
mdx=3
mdy=3
dangle=1

angle = 0
for iy in range(ny):
    for ix in range(nx):
        for imulx in range(mulx):
            for imuly in range(muly):
                mm_rc_a.add( draw.mm_rect_closed(width=w,bar=b,gap=g,chamfer=c).rotate(angle).move((mulx * ix + imulx) * (dx+w) + ix * mdx, (muly * iy + imuly) * (dy+w) + iy * mdy) )
        angle = angle + dangle

edw.save(mm_rc_a, "/home/erje/Programs/eDraw/data/15.ely", format="ely")
edw.save(mm_rc_a, "/home/erje/Programs/eDraw/data/15.svg", format="svg")
