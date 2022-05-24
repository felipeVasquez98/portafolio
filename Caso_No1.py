#!/usr/bin/env python
# coding: utf-8

# # Caso de Negocio No. 1:

# In[1]:


#Caso de Negocio No. 1:

import tkinter
from tkinter import messagebox
import requests
#from requests_html import AsyncHTMLSession
#from requests_html import HTMLSession
from bs4 import BeautifulSoup


# In[2]:


ventana = tkinter.Tk()
ventana.title("LISTA POKEMONES")
ventana.geometry("600x450")
ventana.config(bg="gray")

poke_menu = tkinter.Menu(ventana)
poke_menu.add_command(label='AQUÍ PODRÁS VER TUS POKEMONES :') 
ventana.config(menu=poke_menu)



# ------------------------------------------------- PODERES POKEMONES ----------------------------------------------------------

'''
asession = AsyncHTMLSession()
resp1 = await asession.get('https://pokeapi.co/API/V2/POKEMON/NOMBREPOKEMON')
print(resp1)

session = HTMLSession()
resp2 = session.get('https://pokeapi.co/API/V2/POKEMON/NOMBREPOKEMON')
print(resp2)
'''



#Poderes Spearow
url_spearow = 'https://pokeapi.co/api/v2/pokemon/spearow'
resp_spearow = requests.get(url_spearow)
soup_spearow = BeautifulSoup(resp_spearow.content, 'html.parser')
soup_read_spearow = soup_spearow.get_text()

pos_poder1_spearow = soup_read_spearow.find('name')
poder1_spearow = soup_read_spearow[pos_poder1_spearow+7:pos_poder1_spearow+15].upper()
#print(poder1_spearow)

pos_poder2_spearow = soup_read_spearow.find('name')
poder2_spearow = soup_read_spearow[pos_poder2_spearow+112:pos_poder2_spearow+118].upper()
#print(poder2_spearow)



#Poderes Fearow
url_fearow = 'https://pokeapi.co/api/v2/pokemon/fearow'
resp_fearow = requests.get(url_fearow)
soup_fearow = BeautifulSoup(resp_fearow.content, 'html.parser')
soup_read_fearow = soup_fearow.get_text()

pos_poder1_fearow = soup_read_fearow.find('name')
poder1_fearow = soup_read_fearow[pos_poder1_fearow+7:pos_poder1_fearow+15].upper()
#print(poder1_fearow)

pos_poder2_fearow = soup_read_fearow.find('name')
poder2_fearow = soup_read_fearow[pos_poder2_fearow+112:pos_poder2_fearow+118].upper()
#print(poder2_fearow)



#Poderes Ekans
url_ekans = 'https://pokeapi.co/api/v2/pokemon/ekans'
resp_ekans = requests.get(url_ekans)
soup_ekans = BeautifulSoup(resp_ekans.content, 'html.parser')
soup_read_ekans = soup_ekans.get_text()

pos_poder1_ekans = soup_read_ekans.find('name')
poder1_ekans = soup_read_ekans[pos_poder1_ekans+7:pos_poder1_ekans+17].upper()
#print(poder1_ekans)

pos_poder2_ekans = soup_read_ekans.find('name')
poder2_ekans = soup_read_ekans[pos_poder2_ekans+114:pos_poder2_ekans+123].upper()
#print(poder2_ekans)

pos_poder3_ekans = soup_read_ekans.find('name')
poder3_ekans = soup_read_ekans[pos_poder3_ekans+220:pos_poder3_ekans+227].upper()
#print(poder3_ekans)



#Poderes Arbok
url_arbok = 'https://pokeapi.co/api/v2/pokemon/arbok'
resp_arbok = requests.get(url_arbok)
soup_arbok = BeautifulSoup(resp_arbok.content, 'html.parser')
soup_read_arbok = soup_arbok.get_text()

pos_poder1_arbok = soup_read_arbok.find('name')
poder1_arbok = soup_read_arbok[pos_poder1_arbok+7:pos_poder1_arbok+17].upper()
#print(poder1_arbok)

