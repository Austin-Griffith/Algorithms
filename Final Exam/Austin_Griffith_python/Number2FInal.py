import random
import math


############################################### START OF PROBLEM 2 IMPLEMENTATION ########################################################################  

#STEPS:
# convert from inputs to minimun routing 
# convert from minimun routing to ford fulkerson
# ford fulkerson 

def getPath(G, v, sink, path):      #takes in a graph, a starting point (v) and destination (sink)  finds path between them from any vertex  

  #print(v,path)
  for destination in G[v]:      # loops over all nodes that v traverse too  

    if (destination in path):   #never travserve a vertex more than once  ---> avoid a cycle 
      continue

    if (G[v][destination] > 0):       #checking capacity of edge that we are trying to move along 
      #print(G[v][destination])

      if (destination == sink):         #case where v directly points to sink of graph  
        #print(G)
        return path + [ v,sink ]        #return the full path of vertices 

      pathAttempt = getPath(G, destination, sink, path + [v] )      #finding if you can get from current vertex to sink via destination to sink  --> keeping track of path as you move along 

      if sink in pathAttempt:           #if destination was in the pathAttempt then return that list 
        return pathAttempt

  return []             # return an empty list if no path to destination from cuurent vertex            



#fordFulkerson implementation will solve for max flow
def fordFulkersonMod(G, s, d):      #takes in Graph, source, destination 

  while True:
      pathVerts = getPath(G, s, d, [] )   #pathVerts sets to augmented path if one exsits of vertices along the path; otherwise set to empty list 
      path = []               # path holds a list of edges along the path 

      for i in range( len(pathVerts) - 1 ):         #looping through pathVerts to add edges to path[]
          path += [ (pathVerts[i], pathVerts[i+1]) ]    #adding the pair from pathVerts at i to the next on the path 

      if len(path) == 0:      #if no augmented path found then break from loop  ----> algorithm has found max flow
            break

      flow = G[path[0][0]][path[0][1]]      # initializing flow to be pushed through path to be capacity of the first edge 
      
      for edge in path:
              if ( G[ edge[0] ][ edge[1] ] < flow ):        # if any edge has a lower capacity, restrict the flow to that capacity 
                      flow = G[ edge[0] ][ edge[1] ]      
                
      # if flow == 0:
      #   break

      #print(path)  

      for edge in path:           #loop to push flow through the given path 
        G[ edge[0] ][edge[1] ] -= flow    # decrement the capacity of an edge along the path by the amount of flow    

        if not edge[1] in G:
          G[edge[1]] = {} 

        if not edge[0] in G[edge[1]]:
          G[edge[1]][edge[0]] = 0 

        G[edge[1]][edge[0]] += flow     #increase capacity of going back along of edge by amount that was pushed through  ---  representing the possible to redirect flow 

      print(flow) 

      

  return G    #return and augmented graph  ----> when we have finish maximized flow from  s ----> d 



# an example input to test if our routing solver works. it does.
E = { "a": { "c": 1, "d": 1 }, # E is the capacities for each edge
      "b": { "c": 1, "d": 1 },
      "c": {},
      "d": {},
    }
V = { "a": -1, "b": -2, "c": 2, "d": 1 }              # V is the routing function at each vertex

#print(fordFulkerson(E,"a","c"))                # this tests that the max flow problem works without considering any routing



# solves a routing given edge capacities (E) and a routing function (V)
def isRouting( E, V ):                  
  E["source"] = {}                             # we transform a routing problem into a problem of maximizing flow by connecting a source to all vertices with negative routing functions and connecting all vertices with positive routing functions to a sink, to maximize flow from that source to that sink. we know a routing is feasible if this maximum flow saturates all added edge.
  V["source"] = 0 
  
  for v in E:                                  # go through each vertex and add the proper edges depending on the routing function at that vertex
    if V[v] < 0:
      E["source"][v] = -V[v]                     # this and E[v]["sink"] = V[v] add the proper edges with capacity |V[v]| as described in PS9#1
    elif V[v] > 0:
      E[v]["sink"] = V[v]
  
  #print(E, "\n", "\n")
  
  fordFulkerson(E, "source", "sink")              # calculate the maximum flow of this modified graph (E was modified)
  
  #print(E)                                  # check if this maximum flow saturates any edge that is connected to source or sink
  for e in E["source"]:                        # check all of the edges that the source is connected to
    
    if E["source"][e] > 0:                      # if any of these edges still have capacity, they weren't saturated
      return False;                           # so we return False -- there is no flow that satisfies this routing function
  
  for v1 in E:                              # check all of the edges that are connected to the sink
    for v2 in E[v1]:
      if v2 == "sink":
        if E[v1][v2] > 0:                     # if any of these edges still have capacity, they weren't saturated
          return False;                      # so we return False -- there is no flow that satisfies this routing function
          
  return True;                            # at this point we know that the maximum flow saturated all new edges, and so we can satisfy the routing function

