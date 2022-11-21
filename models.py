from odoo import fields, models

class Alumno(models.Model):
    _name = "alumno.alumno"
    _description = "Modelo Alumno"

    name = fields.Char('Nombre', help = "Nombre del alumno", required=True)
    escuela_id = fields.Many2one("escuela.escuela", string = "Alumno", help = "Escuela del alumno")

class Computadora(models.Model):
    _name = "computadora.computadora"
    _description = "Modelo Computadora"

    modelo = fields.Char(string = 'Modelo de computadora', required=True, help = "Modelo de la computadora")

class Material(models.Model):
    _name = "material.material"
    _description = "Modelo Material"

    name = fields.Char(string = 'Nombre', help = "Nombre del material", required=True)

class Aula(models.Model):
    _name = "aula.aula"
    _descrption = "Modelo Aula"

    computadora_id = fields.Many2one('computadora.computadora', string = 'Computadora', help = "Computadora del aula")
    materiales_ids = fields.Many2many('material.material', string = 'Materiales', help = "Materiales del aula")
    alumnos_ids = fields.Many2many('alumno.alumno', string = 'Alumnos', help = "Alumnos del aula")
    escuela_id = fields.Many2one("escuela.escuela", string = "Aula", help = "Escuela del aula")

class Escuela(models.Model):
    _name = "escuela.escuela"
    _description = "Modelo Escuela"

    name = fields.Char(string = 'Nombre', help = "Nombre de la escuela")
    aulas_ids = fields.One2many('aula.aula', 'escuela_id', string = 'Aulas', help = "Aulas de la escuela")
    alumnos_ids = fields.One2many('alumno.alumno', 'escuela_id', string = 'Alumnos', help = "Alumnos de la escuela")
