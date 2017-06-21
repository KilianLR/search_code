# Search methods

import search

ab = search.GPSProblem('A', 'B', search.romania)

print "BUSQUEDA EN ANCHURA A-B"
print search.breadth_first_graph_search(ab).path()
print
print "BUSQUEDA EN PROFUNDIDAD A-B"
print search.depth_first_graph_search(ab).path()
print
print "BUSQUEDA LIMITADA EN PROFUNDIDAD A-B"
print search.depth_limited_search(ab).path()
print
print "BUSQUEDA EN PROFUNDIDAD ITERATIVA A-B"
print search.iterative_deepening_search(ab).path()
print
print "BUSQUEDA POR RAMIFICACION Y ACOTACION A-B"
print search.branch_bound_tree_search(ab).path()
print
print "BUSQUEDA POR RAMIFICACION Y ACOTACION CON SUBESTIMACION A-B"
print search.branch_bound_underestimates_tree_search(ab).path()
#print
#print "BUSQUEDA POR A* A-B"
#print search.astar_search(ab).path()
#print

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450

"""
on = search.GPSProblem('O', 'N', search.romania)

print "BUSQUEDA EN ANCHURA O-N"
print search.breadth_first_graph_search(on).path()
print
print "BUSQUEDA EN PROFUNDIDAD O-N"
print search.depth_first_graph_search(on).path()
print
print "BUSQUEDA LIMITADA EN PROFUNDIDAD O-N"
print search.depth_limited_search(on).path()
print
print "BUSQUEDA EN PROFUNDIDAD ITERATIVA O-N"
print search.iterative_deepening_search(on).path()
print
print "BUSQUEDA POR RAMIFICACION Y ACOTACION O-N"
print search.branch_bound_tree_search(on).path()
print
print "BUSQUEDA POR RAMIFICACION Y ACOTACION CON SUBESTIMACION O-N"
print search.branch_bound_underestimates_tree_search(on).path()
print
#print "BUSQUEDA POR A* O-N"
#print search.astar_search(on).path()
#print

zc = search.GPSProblem('Z', 'C', search.romania)

print "BUSQUEDA EN ANCHURA Z-C"
print search.breadth_first_graph_search(zc).path()
print
print "BUSQUEDA EN PROFUNDIDAD Z-C"
print search.depth_first_graph_search(zc).path()
print
print "BUSQUEDA LIMITADA EN PROFUNDIDAD Z-C"
print search.depth_limited_search(zc).path()
print
print "BUSQUEDA EN PROFUNDIDAD ITERATIVA Z-C"
print search.iterative_deepening_search(zc).path()
print
print "BUSQUEDA POR RAMIFICACION Y ACOTACION Z-C"
print search.branch_bound_tree_search(zc).path()
print
print "BUSQUEDA POR RAMIFICACION Y ACOTACION CON SUBESTIMACION Z-C"
print search.branch_bound_underestimates_tree_search(zc).path()
print
#print "BUSQUEDA POR A* Z-C"
#print search.astar_search(zc).path()
#print

de = search.GPSProblem('D', 'E', search.romania)

print "BUSQUEDA EN ANCHURA D-E"
print search.breadth_first_graph_search(de).path()
print
print "BUSQUEDA EN PROFUNDIDAD D-E"
print search.depth_first_graph_search(de).path()
print
print "BUSQUEDA LIMITADA EN PROFUNDIDAD D-E"
print search.depth_limited_search(de).path()
print
print "BUSQUEDA EN PROFUNDIDAD ITERATIVA D-E"
print search.iterative_deepening_search(de).path()
print
print "BUSQUEDA POR RAMIFICACION Y ACOTACION D-E"
print search.branch_bound_tree_search(de).path()
print
print "BUSQUEDA POR RAMIFICACION Y ACOTACION CON SUBESTIMACION D-E"
print search.branch_bound_underestimates_tree_search(de).path()
#print
#print "BUSQUEDA POR A* D-E"
#print search.astar_search(de).path()
"""