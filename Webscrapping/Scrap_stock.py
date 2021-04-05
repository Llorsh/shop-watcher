# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 00:07:52 2021

@author: mkostner
"""

# elite center
import time
import urllib3
from tqdm import tqdm
from bs4 import BeautifulSoup
import pandas as pd
from colorama import init, Fore, Back, Style
init(convert=True)

print(Style.RESET_ALL)
# request


#import requests

urllib3.disable_warnings()
salida = pd.DataFrame()


# lista con los url
urls = ['https://www.pcfactory.cl/escritorio?categoria=737']
tienda = 'PC Factory'
for url in urls:  # loop url

    req = urllib3.PoolManager()
    r = req.request('GET', url)  # generamos el request
    # con transformamos el HTML a Soup
    soup = BeautifulSoup(r.data, 'html.parser')
    # buscamos la galeria de productos
    mydivs = soup.find_all("div", {"class": "wrap-caluga-matrix"})

    # print(mydivs[0])

    for i in range(len(mydivs)):  # iteramos por cada uno de los productos
        try:
            link = mydivs[i].a['href']  # sacamos el link
            # print(link)

            name = mydivs[i].findAll(
                'span', {'class': 'nombre'})[0].text.strip().upper()  # nombre del producto

            # nos quedamos solo con los productos que nos interesa
            if (True):
                stock = 'En Stock'  # como todos los productos que estan visibles están disponibles no buscamos el stock sino que le ponemos un string "En Stock"

                precio_efect = int(mydivs[i].findAll('span', {'class': 'price'})[
                                   0].text.strip().replace('$', '').replace('.', ''))  # precio

                # guardamos el resultado
                salida = salida.append(
                    [[tienda, name, precio_efect, "En stock", link]])

        except:
            pass

    try:
        # una vez que tenemos todos los resultados le cambiamos los nombres a las columndas
        salida.columns = ["Tienda", "Descripcion", "Efectivo", "stock", 'link']
    except:
        pass
