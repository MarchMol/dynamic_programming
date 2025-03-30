# Soleado, nublado, lloviendo
estados = ["Sunny", "Rainy"]

# Nivel de humedad bajo, medio y alto
observaciones = ["Walk","Shop","Clean"] 

trans_prob = {
    "Sunny": {
        "Sunny": 0.6,
        "Rainy": 0.4,
        },
    "Rainy": {
        "Sunny": 0.3,
        "Rainy": 0.7,
    },
}

start_prob = {'Sunny': 0.4, 'Rainy': 0.6}
emit_prob = {
    "Sunny": {
        "Walk": 0.6,
        "Shop": 0.3,
        "Clean": 0.1
    },
    "Rainy": {
        "Walk": 0.1,
        "Shop": 0.4,
        "Clean": 0.5

    },
}

import numpy as np
def viterbi(secuencia):
    N = len(estados)
    T = len(secuencia)
    p = [0]*(N*T)
    d = [0]*(N*T)
   
    # init
    for i,s in enumerate(estados):
        p[i] = start_prob[s]*emit_prob[s][secuencia[0]]
    prev_state = estados[np.argmax(p[:N])]
    # bottom up
    for t in range(1,T):
        max_prob = 0
        for i,s in enumerate(estados):
            tem = (p[i+(t-1)*N] * 
            trans_prob[prev_state][s]*
            emit_prob[s][secuencia[t]])
            print(f"V{t}({s}) = {p[i+(t-1)*N]}")
            if tem>max_prob:
                max_prob = p[i+(t)*N]
                prev_state = estados[d[i+(t)*N]]
    
    print(p)
    # best_start = np.argmax(p[:N])
    # best_path = [best_start]
    # for t in range(T-1, 0, -1):
    #     best_path.insert(0,d[best_path[0]])
    # print(best_path)
    # # # Convert indices back to state names
    # best_state_seq = [estados[i] for i in best_path]
    # print(best_state_seq)

    
secuencia = ["Walk","Shop","Clean"]
viterbi(secuencia)