#print(isRouting(E,V))                        # this was the test mentioned above about seeing if we correctly solve a routing problem

Emin = { "a": { "c": 0, "d": 0 },               # we now impose minimums on the edges in a routing function; we keep these data structures separate for convenience rather than for efficiency
         "b": { "c": 0, "d": 0 },               # these are all zero, which wouldn't make a difference, but tweaking the values indicates that our implementation of isMinEdgeRouting works
         "c": {},
         "d": {} }



# solves whether a routing of flow satisfies the routing function, given edge capacities and the minimum required flow along each edge
def isMinEdgeRouting( Emax, Emin, V ): 


  E = {}                                # we create a new adjacency list of edges as to formulate the minimum edge routing as a pure routing
  for v1 in Emax:
    for v2 in Emax[v1]:
      if not v1 in E:                   # add the containing dictionary to E if v1 isn't in it yet so that we can add elements to that dictionary to represent edges
        E[v1] = {}
      
      E[v1][v1 + "." + v2 + ".v'"] = Emax[v1][v2]; 
      
      if not v1 + "." + v2 + ".v'" in E: 
        E[v1 + "." + v2 + ".v'"] = {}
      if not v1 + "." + v2 + ".w'" in E:
        E[v1 + "." + v2 + ".w'"] = {}
        
      E[v1 + "." + v2 + ".v'"][v1 + "." + v2 + ".w'"] = Emax[v1][v2] - Emin[v1][v2];              # we set the new edge capacities as described in PS9#1b
      E[v1 + "." + v2 + ".w'"][v2] = Emax[v1][v2];
      V[v1 + "." + v2 + ".v'"] = Emin[v1][v2];                                              # we set the new routing function as described in PS9#1b
      V[v1 + "." + v2 + ".w'"] = -Emin[v1][v2];
  
  return isRouting( E, V );                           # since we now reduced the problem into a pure routing problem, we can test if that problem is satisfiable
  

# setup / 2e begins here

n = 10        # number of issues 
m = 1000          #number of people
bptp = {}     #the range of number of question allowed to ask each person  ---> disctionary of pairs  
          #  bptp[ p ] = ( b_p , t_p ) for 0 <=  p <= m-1
  
li_ui = {}      # li_ui[ i ] = ( l_i , u_i ) for 0 <= i <= n-1
          # li is the number of responses needed for a given question     u_i is the number of times you can ask about a given question 

opinions = []   # list of pairs ( p , i ) representing that a person has an opinion about issue i 

# For any person p and for any issue i, s/he has a probability of 50% to have an opinion about the issue, i.e there is a 50% probability that there is a link from p to i in the graph G

for p in range(m):
  hP = 0        #number of issues   ---> variable for counting number of issue that p has an opinion about 

  for i in range(n):              #looping over all issues to see if p has an opinion about it 
    # these are all issue-person pairs 

    if (random.randint(0,1) == 0):    
      #add link 
      opinions += [ (p, i) ]      #adds pair to opinions list of pairs 

      hP += 1
  bptp[ p ] = ( math.floor( hP / 2) , hP )

for i in range( n ):                          #looping over all issues to decide l_i and u_i for each issue i 

  li_ui[ i ] = ( random.randint(300,400)) , random.randint(500,700) # pair of ( l_i , u_i )


 # G, M, R was a test to see if our particular reformulation of the inputs as a minimum routing worked (an example output of what's described in 1a, assuming we already converted the inputs into this form)
G = { "a": { "b": 3, "c": 1, "d": 2, "e": 2, "f": 2 },
      "b": { "g": 1, "h": 1, "i": 1 },
      "c": { "g": 1, "h": 0, "i": 1 },
      "d": { "g": 1, "h": 0, "i": 1 },
      "e": { "g": 0, "h": 0, "i": 1 },
      "f": { "g": 0, "h": 0, "i": 1 },
      "g": { "j": 5 },
      "h": { "j": 4 },
      "i": { "j": 3 },
      "j": { "a": 12 }
}

