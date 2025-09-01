import os
import requests
from bs4 import BeautifulSoup
import pandas as pd

def naredi_html_tabele_finviz(stevilo_strani=5, mapa_izhod="finviz_strani"):
    prvi_url = "https://finviz.com/screener.ashx?v=152&f=cap_midover,fa_div_high&o=-dividendyield&c=0,1,2,3,4,5,6,75,14,67,65"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    os.makedirs(mapa_izhod, exist_ok=True)

    for stran in range(1, 6):
        if stran == 1:
            url = prvi_url
        else:
            r = 1 + (stran - 1) * 20
            url = f"{prvi_url}&r={r}"

        r = requests.get(url, headers=headers)
        if r.status_code != 200:
            print(f"Napaka ({r.status_code}) na strani {stran}")
            continue

        
        soup = BeautifulSoup(r.text, "lxml")
        tabela = soup.select_one("table.screener_table")
        if tabela is None:
            blok = soup.select_one("#screener-table")
            if blok:
                tabela = blok.find("table", class_="screener_table")
        if tabela is None:
            print(f"Ni tabele na strani {stran}")
            continue
        
        html_stran = "<!doctype html><meta charset='utf-8'>\n" + str(tabela)

        kam  = os.path.join(mapa_izhod, f"tabela_stran{stran}.html")
        with open(kam, "w", encoding="utf-8") as f:
            f.write(html_stran)

naredi_html_tabele_finviz(stevilo_strani=5, mapa_izhod="finviz_strani")

poti = [os.path.join('finviz_strani', f'tabela_stran{i}.html') for i in range(1, 6)]

podatki = [pd.read_html(p, flavor="lxml")[0] for p in poti]

df = pd.concat(podatki, ignore_index=True)





out_csv = os.path.join('finviz_screener.csv')
df.to_csv(out_csv, index=False, encoding='utf-8-sig')
print(f"Shranjeno: {os.path.abspath(out_csv)} ({len(df)} vrstic)")