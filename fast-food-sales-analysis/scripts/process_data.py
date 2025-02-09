import pandas as pd

def load_and_process_data(file_path="Balaji Fast Food Sales.csv"):
    """
    Carrega e processa os dados do arquivo CSV.
    """
    df = pd.read_csv(file_path)
    
    # Converter a coluna de datas
    df['date'] = pd.to_datetime(df['date'], errors='coerce', dayfirst=True)

    # Criar colunas auxiliares
    df['month'] = df['date'].dt.strftime('%Y-%m')  # Ano-Mês
    df['day_of_week'] = df['date'].dt.day_name()   # Nome do dia da semana

    return df
