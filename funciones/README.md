# FUNCIONES
## concepto
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
> No confundir`return`. el valor retorno por `return` nos permite usarlo fuera de su contexto. y `print()` solo mostrara el literal por terminal.
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
            #return{"nombre":"jose","edad":45}
         
```
