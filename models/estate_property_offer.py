from odoo import fields, models

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estate Property Offer'

    # Basic
    price = fields.Float("Price", required=True, digits=(10, 2))

    # Relation
    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    property_id = fields.Many2one("estate.property", string="Property", required=True)