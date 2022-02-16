# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class odoo_pos_system(models.Model):
#     _name = 'odoo_pos_system.odoo_pos_system'
#     _description = 'odoo_pos_system.odoo_pos_system'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
