import vitierbi
import dac
import random
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
from scipy.stats import linregress


# Informacion de entrada para los algoritmos
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

# Comprobacion de funcionamiento para ambos algoritmos
def test():
    obs_test = ["Walk","Walk","Clean"]
    vit = vitierbi.viterbi(obs_test, estados, start_prob, trans_prob, emit_prob)
    dac_ = dac.divide_and_conquer_viterbi(obs_test, estados, start_prob, trans_prob, emit_prob)
    print(f"Viterbi: {vit}")
    print(f"DaC: {dac_}")

def empiric(N):
    data = {"iter": [], "v_time": [],"d_time": []}
    possible_obs = ["Walk","Shop","Clean"]
    for i in range(1,N):
        data["iter"].append(i)
        rand_observations = random.choices(possible_obs, k=i)
        # Viterbi
        start = time.time() * 1000 # in ms
        vitierbi.viterbi(rand_observations, estados, start_prob, trans_prob, emit_prob)
        data["v_time"].append( (time.time()* 1000)-start)
        # DaC
        start = time.time() * 1000 # in ms
        dac.divide_and_conquer(rand_observations, estados, start_prob, trans_prob, emit_prob)
        data["d_time"].append( (time.time()* 1000)-start)
    return pd.DataFrame(data)
        

def empiric_analysis():
    data = empiric(700)
    X = data.pop("iter")
    y_vit = data.pop("v_time")
    y_dac = data.pop("d_time")

    slope, intercept, r_value_lin, _, _ = linregress(X, y_vit)
    y_pred_linear = slope * X + intercept
    r2_linear = r_value_lin ** 2
    
    
    coeffs = np.polyfit(X, y_dac, 2)
    y_pred_quad = np.polyval(coeffs, X)
    ss_res = np.sum((y_dac - y_pred_quad) ** 2)
    ss_tot = np.sum((y_dac - np.mean(y_dac)) ** 2)
    r2_quad = 1 - (ss_res / ss_tot)
    
    plt.scatter(X, y_vit, color='lightblue', label=f'Viterbi | O(n) (R²={r2_linear:.4f})')
    plt.scatter(X, y_dac, color='pink', label=f'DaC | O(n²) (R²={r2_quad:.4f})')
    plt.plot(X, y_pred_linear, color='blue', linestyle='-')
    plt.plot(X, y_pred_quad, color='red', linestyle='-')
    

    # Labels and legend
    plt.xlabel("Lonngitud de entrada (n)")
    plt.ylabel("Tiempo de ejecucion (ms)")
    plt.title("Viterbi y DaC: n vs Tiempo de ejecucion (N=700)")
    plt.legend()
    plt.show()
            
empiric_analysis()