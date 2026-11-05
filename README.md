# Taller de Pandas

**Nombre:** Juan Alberto Zuluaga Ramirez

## Preguntas de negocio y respuestas

### 1. ¿Qué categoría genera más ingresos?

**Tecnologia**, con $14.290.000.

| Categoría | Ingresos |
|---|---:|
| Tecnologia | 14.290.000 |
| Hogar | 3.653.000 |
| Papeleria | 749.000 |
| Accesorios | 484.000 |

**Datos de consola**

Ingresos por categoría:
categoria
Tecnologia    14290000
Hogar          3653000
Papeleria       749000
Accesorios      484000
Name: total, dtype: int64
La categoría que más ingresa es: Tecnologia 

**Criterio usado**

Se agruparon las ventas por categoría, se sumaron los totales de cada una y se ordenaron de mayor a menor.

### 2. ¿Qué canal vende más?

**Online**, tanto en número de ventas como en ingresos.

| Canal | Ventas | Ingresos |
|---|---:|---:|
| Online | 35 | 14.669.000 |
| Tienda | 33 | 4.507.000 |

**Datos de consola**

Ventas e ingresos por canal:
        ventas  ingresos
canal
Online      35  14669000
Tienda      33   4507000

**Criterio usado**

Se agruparon las ventas por canal y se calcularon dos columnas: el número de ventas y la suma de los ingresos de cada canal.

### 3. ¿Los clientes VIP compran más que los Regulares?

**Sí**, en promedio por cliente. Como hay más clientes Regular que VIP, se comparan promedios y no totales.

| Segmento | Clientes | Compras | Gasto total | Compras promedio | Gasto promedio |
|---|---:|---:|---:|---:|---:|
| Regular | 36 | 39 | 11.110.000 | 1,08 | 308.611 |
| VIP | 24 | 29 | 8.066.000 | 1,21 | 336.083 |

**Datos de consola**

Resumen por segmento de cliente:
                  num_clientes  compras  gasto_total  compras_promedio  gasto_promedio
segmento_cliente                                                                      
Regular                     36       39     11110000          1.083333   308611.111111
VIP                         24       29      8066000          1.208333   336083.333333

**Criterio usado**

Se agruparon los clientes VIP y Regular con sus respectivas compras. Luego se dividieron las compras y el gasto total de cada segmento entre su número de clientes para obtener los promedios.

### 4. ¿Qué método de pago es el más usado?

**Efectivo**, con 30 ventas.

| Método de pago | Ventas |
|---|---:|
| Efectivo | 30 |
| Tarjeta | 25 |
| Transferencia | 13 |

**Datos de consola**

Conteo por método de pago:
metodo_pago
Efectivo         30
Tarjeta          25
Transferencia    13
Name: count, dtype: int64
El método de pago más usado es: Efectivo

**Criterio usado**

Se contó cuántas veces aparece cada método de pago y se tomó el que tiene más ventas.

### 5. ¿Cuáles son los cinco clientes con más compras?

Varios clientes tienen 2 compras, así que se ordenó por número de compras y, como desempate, por gasto total.

| # | Cliente | Compras | Total |
|---:|---|---:|---:|
| 1 | Nicolas Cardona | 2 | 2.515.000 |
| 2 | Matias Rodriguez | 2 | 1.278.000 |
| 3 | Mia Quintero | 2 | 1.090.000 |
| 4 | Luna Montoya | 2 | 1.007.000 |
| 5 | Luis Perez | 2 | 730.000 |

**Datos de consola**

Top 5 clientes con más compras:
                             compras    total
id_cliente nombre_cliente                    
21         Nicolas Cardona         2  2515000
35         Matias Rodriguez        2  1278000
52         Mia Quintero            2  1090000
58         Luna Montoya            2  1007000
3          Luis Perez              2   730000

**Criterio usado**

Se agruparon las ventas por cliente, se contaron sus compras y se sumó su gasto. Se ordenaron por compras (y por gasto como desempate) y se tomaron los cinco primeros.

