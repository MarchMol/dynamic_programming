import numpy as np

def forward(obs, states, start_prob, trans_prob, emit_prob):
    T = len(obs)
    N = len(states)
    alpha = []
    for t in range(T):
        tem = {}
        for i in states:
            tem[i] = 0
        alpha.append(tem)

    for i in states:
        alpha[0][i] = start_prob[i] * emit_prob[i][obs[0]]

    for t in range(1, T):
        for j in states:
            alpha[t][j] = emit_prob[j][obs[t]] * sum(alpha[t-1][j] * trans_prob[i][j] for i in states)

    return alpha

def backward(obs, states, trans_prob, emit_prob):
    T = len(obs)
    N = len(states)
    beta = []
    for o in obs:
        tem = {}
        for i in states:
            tem[i] = 0
        beta.append(tem)

    for t in range(T-2, -1, -1):
        for i in states:
            beta[t][i] = sum(trans_prob[i][j] * emit_prob[j][obs[t+1]] * beta[t+1][j] for j in states)

    return beta

def divide_and_conquer_viterbi(obs, states, start_prob, trans_prob, emit_prob):
    T = len(obs)
    if T == 1:
        prob, state = max(
            ((start_prob[i] * emit_prob[i][obs[0]], i) for i in states),
            key=lambda x: x[0])
        print("BASE: ",state)
        return [state]

    mid = T // 2

    alpha = forward(obs[:mid], states, start_prob, trans_prob, emit_prob)

    beta = backward(obs[mid:], states, trans_prob, emit_prob)


    alpha_mid = alpha[mid - 1] 
    beta_mid = beta[0]


    scores = {state: alpha_mid[state] * beta_mid[state] for state in alpha_mid}
    best_mid_state = max(scores, key=scores.get)

    left_path = divide_and_conquer_viterbi(obs[:mid], states, start_prob, trans_prob, emit_prob)
    right_path = divide_and_conquer_viterbi(obs[mid:], states, start_prob, trans_prob, emit_prob)

    return left_path + right_path


estados = ["Sunny", "Rainy"]
observaciones = ["Walk","Walk","Walk","Walk"]
start_prob = {'Sunny': 0.4, 'Rainy': 0.6}
trans_prob = {
    "Sunny": {"Sunny": 0.6, "Rainy": 0.4 },
    "Rainy": {"Sunny": 0.3, "Rainy": 0.7 }
}
emit_prob = {
    "Sunny": {"Walk": 0.6, "Shop": 0.3, "Clean": 0.1},
    "Rainy": {"Walk": 0.1, "Shop": 0.4, "Clean": 0.5}
}

# Run the divide-and-conquer Viterbi algorithm
best_sequence = divide_and_conquer_viterbi(observaciones, estados, start_prob, trans_prob, emit_prob)

print("Most likely state sequence:", best_sequence)