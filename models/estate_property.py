from odoo import models, fields
from odoo.exceptions import ValidationError


class EstateProperty(models.Model):
    # Private
    _name = 'estate.property'
    _description = 'Estate Property'
    _sql_constraints = [
        ("check_name", "UNIQUE(name)", "This name already exists!"),
        ("check_expected_price", "CHECK(expected_price > 0)", "This Price > 0"),
    ]

    # Basic
    name = fields.Char("Title", required=True)
    description = fields.Text("Description")
    postcode = fields.Char("Postcode")
    date_available = fields.Date("Date Available")
    facades = fields.Integer("Facades")
    garage = fields.Boolean("Garage")
    expected_price = fields.Float("Expected Price", required=True)
    bedrooms = fields.Integer("Bedrooms", default=2)
    living_area = fields.Integer("Living Area (sqm)")
    garden = fields.Boolean("Garden")
    garden_area = fields.Integer("Garden Area (sqm)")
    garden_orientation = fields.Selection(
        selection=[
            ("N", "North"),
            ("S", "South"),
            ("E", "East"),
            ("W", "West"),
        ]
    )

    # Special
    state = fields.Selection(
        selection=[
            ("new", "New"),
            ("offer_received", "Offer Received"),
            ("offer_accepted", "Offer Accepted"),
            ("sold", "Sold"),
            ("canceled", "Canceled"),
        ],
        string="Status",
        required=True,
        copy=False,
        default="new",
    )

    # Relation
    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offers")
    property_type_id = fields.Many2one("estate.property.type", "Property Type")
    tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    user_id = fields.Many2one("res.users", string="Salesman", default=lambda self: self.env.user)
    buyer_id = fields.Many2one("res.partner", string="Buyer", copy=False)

    # Action
    def action_mark_as_sold(self):
        for rec in self:
            if rec.state in ['sold', 'canceled']:
                raise ValidationError("Cannot mark as sold. Already sold or canceled.")
            rec.state = 'sold'
