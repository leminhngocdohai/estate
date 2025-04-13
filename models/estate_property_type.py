from odoo import models, fields


class EstateProperty(models.Model):
    # Private
    _name = 'estate.property.type'
    _description = 'Estate Property Types'
    _sql_constraints = [
        ("check_name", "UNIQUE(name)", "This name already exists!")
    ]

    # Basic
    name = fields.Char("Title", required=True)

    # Relation
    property_ids = fields.One2many("estate.property", "property_type_id", string="Offers")