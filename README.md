#  Analiza delnic
Pri predmetu **Uvod v programiranje**, sem se odločil analizirati podatke o 100 delnicah z najvišjim dividendnim donosom. Podatke sem dobil iz spletne strani https://finviz.com/,
s katere sem ustvaril 5 html strani iz katerih funkcija pobere te podatke.


##  Kaj naredi koda?

1. **Prenos 5 HTML  strani** s Finviz screenerja.  
2. **Shranjevanje HTML strani** v mapo `finviz_strani/`.  
3. **Branje tabel** z `pandas.read_html`.  
4. **Združevanje** vseh strani v enoten `DataFrame`.  
5. **Shranjevanje v CSV** (`finviz_screener.csv`).  


##  Struktura kode

- **`naredi_html_tabele_finviz`** – funkcija, ki prenese HTML tabele in jih shrani lokalno.  
- **`poti`** – seznam poti do shranjenih `.html` datotek.  
- **`podatki`** – seznam pandas DataFrame-ov, po en za vsako stran.  
- **`df`** – združen DataFrame vseh delnic.  
- **`out_csv`** – končni CSV izvoz (`finviz_screener.csv`).  

---

##  Uporaba

1. Namesti potrebne knjižnice:
   pip install requests beautifulsoup4 pandas lxml
2. Zaženi program 

