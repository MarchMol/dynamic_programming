import numpy as np

from decimal import Decimal, getcontext

def forward(obs, states, start_prob, trans_prob, emit_prob):
    T = len(obs)
    N = len(states)
    alpha = []
    for t in range(T):
        tem = {}
        for i in states:
            tem[i] = Decimal(0)
        alpha.append(tem)

    for i in states:
        alpha[0][i] = Decimal(start_prob[i]) * Decimal(emit_prob[i][obs[0]])

    for t in range(1, T):
        for j in states:
            alpha[t][j] = Decimal(emit_prob[j][obs[t]]) * sum(Decimal(alpha[t-1][j]) * Decimal(trans_prob[i][j]) for i in states)

    return alpha

def backward(obs, states, trans_prob, emit_prob):
    T = len(obs)
    N = len(states)
    beta = []
    for o in obs:
        tem = {}
        for i in states:
            tem[i] = Decimal(0)
        beta.append(tem)

    for t in range(T-2, -1, -1):
        for i in states:
            beta[t][i] = sum(Decimal(trans_prob[i][j]) * 
                             Decimal(emit_prob[j][obs[t+1]]) * 
                             Decimal(beta[t+1][j]) for j in states)

    return beta

def divide_and_conquer(obs, states, start_prob, trans_prob, emit_prob):
    getcontext().prec = 10000
    T = len(obs)
    if T == 1:
        prob, state = max(
            ((Decimal(start_prob[i] * emit_prob[i][obs[0]]), i) for i in states),
            key=lambda x: x[0])
        return [state]

    mid = T // 2

    alpha = forward(obs[:mid], states, start_prob, trans_prob, emit_prob)

    beta = backward(obs[mid:], states, trans_prob, emit_prob)


    alpha_mid = alpha[mid - 1] 
    beta_mid = beta[0]


    scores = {state: Decimal(alpha_mid[state]) * Decimal(beta_mid[state]) for state in alpha_mid}
    best_mid_state = max(scores, key=scores.get)

    left_path = divide_and_conquer(obs[:mid], states, start_prob, trans_prob, emit_prob)
    right_path = divide_and_conquer(obs[mid:], states, start_prob, trans_prob, emit_prob)

    return left_path + right_path
