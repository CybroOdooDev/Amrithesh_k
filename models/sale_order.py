from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        res = super().action_confirm()
        all_product_types = list(set([rec.product_template_id.detailed_type for rec in self.order_line]))


    def action_view_delivery(self):
        return self._get_action_view_picking(self.env['stock.picking'].search([('origin', '=', self.name)]))
