# 📂 src/filter_by_date.py - Filtrado dinámico por fecha proceso

import pandas as pd

def filter_by_date(df, fecha_proceso):
    df_filtered = df[df['fecha'] == fecha_proceso]
    return df_filtered

if __name__ == "__main__":
    df = pd.read_csv("data/datos.csv")
    fecha_proceso = "2024-05-01"
    df_filtrado = filter_by_date(df, fecha_proceso)
    print(df_filtrado.head())