# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, api, fields, models

class Partner(models.Model):
    _inherit = 'res.partner'

    rating = fields.Float(string='Rating')
