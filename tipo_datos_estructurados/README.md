# tipo de datos estructurados(TDA - tipos de datos abstractos)
```python
#lista - sus   valores o elementos se pueden actualizar,eliminar
lista=["abel",20, False ,["texto",.2]]
#tupla - sus valores o elementos no pueden ser modificados o eliminados
tupla=("abel",20,5.2,5,False,[])
#diccionario o objetos
#los diccionarios almacenan los datos con clave:valor
diccionario={"nombre":"antonio","edad":15,"sexo":False}
```
[TIP]
**observacion:** que los tipos de datos estructurados pueden almacenar en su interior otros tipos

lista_alumnos=[]
"nombre":"abel"
"edad":20
"amigos":["no tiene"]

##Metodos
### 1. convertir texto a lista
```python
#Metodo list
texto="hola"
list(texto)
#["h","o","l","a"]
#metodo split
texto="hola como estan, alumnitos lindo"
texto.split(",")
##metodo join
```

### 2. agregar alementos a una lista
```python
#metodo append - es el elemento que me oermite agregar elementos al final de la lista
lista=["hola"]
lista.append("mundo")
print(lista)
#["hola","mundo"]

#metodo insert -es el metodo que me permite agregar elementos en cualquier ubicacion de la lista

lista_nombre=["edit","ruth","luz"]
lista_nombre.insert(0,"antony")
```

### eliminar elementos de una lista

```python
# metodo pop - es el metodo que elimina el ultimo elemento de la lista  es lo cntrario de append.

lista_nombre=["edit","ruth","luz"]
lista_nombre.pop()

#primera manera .-metodo remove - este metodo elimina  el por el nombre el elemento que coincida dentro de mi lista
lista_nombre=["edit","ruth","luz"]
lista_nombre.pop(0)
```

### buscar un elemento en una lista¨
```python
lista_nombre=["edit","ruth","luz"]
indice=lista_nombre.index("ruth")
print(lista_nombre[indice])

pertenecia="edit"in lista_nombre #true False

### 5.COMPARACION DE LISTAS
##podemos aser uso de los operadores de compracion para  comparar listas
**Ejemplo:**
```
```Python
compara=[1,2,3]>[1,2,3]
# 1 no por que son iguales en ambas listas
#2 no por que son iguales en ambas listas
# 3 evalua que es menor a 4
#entonces la primera lista es menor que la segunda lista
print(compara)
```
### FE DE ERRATAS(Actualizar listas)
```python
lista=[1,3,4,5,6]
lista[0]=2
print(copia_lista)
#[2,3,4,5,6]
#modificando lista con diccionario
alumnos=[
    {
        "nombre":"abel" ,
        "edad":15
    },
    {
        "nombre":"anthony",
        "edad":29
    
    }
]
alumnos[0]["edad"]=30
alumnos[0]={"nombre":"mafer","edad":15 }
alumnos[1]["sexo"]="por definir"
print(alumnos)
```
### 8. lists y diccionarios por comprencion
  es una tecnica pythonica nos pernite crear listas y diccionarios en una sola linea combinando bucles y deciciones.
  >[!NOTE]
> **vlc** value loop condiciones - valor bucle condicion
```python
#lista
texto="1,4,8,9,6"
nueva_lista=[]
for n in texto.split(","):
    nueva_lista.append(int(n))
print(nueva_lista)
#aplicando la tecnica valor bucle y condicion
texto="1,4,8,9,6"
nueva_lista=[int(n)for n in texto.split(",")if (n)%2==0]
print(nueva_lista)
```


