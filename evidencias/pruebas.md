# Pruebas realizadas

## Prueba 1: Creación de registros

Se crearon varias tareas correctamente desde el formulario

### Resultado 

Correcto.

---
## Prueba 2: cambio de estado

Se pulsó el botón:

```text
Marcar como finalizada
```

### Resultado

Correcto. El estado cambió correctamente.

```text
Pendente - > Finalizada
```

---
## Prueba 3: Se aplicó filtro

```text
Tareas pendientes
```

### Resultado

Sólo se mostrasron tareas pendiente

---
## Prueba 3: Agrupación por cliente

Se gruparon registros por clientes

### Resultado

La tareas aparecieron agrupadas correctamente

---

## Prueba 4: Exportación CSV

Se exportó el listado de tareas desde la vista lista.

### Resultado

Se generó correctamente el archivo.

```text
exportación.csv
```

--- 

# Verificación general
| Elemento  | Estado  |
|---|---|
| Modelo  | Correcto  |
| Vistas  | Correcto  |
| Botón  | Correcto  |
| ORM  | Correcto  |
| Filtro  | Correcto  |
| Exportación  | Correcto  |
| JSON API  | Correcto  |

---

# Conclusión

El módulo funciona correctamente y cumple los requisitos solicitados an la práctica.