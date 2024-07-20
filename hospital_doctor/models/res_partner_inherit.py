from odoo import api, fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    is_doctor = fields.Boolean(string='Is Doctor')
    specialist = fields.Many2one('hospital.specialist.category', string='Specialist')
    available_hours = fields.Integer(string='Available Hours')
    present_days = fields.Many2many('res.weekday')
    patient_count = fields.Integer(string='Patient Count')


class Weekday(models.Model):
    _name = 'res.weekday'
    _description = 'Weekday'

    index = fields.Integer(string='Index')
    name = fields.Char(string='Name')
    color = fields.Char(string='Color')


class SpecialistCategory(models.Model):
    _name = 'hospital.specialist.category'
    _description = 'Medical Specialities'

    name = fields.Char(string='Name')
    parent_id = fields.Many2one('hospital.specialist.category', 'Parent')
    child_ids = fields.One2many('hospital.specialist.category', 'parent_id', 'Child')