pos_poder2_arbok = soup_read_arbok.find('name')
poder2_arbok = soup_read_arbok[pos_poder2_arbok+114:pos_poder2_arbok+123].upper()
#print(poder2_arbok)

pos_poder3_arbok = soup_read_arbok.find('name')
poder3_arbok = soup_read_arbok[pos_poder3_arbok+220:pos_poder3_arbok+227].upper()
#print(poder3_arbok)



#Poderes Pikachu
url_pika = 'https://pokeapi.co/api/v2/pokemon/pikachu'
resp_pika = requests.get(url_pika)
soup_pika = BeautifulSoup(resp_pika.content, 'html.parser')
soup_read_pika = soup_pika.get_text()

pos_poder1_pikachu = soup_read_pika.find('name')
poder1_pikachu = soup_read_pika[pos_poder1_pikachu+7:pos_poder1_pikachu+13].upper()
#print(poder1_pikachu)

pos_poder2_pikachu = soup_read_pika.find('name')
poder2_pikachu = soup_read_pika[pos_poder2_pikachu+109: pos_poder2_pikachu+122].upper()
#print(poder2_pikachu)



#Poderes Raichu
url_raichu = 'https://pokeapi.co/api/v2/pokemon/raichu'
resp_raichu = requests.get(url_raichu)
soup_raichu = BeautifulSoup(resp_raichu.content, 'html.parser')
soup_read_raichu = soup_raichu.get_text()


pos_poder1_raichu = soup_read_raichu.find('name')
poder1_raichu = soup_read_raichu[pos_poder1_raichu+7:pos_poder1_raichu+13].upper()
#print(poder1_raichu)

pos_poder2_raichu = soup_read_raichu.find('name')
poder2_raichu = soup_read_raichu[pos_poder2_raichu+109: pos_poder2_raichu+122].upper()
#print(poder2_raichu)



#Poderes Sandshrew
url_sandshrew = 'https://pokeapi.co/api/v2/pokemon/sandshrew'
resp_sandshrew = requests.get(url_sandshrew)
soup_sandshrew = BeautifulSoup(resp_sandshrew.content, 'html.parser')
soup_read_sandshrew = soup_sandshrew.get_text()

pos_poder1_sandshrew = soup_read_sandshrew.find('name')
poder1_sandshrew = soup_read_sandshrew[pos_poder1_sandshrew+7:pos_poder1_sandshrew+16].upper()
#print(poder1_sandshrew)

pos_poder2_sandshrew = soup_read_sandshrew.find('name')
poder2_sandshrew = soup_read_sandshrew[pos_poder2_sandshrew+112: pos_poder2_sandshrew+121].upper()
#print(poder2_sandshrew)



#Poderes Sandslash
url_sandslash = 'https://pokeapi.co/api/v2/pokemon/sandslash'
resp_sandslash = requests.get(url_sandslash)
soup_sandslash = BeautifulSoup(resp_sandslash.content, 'html.parser')
soup_read_sandslash = soup_sandslash.get_text()

pos_poder1_sandslash = soup_read_sandslash.find('name')
poder1_sandslash = soup_read_sandslash[pos_poder1_sandslash+7:pos_poder1_sandslash+16].upper()
#print(poder1_sandslash)

pos_poder2_sandslash = soup_read_sandslash.find('name')
poder2_sandslash = soup_read_sandslash[pos_poder2_sandslash+112: pos_poder2_sandslash+121].upper()
#print(poder2_sandslash)



#Poderes Nidorina
url_nidorina = 'https://pokeapi.co/api/v2/pokemon/nidorina'
resp_nidorina = requests.get(url_nidorina)
soup_nidorina = BeautifulSoup(resp_nidorina.content, 'html.parser')
soup_read_nidorina = soup_nidorina.get_text()

