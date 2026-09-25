from odoo import models, fields, api


class Classmates(models.Model):
    _name = 'classmates'

    name = fields.Char()
    company = fields.Selection(
        [
            ("company1", "Company 1"),
            ("company2", "Company 2")
        ]
    )
    working_date = fields.Date()
    image = fields.Image()
    position = fields.Selection(
        [
            ("position1", "Position 1"),
            ("position2", "Position 2")
        ]
    )
    address = fields.Char()
    phone = fields.Char()
    email = fields.Char()
    url = fields.Char()
