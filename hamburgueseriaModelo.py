from odoo import models, fields, api
from odoo.exceptions import ValidationError
import datetime


class tienda(models.Model):
    _name='hamburgueseria.tienda'
    _description='Descripcion de la tienda'


    name=fields.Char(string='Nombre de la tienda')
    descripcion=fields.Text(string='Descripcion de la tienda')
    email= fields.Char(string='Email')
    telefono = fields.Char(string='Telefono')
    web = fields.Char(string='Web')
    

    @api.constrains('email')
    def _check_email(self):
        for record in self:
            if '@' not in record.email:
                raise ValidationError("El email no es correcto")

class promocion(models.Model):
    _name='hamburgueseria.promocion'
    _description='Promociones de la hamburgueseria'


    name=fields.Char(string='Nombre de la promocion')
    descripcion=fields.Text(string='Descripcion de la promocion')
    fecha_inicio=fields.Date(string='Fecha de inicio')
    fecha_fin=fields.Date(string='Fecha de fin')
    precio=fields.Float(string='Precio')
    tienda=fields.Many2one('hamburgueseria.tienda', string='Tienda')
    hamburguesa=fields.Many2one('hamburgueseria.hamburguesa', string='Hamburguesa')
    bebida=fields.Many2one('hamburguesaria.bebida', string='Bebida')
    

    @api.constrains('fecha_inicio','fecha_fin')
    def _check_fechas(self):
        for record in self:
            if record.fecha_inicio > record.fecha_fin:
                raise ValidationError("La fecha de inicio no puede ser mayor que la de fin")

    @api.constrains('precio')
    def _check_precio(self):
        for record in self:
            if record.precio < 0:
                raise ValidationError("El precio no puede ser negativo")

class hamburguesa(models.Model):
    _name='hamburgueseria.hamburguesa'
    _description='Hamburguesas de la hamburgueseria'


    name=fields.Char(string='Nombre de la hamburguesa')
    descripcion=fields.Text(string='Descripcion de la hamburguesa')
    precio=fields.Float(string='Precio')
    promocion=fields.Many2one('hamburgueseria.promocion', string='Promocion')

    @api.constrains('precio')
    def _check_precio(self):
        for record in self:
            if record.precio < 0:
                raise ValidationError("El precio no puede ser negativo")
class bebida(models.Model):
    _name='hamburgueseria.bebida'
    _description='Bebidas de la hamburgueseria'

    name=fields.Char(string='Nombre de la bebida')
    descripcion=fields.Text(string='Descripcion de la bebida')
    precio=fields.Float(string='Precio')
    promocion=fields.Many2one('hamburgueseria.promocion', string='Promocion')

    @api.constrains('precio')
    def _check_precio(self):
        for record in self:
            if record.precio < 0:
                raise ValidationError("El precio no puede ser negativo")