pos_poder1_nidorina = soup_read_nidorina.find('name')
poder1_nidorina = soup_read_nidorina[pos_poder1_nidorina+7:pos_poder1_nidorina+19].upper()
#print(poder1_nidorina)

pos_poder2_nidorina = soup_read_nidorina.find('name')
poder2_nidorina = soup_read_nidorina[pos_poder2_nidorina+116:pos_poder2_nidorina+123].upper()
#print(poder2_nidorina)

pos_poder3_nidorina = soup_read_nidorina.find('name')
poder3_nidorina = soup_read_nidorina[pos_poder3_nidorina+220:pos_poder3_nidorina+226].upper()
#print(poder3_nidorina)



#Condicional para verificar el estatus: (200 = Éxito) y (404 = Failled)
if resp_spearow and resp_fearow and resp_ekans and resp_arbok and resp_pika and resp_raichu and resp_sandshrew and resp_sandslash and resp_nidorina:
    print('¡Éxito! ¡Se han obtenido las habilidades de las APIS!')
else:
    print('¡Un error ha ocurrido!')



# ---------------------------------------------------- FUNCIONES ---------------------------------------------------------------

#Función que sirve para invocar a determinado Pokemon y para saber qué número es
def mensaje_nombre(nombre, numero):
    respuesta = messagebox.showinfo(message = "Este pokemon es " + nombre, title = "Pokemon " + numero)
    
    
#Funciones que sirven para describir brevemente a los pokemones    
def descripcion_poke1():
    respuesta = messagebox.showinfo(message = "Spearow es un Pokémon de tipo normal/volador introducido en la primera generación. Spearow es más pequeño que Fearow y tiene una forma más parecida a la de un halcón. Su pico es pequeño, el cual usa para atrapar a sus presas. Sus alas son de color rojizo y sus puntas tienen un tono más claro. Las patas tienen garras para poder agarrar a sus presas. Sus ojos parecen ser desafiantes. Es el peor enemigo de los Pidgey y los Rattata. No hay que subestimarlo por su diminuto tamaño, ya que tiene una actitud muy feroz.", 
                                    title = "Descripción genérica - Pokemon 1")
    
def descripcion_poke2():
    respuesta = messagebox.showinfo(message = "Fearow es un Pokémon de tipo normal/volador introducido en la primera generación. Es la evolución de Spearow. Su nombre proviene de las palabras en inglés fear (miedo) y sparrow (gorrión). También hay posibilidad de que su nombre provenga de fear (miedo) y arrow (flecha o lanza) por la forma de su pico o de row (bronca) por su fuerte carácter, como puede apreciarse en el anime.", 
                                    title = "Descripción genérica - Pokemon 2")
    
def descripcion_poke3():
    respuesta = messagebox.showinfo(message = "Ekans es un Pokémon de tipo veneno introducido en la primera generación. Al ser una serpiente, le es fácil moverse por casi todo tipo de lugares y escabullirse en cualquier momento. Es muy silenciosa y sigilosa, es difícil saber cuando está al acecho. Su longitud crece a medida que envejece. Al nacer, su mandíbula no posee veneno, por lo que su mordisco es inofensivo, sin embargo es muy doloroso. Cuando quiere descansar, se enrosca. Como las serpientes, muda la piel periódicamente.", 
                                    title = "Descripción genérica - Pokemon 3")
    
def descripcion_poke4():
    respuesta = messagebox.showinfo(message = "Arbok es un Pokémon de tipo veneno introducido en la primera generación. Es la forma evolucionada de Ekans. Arbok es un Pokémon que parece inspirada en la cobra de anteojos. Este Pokémon es venenoso y habita en pantanos, bosques, etc. Sus músculos son capaces de estrujar bidones de hierro. No obstante, esta cualidad es más común en las boas que en las cobras. Al contrario que las cobras, Arbok no puede retractar la membrana de su cuello.", 
                                    title = "Descripción genérica - Pokemon 4")
    
