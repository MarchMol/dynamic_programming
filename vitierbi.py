import numpy as np

from decimal import Decimal, getcontext


def viterbi(obsv, states, start_p, trans_p, emit_p):
    getcontext().prec = 10000
    N = len(states)
    T = len(obsv)
    counter = 0
    p = [{}]
    d = {}
    # init
    for s in states:
        p[0][s] = start_p[s]*emit_p[s][obsv[0]]
        d[s] = [s]
    # bottom up
    for t in range(1,T):
        newpath = {}
        p.append({})
        
        for x in states:
            prob = Decimal(0)
            last_state = ""
            for y in states:
                counter+=1
                eval = Decimal(p[t-1][y])* Decimal(trans_p[y][x]) *  Decimal(emit_p[x][obsv[t]])
                if eval>prob:
                    prob = eval
                    last_state = y
            p[t][x] = prob
            newpath[x] = d[last_state]+[x]
        d = newpath

    (prob, state) = max([(p[-1][y], y) for y in states])
    return(prob, d[state])