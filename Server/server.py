from graph import DiGraph
import algorithms    
from bottle import route, run, response, request
import result

@route('/buschange')
def returnsingle():
    source = request.GET.get('source')
    sink = request.GET.get('sink')
    rank = request.GET.get('rank')
	
    # Load the graph
    G = DiGraph("net5")    
    # Get the painting object and set its properties.
    paint = G.painter()
    paint.set_source_sink(source, sink)    
    # Generate the graph using the painter we configured.
    G.export(False, paint)
    i=int(rank)
    iRank = i
    # Get shortest paths from the graph.
    items = algorithms.ksp_yen(G, source, sink, i)
    for path in items:
        sCost = path['cost']
        sPath = ", ".join(path['path'])               
        response.content_type='application/json'
        if i==1:
            return { "BusChange": result.busChanger(source,sink,iRank) }
        else:
            i=i-1
            continue

@route('/pathavail')
def returnsingle():
    source = request.GET.get('source')
    sink = request.GET.get('sink')
    rank = request.GET.get('rank')
    
    # Load the graph
    G = DiGraph("net5")    
    # Get the painting object and set its properties.
    paint = G.painter()
    paint.set_source_sink(source, sink)    
    # Generate the graph using the painter we configured.
    G.export(False, paint)
    i=int(rank)
    iRank = i
    # Get shortest paths from the graph.
    items = algorithms.ksp_yen(G, source, sink, i)
    for path in items:
        sCost = path['cost']
        sPath = ", ".join(path['path'])               
        response.content_type='application/json'
        if i==1:
            return { "Cost": sCost, "Path": sPath }
        else:
            i=i-1
            continue

run(host='localhost', port=8080, debug=True)