import os  
from datetime import datetime, timedelta

SEGUNDOS_ANTES = 10 
SEGUNDOS_DEPOIS = 3

def extrair_data_do_nome(nome_arquivo): 

    texto_data = nome_arquivo.replace(".mp4", "")
    return datetime.strptime(texto_data, "%Y%m%d_%H%M%S")

def buscar_segmentos_do_intervalo(momento_do_clique): 
    inicio_janela = momento_do_clique - timedelta(seconds = SEGUNDOS_ANTES)
    fim_janela = momento_do_clique + timedelta(seconds = SEGUNDOS_DEPOIS) 

    arquivos_na_janela = []

    for nome_arquivo in os.listdir("buffer"): 
        data_do_arquivo = extrair_data_do_nome(nome_arquivo) 

        if inicio_janela <= data_do_arquivo <= fim_janela: 
            arquivos_na_janela.append(nome_arquivo) 

    arquivos_na_janela.sort()
    return arquivos_na_janela 

momento_simulado = datetime.now()
print(f"Simulando clique às: {momento_simulado}")

resultado = buscar_segmentos_do_intervalo(momento_simulado)

print(f"Segmentos encontrados na janela ({len(resultado)}):")

for nome in resultado:
    print(f"  - {nome}")


    
                                      