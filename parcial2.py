# 2. Dada una pila con los datos de dinosaurios resolver lo siguiente actividades:
#a) Contar cuantas especies hay;
#b) Determinar cuantos descubridores distintos hay;
#c) Mostrar todos los dinosaurios que empiecen con T;
#d) Mostrar todos los dinosaurio que pesen menos de 275 Kg
#e) Dejar en una pila aparte todos los dinosaurios que comienzan con A, Q, S;

class Stack:

    def __init__(self):
        self.__elements = []

    def push(self, element):
        self.__elements.append(element)

    def pop(self):
        if len(self.__elements) > 0:
            return self.__elements.pop()
        else:
            return None

    def on_top(self):
        if len(self.__elements) > 0:
            return self.__elements[-1]
        else:
            return None

    def size(self):
        return len(self.__elements)
    
    
dinosaurios = [
    {
      "nombre": "Tyrannosaurus Rex",
      "especie": "Theropoda",
      "peso": "7000 kg",
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1902
    },
    {
      "nombre": "Triceratops",
      "especie": "Ceratopsidae",
      "peso": "6000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1889
    },
    {
      "nombre": "Velociraptor",
      "especie": "Dromaeosauridae",
      "peso": "15 kg",
      "descubridor": "Henry Fairfield Osborn",
      "ano_descubrimiento": 1924
    },
    {
      "nombre": "Brachiosaurus",
      "especie": "Sauropoda",
      "peso": "56000 kg",
      "descubridor": "Elmer S. Riggs",
      "ano_descubrimiento": 1903
    },
    {
      "nombre": "Stegosaurus",
      "especie": "Stegosauridae",
      "peso": "5000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Spinosaurus",
      "especie": "Spinosauridae",
      "peso": "10000 kg",
      "descubridor": "Ernst Stromer",
      "ano_descubrimiento": 1912
    },
    {
      "nombre": "Allosaurus",
      "especie": "Theropoda",
      "peso": "2000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Apatosaurus",
      "especie": "Sauropoda",
      "peso": "23000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Diplodocus",
      "especie": "Sauropoda",
      "peso": "15000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1878
    },
    {
      "nombre": "Ankylosaurus",
      "especie": "Ankylosauridae",
      "peso": "6000 kg",
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1908
    },
    {
      "nombre": "Parasaurolophus",
      "especie": "Hadrosauridae",
      "peso": "2500 kg",
      "descubridor": "William Parks",
      "ano_descubrimiento": 1922
    },
    {
      "nombre": "Carnotaurus",
      "especie": "Theropoda",
      "peso": "1500 kg",
      "descubridor": "José Bonaparte",
      "ano_descubrimiento": 1985
    },
    {
      "nombre": "Styracosaurus",
      "especie": "Ceratopsidae",
      "peso": "2700 kg",
      "descubridor": "Lawrence Lambe",
      "ano_descubrimiento": 1913
    },
    {
      "nombre": "Therizinosaurus",
      "especie": "Therizinosauridae",
      "peso": "5000 kg",
      "descubridor": "Evgeny Maleev",
      "ano_descubrimiento": 1954
    },
    {
      "nombre": "Pteranodon",
      "especie": "Pterosauria",
      "peso": "25 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1876
    },
    {
      "nombre": "Quetzalcoatlus",
      "especie": "Pterosauria",
      "peso": "200 kg",
      "descubridor": "Douglas A. Lawson",
      "ano_descubrimiento": 1971
    },
    {
      "nombre": "Plesiosaurus",
      "especie": "Plesiosauria",
      "peso": "450 kg",
      "descubridor": "Mary Anning",
      "ano_descubrimiento": 1824
    },
    {
      "nombre": "Mosasaurus",
      "especie": "Mosasauridae",
      "peso": "15000 kg",
      "descubridor": "William Conybeare",
      "ano_descubrimiento": 1829
    },

  ]
#pounto A
def especies(dinosaurios):
    lista_especies=[]
    for index,element in enumerate(dinosaurios):
        if dinosaurios[index]['especie'] not in lista_especies:
            lista_especies.append(dinosaurios[index]['especie'])
    cant=len(lista_especies)
    print("la cantidad de especies es de ",cant, "y son", lista_especies)
especies(dinosaurios)    

#punto B
descubridores = set()
for dinosaurio in dinosaurios:
    descubridores.add(dinosaurio['descubridor'])

numero_descubridores_distintos = len(descubridores)

print(f"Cantidad de descubridores distintos: {numero_descubridores_distintos}")

print(f"Cantidad de descubridores distintos: {numero_descubridores_distintos}")

#punto C Mostrar todos los dinosaurios que empiecen con T;

lista_T = []
for dino in dinosaurios:
    if dino["nombre"][0] == "T":
        lista_T.append(dino)
print (lista_T)

#punto D Mostrar todos los dinosaurio que pesen menos de 275 Kg

for dino in dinosaurios:
    peso_str = dino["peso"]
    peso_int = int(peso_str.split()[0]) 
    if peso_int < 275:
        print(dino["nombre"]) 
    
#punto E Dejar en una pila aparte todos los dinosaurios que comienzan con A, Q, S;

def mostrar_dinosaurios_por_letra(letra):
    print(f"Dinosaurios que empiezan con '{letra}':")
    for dino in dinosaurios:
        if dino["nombre"][0].upper() == letra.upper():
            print(dino["nombre"])
            
mostrar_dinosaurios_por_letra("A")
mostrar_dinosaurios_por_letra("Q")
mostrar_dinosaurios_por_letra("S")