from odoo import models, fields, api


class Classmates(models.Model):
    _name = 'classmates'

    name = fields.Char(required= True)
    company = fields.Selection(
        [
            ("rondy", "الشركة الدولية لصناعة السيراميك روندي"),
            ("elkholy_swimming_pool", "الخولي للتشطيبات وحمامات السباحة")
        ],
        required= True,
        default='rondy'
    )
    working_start_date = fields.Date(default=fields.Date.today())
    working_end_date = fields.Date(default=fields.Date.today())
    image = fields.Image()
    position = fields.Selection(
        [
            ("position1", "رئيس وردية"),
            ("position2", "رئيس قسم"),
            ("position3", "زميل عمل"),
            ("position4", "مساعد رئيس قسم"),
            ("position5", "مقاول"),
            ("position6", "رئيس المكتب الفني")
        ]
    )
    address = fields.Char()
    phone = fields.Char(size=11)
    email = fields.Char()
    url = fields.Char()
