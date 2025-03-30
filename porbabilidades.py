# Soleado, nublado, lloviendo
estados = ["Soleado", "Nublado", "Lloviendo"]

# Nivel de humedad bajo, medio y alto
observaciones = ["Bajo","Medio","Alto"] 

trans_prob = {
    "Soleado": {
        "Soleado": 0.6,
        "Nublado": 0.3,
        "Lloviendo": 0.1
        },
    "Nublado": {
            "Soleado": 0.4,
            "Nublado": 0.3,
            "Lloviendo": 0.3
        },
    "Lloviendo": {
            "Soleado": 0.2,
            "Nublado": 0.3,
            "Lloviendo": 0.5
    }
}

trans_prob = {
    "Soleado": {
        "Bajo": 0.3,
        "Medio": 0.2,
        "Alto": 0.5
    },
    "Nublado": {
        "Bajo": 0.3,
        "Medio": 0.4,
        "Alto": 0.3
    },
    "Lloviendo": {
        "Bajo": 0.1,
        "Medio": 0.3,
        "Alto": 0.6
    }
}