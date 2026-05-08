# Simulación API

## Objetivo

Simular el envío de información desde Odoo haci otro sistema ERP/CRM o aplicación externa

---

# Datos que se enviaran

Los datos enviados serían:

- nombre de la tarea
- cliente asociado
- fecha
- estado

---

# Ejemplo JSON

```json
{
    "nombre": "Llamad de seguimiento",
    "cliente_id": 7,
    "cliente_nombre": "Agrolait",
    "fecha": "2026-05-12",
    "estado": "pendiente"
}
```
---

# Flujo básico de integración

1. El usuario crea tareas en Odoo.
2. Odoo almacena la información en PostgreSQL.
3. El ORM consulta los registros.
4. Los datos se convierten en JSON.
5. El sistema externo recibe la información.

--- 

# Utilidad empresarial

Esta integración permitiría:

- sincronizar tareas
- generar informes
- compartir información con CRM externos
- automatizar procesos empresariales