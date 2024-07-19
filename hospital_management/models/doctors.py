from odoo import fields, models


class Doctors(models.Model):
    _inherit = 'res.partner'
    
    speciality = fields.Selection(
        [
            ('general', 'General'),
            ('dentist', 'Dentist'),
            ('sergeant', 'Sergeant'),
            ('child_special', 'Child Specialize'),
            ('liver_special', 'Liver Specialize'),
            ('stomach_special', 'Stomach Specialize'),
        ],
        'Speciality',
    )
    hourly_rate = fields.Integer('Hourly Rate')
    is_doctor = fields.Boolean(string='Doctor', default=True)
