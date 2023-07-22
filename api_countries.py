import requests


def listar_nombres_paises(url):
     paises = requests.get(url)
     paises = paises.json()

     for pais in paises:
        print(f"Nombre Oficial en Español: {pais['translations']['spa']['official']}")
        print(f"La capital es: {pais['capital'][0]}")
        moneda = pais['currencies']
        for mon in moneda.values():
            print(f"Nombre de la moneda: {mon['name']}")
            print(f"Su simbolo es: {mon['symbol']}")
        codtelf= pais['idd']['root'] + pais['idd']['suffixes'][0]
        print(f"El código telefónico: {codtelf}")




url = 'https://restcountries.com/v3.1/independent?status=true&fields=translations,capital,currencies,idd'
listar_nombres_paises(url)