# FUNCIONES
## Concepto
matematicamente una funcion es una operacion que toma uno o mas valores llamados `argumentos`y produce un valor denominado`resultado`.
f(x)=x/1+x**2
>[NOTE]
> todos los lenguajes de programacion tiene funciones incorporadas (`funciones internas`), y funciones creadas por el usuario (`funciones externas`)
> en programacion una funcios es un subprograma, podemos decir tambien que es una estructura que nos permita agrupar codigo y sus principales objetivos son:
-`NO REPETIR` fragmentos de codigo
-`REUTILIZAR` el codigo en distintos escenarios
## Estructura de una  funcion
Una funcion viene`definida`por un `nombre`, sus `parametros` y su valor de `entorno`. una vez creada la funcion podemos solicitar su ejecucion
`invocando` la funcion por su`nombre`.
## Definir una funcion
para definir una funcion en python utilizaremis la palabra` def` seguida por el nombre de la funcion a continuacion espesificaremos los `parametros` con `()` si es una funcion sin parametros , si se tuviera mas de un parametro iran reparados por `,`, finalizaremos la linea con `:`, en la siguiente linea sin olvidar el identado, comensara  el `cuerpo` de la funcion (micro programa) que puede contener 1 o mas sentencias, finalmente devera`retornar` un resultado con ta palabra`retrun`.
> [!TIP]
>  como retorno tambien se puede utilizar la `funcion interna`,`print()`, para depuracion de codigo no es recomendable usarlo en produccion.
> `print` es una funcion,herramienta que nos permite comprobar si una funcion
**ejemplo:**
```python
 def saluso():
    saludo="hola chivo"
    saludo_dos="como estas"
    return f"{saludo},{saludo_dos}"
    # print(f"{saludo},{ saluso_dos}")
    print(saludo())
    #saludo()
```
## Invocar una funcion
para invocar , (o llamar , ejecutar) una funcion solo tendremos  que escribir el `nombre` de la funcion seguido por`()` parentecis.
```python
def saludo()
print("hola")
#invocando la funcion
saludo()
```
## Retorna un valor
las funciones pueden retornar( o devolver) un valor.
```python
def uno():
    return 1
    uno()
```
>[!WARNING]
> No confundir`return`. el valor retorno por `return` nos pe♠rmite usarlo fuera de su contexto. y `print()` solo mostrara el literal por terminal.
**ejemplo**
*en el ejemplo`lecture.py`
## Retornando multiples valores
el secreto es hacerlo mediante un tipo de dato estructurado
```python
def varios()
return 2,3,4
verios()
#retorna (2,3,4)
def lista():
    return["hola",45]
    #retorna["hola",45]
    def dicc():
        return{"nombre":"jose","edad":45}
         dicc()
#retorna{"nombre":"jose","edad":45}
```
## Parametros y argumentos
 si una funcion nos dispuciera de valores de entrada estaria limitada en su actuacion.
 es por ello que los `parametros` nos permiten variar los datos que consume una funcion para optener distintos resultados
 **ejemplo**
*crear una funcion para recivir un valor numerico y disminuye su raiz cuadrada*

  ```python
  def sqrt(valor):
    return valor**(1/2)
# NOTA: en este caso, el valor 4 es un argumento  de la funcion
    sqrt(4)
 ```
cuando llamamos a una funcion con`argumentos`, los valores de estos argumentos  se copian en los correspondientemente`parametros` dentro fe la funcion.
```python
def ejem(a,b,c):
    return a+b+c
    ejem(4,5,6)
```
### Argumentos nominales
En esta aproximacion los argumentos no son copiados en un orden especifico si no que **asignan por nombre a cada parametro**. Ello nos permiten evitar el proiblema de conocer cual es el orden de los parametros de la definicion de la funcion.Para utilizarlo, basta con realizar una asignacion de cada argumentos en la propia llanmada ala funcion.
**ejemplo**
```python
def builld_cpu(familia,num_core,frecuencia):
    print(f"""
    la cpu es la familia{familia},con{num_core} cores y con una
     frecuencia de{frecuencia}
  """  )
  # haciendos uso de argumentos nominales
  builld_cpu(num_core=4,familia="intel",frecuencia=2.7)
  builld_cpu("intel",4,2,7)
```
### Argumentos posicionales
los argumentos no son copiados en un orden especifico , en easte caso devemos conocer o recordar cual es el orden de los parametros
**ejemplo**
```python
def builld_cpu(familia,num_core,frecuencia):
    print(f"""
    la cpu es la familia{familia},con{num_core} cores y con una
     frecuencia de{frecuencia}
  """  )
  # haciendos uso de argumentos nominales
  builld_cpu(num_core=4,familia="intel",frecuencia=2.7)
  builld_cpu("intel",4,2,7)
  ```
