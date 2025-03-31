import numpy as np
from pprint import pprint
def viterbi(obsv, states, start_p, trans_p, emit_p):
    N = len(states)
    T = len(obsv)
    
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
            prob = 0
            last_state = ""
            for y in estados:
                eval = p[t-1][y] * trans_p[y][x] *  emit_p[x][obsv[t]]
                if eval>prob:
                    prob = eval
                    last_state = y
            p[t][x] = prob
            newpath[x] = d[last_state]+[x]
        d = newpath

    (prob, state) = max([(p[-1][y], y) for y in states])
    return(prob, d[state])

estados = ["Sunny", "Rainy"]
observaciones = ["Walk","Shop","Clean"]
start_prob = {'Sunny': 0.4, 'Rainy': 0.6}
trans_prob = {
    "Sunny": {"Sunny": 0.6, "Rainy": 0.4 },
    "Rainy": {"Sunny": 0.3, "Rainy": 0.7 }
}
emit_prob = {
    "Sunny": {"Walk": 0.6, "Shop": 0.3, "Clean": 0.1},
    "Rainy": {"Walk": 0.1, "Shop": 0.4, "Clean": 0.5}
}

rslt = viterbi(observaciones, estados, start_prob, trans_prob, emit_prob)
print(rslt)