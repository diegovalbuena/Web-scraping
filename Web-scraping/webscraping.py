# WEBSCRAPING :
#pip install beautifulsoup4
from bs4 import BeautifulSoup
from urllib.request import urlopen

def pagina():
    """
    Extrae la información del sitio web guardandola en el archivo .txt llamado "Archivo_corferias"
    :param none:
    :return: none.
    """
    url = "https://corferias.com/?doc=calendario_ferial&ids=4&intAno=2021&intIdioma=1&StrIdioma=es"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    texto = soup.get_text()
    lineas = [linea for linea in texto.split('\n') if linea != '']
    texto_limpio = '\n'.join(lineas)
    archivo_externo = open("Archivo_corferias.txt","w")
    archivo_externo.write(texto_limpio)
    archivo_externo.close()

def informacion():
    """
    Busca  en el  "archivo_corferias" la informacion del nombre o el link, la descripcion
     y la fecha del evento, añade esta informacion a  listas.
    :param none:
    :return: links | fechas | informacion.
    """
    archivo_externo = open("Archivo_corferias.txt", "r")
    j = 0
    links=[]
    fechas=[]
    informacion=[]
    link = [" "]
    for line in archivo_externo.readlines():
        j = j + 1
        line = str(line)
        line = line.split(' ')
        if line[0] == "Del":
            links.append(link)
            fechas.append(line)
        elif link[0] == "Información" and link[1] == "General\n":
            informacion.append(line)
        link = line
    archivo_externo.close()
    return links,fechas,informacion

def datos(links,fechas,informacion):
    """
    Muestra de forma organizada los datos de cada convencion y los guarda en un archivo .txt llamado
    "Archivo_datos_convenciones".
    :param list[string] links: lista de los links de los eventos.
    :param list[string] fechas: lista de las fechas de los eventos.
    :param list[string] informacion: lista de la descripcion de los eventos.
    :return: none
    """
    archivo= open("Archivo_datos_convenciones.txt","w")
    for j in range(len(links)):
        print(" CONVENCION " + str(j + 1))
        archivo.write(" CONVENCION " + str(j + 1) + "\n")
        print(" Link: ", end="")
        for i in links[j]:
            archivo.write(" " + i)
            print(str(i), end= " ")
        print("Fecha: " , end="")
        for i in fechas[j]:
            archivo.write(" " + i + " ")
            print(str(i), end= " ")
        print("Informacion general: ", end= "")
        for i in informacion[j]:
            archivo.write(i + " ")
            print(str(i), end= " ")
        archivo.write("//////////////////" + "\n")
        print("//////////////////")
    archivo.close()

def main():
    pagina()
    num1 = informacion()
    datos(num1[0],num1[1],num1[2])

main()