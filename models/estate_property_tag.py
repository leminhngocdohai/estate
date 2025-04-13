from odoo import models, fields


class EstateProperty(models.Model):
    # Private
    _name = 'estate.property.tag'
    _description = 'Estate Property Tag'
    _sql_constraints = [
        ("check_name", "UNIQUE(name)", "This name already exists!")
    ]

    # Basic
    name = fields.Char("Title", required=True)
    color = fields.Integer("Color Index")