def descripcion_poke5():
    respuesta = messagebox.showinfo(message = "Pikachu es un Pokémon de tipo eléctrico introducido en la primera generación. Es el Pokémon más conocido de la historia, mayormente por ser el acompañante del protagonista del anime, Ash Ketchum y la mascota representante de la franquicia Pokémon. Pikachu almacena una gran cantidad de electricidad en sus mejillas. Estas parecen cargarse eléctricamente durante la noche mientras duerme. Las mejillas de Pikachu también pueden ser recargadas mediante una descarga eléctrica, como se ha podido observar en algunos episodios del anime. A veces suelta unas pequeñas descargas cuando se acaba de despertar.", 
                                    title = "Descripción genérica - Pokemon 5")
    
def descripcion_poke6():
    respuesta = messagebox.showinfo(message = "Raichu es un Pokémon de tipo eléctrico introducido en la primera generación. Es una de las dos posibles evoluciones de Pikachu y la forma habitual del Raichu de Alola. Este Pokémon es un gran roedor bípedo. Tiene un pelaje anaranjado, una cola oscura y gruesa como un cable de tendido eléctrico que termina en forma de rayo y totalmente plana, que además puede soportar grandes cargas. Tiene un vientre de tono claro y unas mejillas amarillas, que son sus polos eléctricos, estos producen la energía eléctrica que se conduce a la cola de Raichu para ser liberada en forma de potentes ataques tipo eléctrico.", 
                                    title = "Descripción genérica - Pokemon 6")
    
def descripcion_poke7():
    respuesta = messagebox.showinfo(message = "Sandshrew es un Pokémon de tipo tierra introducido en la primera generación. Es la forma habitual del Sandshrew de Alola. Pese a su nombre, la apariencia de Sandshrew es más semejante a la de un armadillo o un pangolín que a la de una musaraña. Es una criatura pequeña, amarilla y de apariencia similar a un roedor, cubierto de escamas duras y con garras afiladas. Sus ojos son grandes y negros.", 
                                    title = "Descripción genérica - Pokemon 7")
    
def descripcion_poke8():
    respuesta = messagebox.showinfo(message = "Sandslash es un Pokémon de tipo tierra introducido en la primera generación. Es la evolución de Sandshrew y la forma habitual del Sandslash de Alola. Sandslash habita en las mismas zonas áridas que su preevolución Sandshrew, en profundas y numerosas madrigueras interconectadas. Se alimenta de lo que logra cazar en el desierto y el rocío que se forma en sus escamas durante la noche es su principal fuente de agua.", 
                                    title = "Descripción genérica - Pokemon 8")
    
def descripcion_poke9():
    respuesta = messagebox.showinfo(message = "Nidorina es un Pokémon de tipo veneno introducido en la primera generación. Es la forma evolucionada de Nidoran♀ y la contraparte femenina de Nidorino. Es un Pokémon que básicamente reside en los campos de hierba alta. Es muy similar a Nidorino a pesar de que no tenga cuerno. Puede enfadarse tanto o más que este ya que sabe defenderse bien con sus púas venenosas. Tiene un oído tan fino dado el considerable tamaño de sus orejas. Sus púas se contraen al dormir y cuando está relajada; estas crecen más lentamente que las de un Nidorino. Por esta razón prefiere atacar con mordiscos y arañazos.", 
                                    title = "Descripción genérica - Pokemon 9")
    
#Función para imprimir los poderes de los pokemones
def poderes2_pokemon(poder1, poder2, nombre):
    respuesta = messagebox.showinfo(message = "Los poderes de este pokemon son " + poder1 + " y " + poder2,
                                  title = "Poderes del Pokemon " + nombre)
    
def poderes3_pokemon(poder1, poder2, poder3, nombre):
    respuesta = messagebox.showinfo(message = "Los poderes de este pokemon son " + poder1 + ", " + poder2 + " y " + poder3,
                                  title = "Poderes del Pokemon " + nombre)
    
    

# ------------------------------------------------ BOTONES DE POKEMONES --------------------------------------------------------    

