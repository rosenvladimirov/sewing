# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools, _

import logging

_logger = logging.getLogger(__name__)


class ProductPropertiesStatic(models.Model):
    _inherit = "product.properties.static"

    fabric_standard_width = fields.Float('Standard fabric width')
    fabric_width = fields.Float('Fabric width')


class ProductPropertiesLineCategory(models.Model):
    _inherit = "product.properties.print.line.category"

    use_fabric_width = fields.Boolean()

    @api.depends('type_id', 'print_id')
    def _compute_display_name(self):
        for type in self:
            if type.type_id:
                type.display_name = "[%s] %s" % (type.type_id.sequence, type.type_id.name)
            elif type.static_field:
                type.display_name = "%s" % type.static_field
            else:
                use_fabric_width = "%s" % type.use_fabric_width and "x" or "-"

                type.display_name = "Patient usage |%s|" % (
                    use_fabric_width,
                )
