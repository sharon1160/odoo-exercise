# odoo-exercise

Escuela
- 5 aulas
- 20 alumnos
- 20 computadoras
- 100 materiales

**Modelos:** aula, alumno, computadora, material, escuela

- **Campos Escuela:** name:Char, aulas:One2many, alumnos:One2many
- **Campos Alumnos:** name:Char
- **Campos Aula:** computadoras:many2one, materiales:many2many, alumnos:many2many