#POKEMON 1 - Spearow
boton1_1 = tkinter.Button(ventana, text = "Pokemon 1", command = lambda: mensaje_nombre("Spearow", "1"), font = "Roboto", bg="brown")
boton1_1.place(relx=0.03, rely=0.02, relwidth=0.23, relheight=0.08)

boton1_2 = tkinter.Button(ventana, text = "Descripcion 1", command = descripcion_poke1, font = "Roboto", bg="green")
boton1_2.place(relx=0.38, rely=0.02, relwidth=0.23, relheight=0.08)

boton1_3 = tkinter.Button(ventana, text = "Habilidades 1", command = lambda: poderes2_pokemon(poder1_spearow, poder2_spearow, "Spearow"), font = "Roboto", bg="orange")
boton1_3.place(relx=0.73, rely=0.02, relwidth=0.23, relheight=0.08)


#POKEMON 2 - Fearow
boton2_1 = tkinter.Button(ventana, text = "Pokemon 2", command = lambda: mensaje_nombre("Fearow", "2"), font = "Roboto", bg="brown")
boton2_1.place(relx=0.03, rely=0.13, relwidth=0.23, relheight=0.08)

boton2_2 = tkinter.Button(ventana, text = "Descripcion 2", command = descripcion_poke2, font = "Roboto", bg="green")
boton2_2.place(relx=0.38, rely=0.13, relwidth=0.23, relheight=0.08)

boton2_3 = tkinter.Button(ventana, text = "Habilidades 2", command = lambda: poderes2_pokemon(poder1_fearow, poder2_fearow, "Fearow"), font = "Roboto", bg="orange")
boton2_3.place(relx=0.73, rely=0.13, relwidth=0.23, relheight=0.08)


#POKEMON 3 - Ekans
boton3_1 = tkinter.Button(ventana, text = "Pokemon 3", command = lambda: mensaje_nombre("Ekans", "3"), font = "Roboto", bg="brown")
boton3_1.place(relx=0.03, rely=0.24, relwidth=0.23, relheight=0.08)

boton3_2 = tkinter.Button(ventana, text = "Descripcion 3", command = descripcion_poke3, font = "Roboto", bg="green")
boton3_2.place(relx=0.38, rely=0.24, relwidth=0.23, relheight=0.08)

boton3_3 = tkinter.Button(ventana, text = "Habilidades 3", command = lambda: poderes3_pokemon(poder1_ekans, poder2_ekans, poder3_ekans, "Ekans"), font = "Roboto", bg="orange")
boton3_3.place(relx=0.73, rely=0.24, relwidth=0.23, relheight=0.08)


#POKEMON 4 - Arbok
boton4_1 = tkinter.Button(ventana, text = "Pokemon 4", command = lambda: mensaje_nombre("Arbok", "4"), font = "Roboto", bg="brown")
boton4_1.place(relx=0.03, rely=0.35, relwidth=0.23, relheight=0.08)

boton4_2 = tkinter.Button(ventana, text = "Descripcion 4", command = descripcion_poke4, font = "Roboto", bg="green")
boton4_2.place(relx=0.38, rely=0.35, relwidth=0.23, relheight=0.08)

boton4_3 = tkinter.Button(ventana, text = "Habilidades 4", command = lambda: poderes3_pokemon(poder1_arbok, poder2_arbok, poder3_arbok, "Arbok"), font = "Roboto", bg="orange")
boton4_3.place(relx=0.73, rely=0.35, relwidth=0.23, relheight=0.08)


#POKEMON 5 - Pikachu
boton5_1 = tkinter.Button(ventana, text = "Pokemon 5", command = lambda: mensaje_nombre("Pikachu", "5"), font = "Roboto", bg="brown")
boton5_1.place(relx=0.03, rely=0.46, relwidth=0.23, relheight=0.08)

boton5_2 = tkinter.Button(ventana, text = "Descripcion 5", command = descripcion_poke5, font = "Roboto", bg="green")
boton5_2.place(relx=0.38, rely=0.46, relwidth=0.23, relheight=0.08)

