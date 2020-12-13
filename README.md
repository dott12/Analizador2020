# Analizador2020

---

Esta hecho en Python3, utilizando la libreria tkinter para el manejo de la interfaz grafica. 
Consta de dos archivos principales (por el momento), `word.py` y `main.py`.


+ `word.py` es donde esta definida la clase utilizada al momento de crear un objeto que represente
una palabra dentro del codigo.

+ `main.py` tiene las funciones prinicipales, y es donde se instancia el objeto de la interfaz de usuario,
con la cual interactuaria un usuario.
  
El listado de palabras reservadas e identificadores esta en el archivo `Tipos.csv`, para un facil manejo
y parseo.


---

# Reglas de Produccion:





| LEXEMA   | TOKEN |
|----------|-------|
| +        |    PLUS   |
| -        |   MINUS    |
| *        |    TIMES   |
| /        |    DIVIDE   |
| =       |    EQUALS   |
| INICIO   |    INICIO   |
| FIN      |    FIN   |
| (      |    LPAREN   |
| )      |    RPAREN   |
| [+-]? ['0'-'9']       |    NUMBER   |
| ['A'-'Z'] ['a'-'z'].*   |    ID   |
| ESCRIBIR |  ESCRIBIR     |
| LEER     |   LEER    |

\
\
\
```

<PROGRAMA> -> INICIO <STAT> FIN

<STAT> -> <EXP> |  <ID> EQUALS <NUMBER> | <ID> EQUALS <ID>

<EXP> -> ESCRIBIR <EXP> | LEER <EXP> | LPAREN <OP> RPAREN | <NUMBER> | <ID>

<OP> -> <NUMBER> PLUS <NUMBER> | <NUMBER> MINUS <NUMBER> | <NUMBER> TIMES <NUMBER> | <NUMBER> DIVIDE <NUMBER> 

<NUMBER> -> [+-]? ['0'-'9']+

<ID> -> ['A'-'Z'] ['a'-'z'].*

```

\
\
Estas son las reglas de produccion correspondientes a este analizador sintactico. Aun son WIP.