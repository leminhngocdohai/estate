from odoo import models, fields, api

class EstateProperty(models.Model):
    _inherit = 'estate.property'

    product_id = fields.Many2one('product.template', string="Related Product", readonly=True)

    def sync_product_template(self):
        # Access the 'product.template' model
        Product = self.env['product.template']

        for property in self:
            if property.product_id:
                # Update the product if it already exists
                property.product_id.write({
                    'name': property.name,
                    'list_price': property.expected_price,
                })
            else:
                # Create a new product if it doesn't exist
                product = Product.create({
                    'name': property.name,
                    'type': 'service',
                    'list_price': property.expected_price,
                })
                property.product_id = product.id

    # Override create method with @api.model_create_multi
    @api.model_create_multi
    def create(self, vals_list):
        # Create multiple estate property records
        properties = super().create(vals_list)

        # Sync product template for each created property
        for property in properties:
            property.sync_product_template()

        return properties

    # Override write method
    def write(self, vals):
        res = super().write(vals)

        # Sync product template after updating the estate property
        self.sync_product_template()

        return res

    # Override unlink method
    def unlink(self):
        # Get all related products and delete them
        products_to_delete = self.mapped('product_id').filtered(lambda p: p)
        res = super().unlink()

        if products_to_delete:
            products_to_delete.unlink()

        return res
