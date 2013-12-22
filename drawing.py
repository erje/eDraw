from .shapes import rect, poly, line

def cross(cx=0.0, cy=0.0, size=10.0):
    h = float(abs(size))
    return poly( points = [ (cx - h/10, cy + h/2), (cx + h/10, cy + h/2), (cx, cy), (cx + h/2, cy + h/10), (cx + h/2, cy - h/10), (cx, cy), (cx + h/10, cy - h/2), (cx - h/10, cy - h/2), (cx, cy), (cx - h/2, cy - h/10), (cx - h/2, cy + h/10), (cx, cy) ] )

def mm_rect_closed(width=30.0, bar=2.0, gap=1.5, chamfer=0.25):
    w = width
    b = bar
    g = gap
    c = chamfer
    
    cap = 10

    # array holding a single polygon as coordinate pairs
    #rect_closed_base = Array.new(0) { Array.new(2) }
    rc = poly(points=[(0,0)])
    
    #upper
    rc.add( (-w/2, 0) )
    rc.add( (-w/2, w/2-c) )
    rc.add( (-w/2+c, w/2) )
    rc.add( (+w/2-c, w/2) )
    rc.add( (+w/2, w/2-c) )
    rc.add( (+w/2, 0) )
    rc.add( (+g/2, 0) )
    rc.add( (+g/2, cap/2) )
    rc.add( (+g/2+b-c, cap/2) )
    rc.add( (+g/2+b, cap/2-c) )
    rc.add( (+g/2+b, b/2) )
    rc.add( (+w/2-b, b/2) )
    rc.add( (+w/2-b, w/2-b-c) )
    rc.add( (+w/2-b-c, w/2-b) )
    rc.add( (-w/2+b+c, w/2-b) )
    rc.add( (-w/2+b, w/2-b-c) )
    rc.add( (-w/2+b, b/2) )
    rc.add( (-g/2-b, b/2) )
    rc.add( (-g/2-b, cap/2-c) )
    rc.add( (-g/2-b+c, cap/2) )
    rc.add( (-g/2, cap/2) )
    rc.add( (-g/2, 0) )
    
    #lower
    rc.add( (-w/2, 0) )
    rc.add( (-w/2, -w/2+c) )
    rc.add( (-w/2+c, -w/2) )
    rc.add( (+w/2-c, -w/2) )
    rc.add( (+w/2, -w/2+c) )
    rc.add( (+w/2, 0) )
    rc.add( (+g/2, 0) )
    rc.add( (+g/2, -cap/2) )
    rc.add( (+g/2+b-c, -cap/2) )
    rc.add( (+g/2+b, -cap/2+c) )
    rc.add( (+g/2+b, -b/2) )
    rc.add( (+w/2-b, -b/2) )
    rc.add( (+w/2-b, -w/2+b+c) )
    rc.add( (+w/2-b-c, -w/2+b) )
    rc.add( (-w/2+b+c, -w/2+b) )
    rc.add( (-w/2+b, -w/2+b+c) )
    rc.add( (-w/2+b, -b/2) )
    rc.add( (-g/2-b, -b/2) )
    rc.add( (-g/2-b, -cap/2+c) )
    rc.add( (-g/2-b+c, -cap/2) )
    rc.add( (-g/2, -cap/2) )
    rc.add( (-g/2, 0) )

    return rc
