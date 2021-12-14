# Copyright 2021 Rosen Vladimirov, BioPrint Ltd.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Product Properties Sewing',
    'summary': """
        Add specific static properties for sewing industry""",
    'version': '11.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Rosen Vladimirov, BioPrint Ltd.,Odoo Community Association (OCA)',
    'website': 'https://github.com/rosenvladimirov/sewing',
    'depends': [
        'product',
        'product_properties',
        'stock',
    ],
    'data': [
        'views/stock_production_lot_views.xml',
    ],
    'demo': [
    ],
}