M = { "a": { "b": 2, "c": 1, "d": 1, "e": 1, "f": 1 },
      "b": { "g": 0, "h": 0, "i": 0 },
      "c": { "g": 0, "h": 0, "i": 0 },
      "d": { "g": 0, "h": 0, "i": 0 },
      "e": { "g": 0, "h": 0, "i": 0 },
      "f": { "g": 0, "h": 0, "i": 0 },
      "g": { "j": 2 },
      "h": { "j": 1 },
      "i": { "j": 2 },
      "j": { "a": 5 }
}

R = { "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g":0, "h":0, "i":0, "j":0 }

G = {}      # conversion / 2a begins here
M = {}
R = {}

minItotal = 0;          # these are a shitty way to restrict the flow along the backwards edge (edge that goes from the sink back to the source) for converting the input into a routing with minimums problem
maxItotal = 0;
minPtotal = 0;
maxPtotal = 0;


for o in opinions:                           # go through every opinion (pairs (p, i) representing that person p has an opinion about issue i) and connect each person to each issue that they have an opinion about
  if not "p"+str(o[0]) in G:                  # add containing dictionaries to the graph structure if needed
    G["p"+str(o[0])] = {}
    M["p"+str(o[0])] = {}
  G["p"+str(o[0])]["i"+str(o[1])] = 1;              # set the capacity of the edge connecting person p with issue i to be 1, represeting that you can only ask a person about one question once, or rather you will only get one answer out of questioning him about it
  M["p"+str(o[0])]["i"+str(o[1])] = 0;               # and set the minimum to zero, representing that you don't have to ask a person about any given question

for p in bptp:                         # go through the bptp input and connect the source to each person
  minPtotal += bptp[p][0]               # update the totals for the edge that goes from the sink d back to the source s
  maxPtotal += bptp[p][1]
  
  R["p"+str(p)] = 0;                    # set the demand of any added vertex to be zero, in this case for each person
  if not "s" in G:                      # initialize dictionary of adjacent capacities for G["s"]
    G["s"] = {}
  if not "s" in M:                      # initialize dictionary of adjacent minimums for M["s"]
    M["s"] = {}
  G["s"]["p"+str(p)] = bptp[p][1]         # connect the source to each person with the proper capacities
  M["s"]["p"+str(p)] = bptp[p][0]          # and minimums
for i in li_ui:                        # go through the liui input and connect each issue to the sink
  minItotal += li_ui[i][0]           # update the totals for the edge that goes from the sink d back to the source s
  maxItotal += li_ui[i][1]
  
  R["i"+str(i)] = 0;                  # set the demand of any added vertex to be zero, in this case for each issue
  if not "i"+str(i) in G:             # initialize dictionary of adjacent capacities for G[issue i]
    G["i"+str(i)] = {}
  if not "i"+str(i) in M:             # initialize dictionary of adjacent minimums for M[issue i]
    M["i"+str(i)] = {}
  G["i"+str(i)]["d"] = li_ui[i][1]     # connect each issue to the sink with the proper capacities
  M["i"+str(i)]["d"] = li_ui[i][0]    # and minimums
G["d"] = {}                           # initialize dictionary for the backwards edge
# G["d"]["s"] = 10000;
G["d"]["s"] = min( maxItotal, maxPtotal )       # this..
M["d"] = {}
# M["d"]["s"] = 0;
M["d"]["s"] = max( minItotal, minPtotal )       # ..and this restrict the flow along the backwards edge
R["s"] = 0;                             # set the demands at the source and sink to be zero, as these we didn't set while looping through people and issues
R["d"] = 0;





# print(G)
print( isMinEdgeRouting( G, M, R ) )      # now, having converted the input into a problem of satisfying a routing with minimums, we see if the input specified by part e is feasible. 
                                          #this takes particularly long to run, but has returned True in each of the five runs that I've completed. this indicates that these generated parameters are particularly feasible. 
                                          #the run times for this vary a lot and have taken my even my powerful desktop about 2 1/2 hours to return True

#print( isMinEdgeRouting( E, Emin, V ) ) # this was just an earlier test