boton5_3 = tkinter.Button(ventana, text = "Habilidades 5", command = lambda: poderes2_pokemon(poder1_pikachu, poder2_pikachu, "Pikachu"), font = "Roboto", bg="orange")
boton5_3.place(relx=0.73, rely=0.46, relwidth=0.23, relheight=0.08)


#POKEMON 6 - Raichu
boton6_1 = tkinter.Button(ventana, text = "Pokemon 6", command = lambda: mensaje_nombre("Raichu", "6"), font = "Roboto", bg="brown")
boton6_1.place(relx=0.03, rely=0.57, relwidth=0.23, relheight=0.08)

boton6_2 = tkinter.Button(ventana, text = "Descripcion 6", command = descripcion_poke6, font = "Roboto", bg="green")
boton6_2.place(relx=0.38, rely=0.57, relwidth=0.23, relheight=0.08)

boton6_3 = tkinter.Button(ventana, text = "Habilidades 6", command = lambda: poderes2_pokemon(poder1_raichu, poder2_raichu, "Raichu"), font = "Roboto", bg="orange")
boton6_3.place(relx=0.73, rely=0.57, relwidth=0.23, relheight=0.08)


#POKEMON 7 - Sandshrew
boton7_1 = tkinter.Button(ventana, text = "Pokemon 7", command = lambda: mensaje_nombre("Sandshrew", "7"), font = "Roboto", bg="brown")
boton7_1.place(relx=0.03, rely=0.68, relwidth=0.23, relheight=0.08)

boton7_2 = tkinter.Button(ventana, text = "Descripcion 7", command = descripcion_poke7, font = "Roboto", bg="green")
boton7_2.place(relx=0.38, rely=0.68, relwidth=0.23, relheight=0.08)

boton7_3 = tkinter.Button(ventana, text = "Habilidades 7", command = lambda: poderes2_pokemon(poder1_sandshrew, poder2_sandshrew, "Sandshrew"), font = "Roboto", bg="orange")
boton7_3.place(relx=0.73, rely=0.68, relwidth=0.23, relheight=0.08)


#POKEMON 8 - Sandslash
boton8_1 = tkinter.Button(ventana, text = "Pokemon 8", command = lambda: mensaje_nombre("Sandslash", "8"), font = "Roboto", bg="brown")
boton8_1.place(relx=0.03, rely=0.79, relwidth=0.23, relheight=0.08)

boton8_2 = tkinter.Button(ventana, text = "Descripcion 8", command = descripcion_poke8, font = "Roboto", bg="green")
boton8_2.place(relx=0.38, rely=0.79, relwidth=0.23, relheight=0.08)

boton8_3 = tkinter.Button(ventana, text = "Habilidades 8", command = lambda: poderes2_pokemon(poder1_sandslash, poder2_sandslash, "Sandslash"), font = "Roboto", bg="orange")
boton8_3.place(relx=0.73, rely=0.79, relwidth=0.23, relheight=0.08)


#POKEMON 9 - Nidorina
boton9_1 = tkinter.Button(ventana, text = "Pokemon 9", command = lambda: mensaje_nombre("Nidorina", "9"), font = "Roboto", bg="brown")
boton9_1.place(relx=0.03, rely=0.90, relwidth=0.23, relheight=0.08)

boton9_2 = tkinter.Button(ventana, text = "Descripcion 9", command = descripcion_poke9, font = "Roboto", bg="green")
boton9_2.place(relx=0.38, rely=0.90, relwidth=0.23, relheight=0.08)

boton9_3 = tkinter.Button(ventana, text = "Habilidades 9", command = lambda: poderes3_pokemon(poder1_nidorina, poder2_nidorina, poder3_nidorina, "Nidorina"), font = "Roboto", bg="orange")
boton9_3.place(relx=0.73, rely=0.90, relwidth=0.23, relheight=0.08)



ventana.mainloop()


# In[ ]:




