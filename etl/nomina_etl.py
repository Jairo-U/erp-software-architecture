import pandas as pd

def procesar_nomina():
    data = {
        "empleado": ["Ana", "Carlos", "Luis"],
        "salario_mensual": [2000, 2500, 1800]
    }

    df = pd.DataFrame(data)
    df["salario_anual"] = df["salario_mensual"] * 12

    return df

if __name__ == "__main__":
    print(procesar_nomina())