### Parametros por defecto
Es posible especificar **valores por defecto** en los parametros de una funcion , en el caso de que nose proporcione un valor argumenti en la llamada  ala funcion el parametro correspondiente tomaran el valor definido por defecto.
**ejemplo**
```python
def alumnos(nom,app,estado=aprobado):
    alumno("ruth","castillo")
    alumno("anthony","crucez","desaprovado")
```
## Desempaquetado/Empaquetado de argumentos(tarea)

python nos ofrece la posibilidad de empaquetar y desempaquetar argumentos cuando estamos invocando a una función, tanto para argumentos posicionales como para argumentos nominales.Y de esto se deriva el hecho de que podamos utilizar un número variable de argumentos en una función, algo que puede ser muy interesante según el caso de uso que tengamos.
**ejemplo**
```python
def _sum(*values):
    print(f'{values=}')
    result = 0
    for value in values:  # values es una tupla
        result += value
    return result
sum(4, 3, 2, 1)
values=(4, 3, 2, 1)
10

```
## Funcion internas de python(tarea)
son aquellas que están integradas en el lenguaje y están disponibles para su uso sin necesidad de importar ningún módulo adicional. Estas funciones están diseñadas para realizar tareas comunes y están optimizadas para un rendimiento óptimo.
**ejemplo**
- print(): Utilizada para imprimir texto o variables en la consola.
- len(): Devuelve la longitud (número de elementos) de un objeto iterable como una cadena, lista, tupla, diccionario, etc.
- input(): Lee una entrada del usuario desde la consola.
- type(): Devuelve el tipo de un objeto.
- range(): Genera una secuencia de números.
- int(), float(), str(), list(), tuple(), dict(), etc.: Utilizadas para convertir objetos a tipos específicos.
- sum(): Devuelve la suma de los elementos de un iterable.
- max(), min(): Devuelven el valor máximo y mínimo de un iterable, respectivamente.
- abs(): Devuelve el valor absoluto de un número.
- round(): Redondea un número al entero más cercano.
- sorted(): Ordena los elementos de un iterable.
- enumerate(): Devuelve un iterable de pares índice-valor.
- zip(): Combina iterables en una sola secuencia de tuplas.
 
 ## tipos de funciones
 ### funciones  anonimas(funciones lambda)
 una funcion que no tiene nombre
 ```python
 lambada:"hola"
 # normal
 def saludo():
    retur
 ```
 ### funciones closure
 una funcion que dentro tiene otra  funcion
 ### Funciones callback
 ### Programacion funcional
 la programacion funcional no requiere que sepas como se desarrollo y ejecuta el procemiento
 **ejemplo**
 ```python
 lista=[5,7,8,4,1]
 def num_minimo(l):
    minimo=[0]
    for n in l:
        if n < minimo:
            minimo=n
            return minimo
 #programacion funcional
 min(lista)
 ```
 #### Averiguar sobre map(),filter(),reduce()
 Map, reduce y filter son todos métodos de arreglo en JavaScript. Cada uno iterará sobre un arreglo y realizará una transformación o cálculo. Cada uno devolverá un nuevo arreglo basado en el resultado de la función. En este artículo, aprenderás por qué y cómo usar cada uno de ellos.
## MAP
El método map() se utiliza para crear un nuevo arreglo a partir de una existente, aplicando una función a cada uno de los elementos de la primera arreglo.
**ejemplo**
```python
const numeros = [1, 2, 3, 4];
const duplicar = numeros.map(elemento => elemento * 2);
console.log(duplicar); // [2, 4, 6, 8]
```

