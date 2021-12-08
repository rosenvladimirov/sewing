# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class ProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    product_prop_static_id = fields.Many2one("product.properties.static", 'Static Product properties')
    count_static_properties = fields.Integer("Count static properties", compute="_compute_count_static_properties")
    fabric_standard_width = fields.Float('Standard fabric width', related="product_prop_static_id.fabric_standard_width")
    fabric_width = fields.Float('Fabric width', related="product_prop_static_id.fabric_width", store=True)

    @api.multi
    def _compute_count_static_properties(self):
        for record in self:
            record.count_static_properties = len(self.env['product.properties.static'].search(
                [('object_id', '=', 'product.template,%s' % record.id)]).ids)

    @api.model
    def create(self, vals):
        if 'product_prop_static_id' not in vals:
            vals = self.env['product.properties.static'].static_property_data(self, vals)

        res = super(ProductionLot, self).create(vals)

        if res.product_prop_static_id:
            res.product_prop_static_id.write({'object_id': "%s,%d" % ("%s" % res._name, res.id)})
        return res

    @api.multi
    def write(self, vals):
        for res in self:
            static_ids = self.env['product.properties.static'].static_property_fields()
            if 'product_prop_static_id' not in vals \
                    and not res.product_prop_static_id \
                    and any([x in vals for x in static_ids]):
                vals = self.env['product.properties.static'].static_property_data(res, vals)
        return super(ProductionLot, self).write(vals)
