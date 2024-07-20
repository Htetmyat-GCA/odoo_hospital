from odoo import api, fields, models
from datetime import datetime


class Patient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Patient'
    _order = 'id desc'

    name = fields.Char(string='Name', required=True, tracking=True)
    reference = fields.Char(string='Reference', readonly=True)
    age = fields.Integer(string='Age', store=True, readonly=True, default=1)
    birth_date = fields.Date(string='Birth Date', required=True, tracking=True)
    email = fields.Char(string='Email', tracking=True)
    phone = fields.Char(string='Phone')
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female')], required=True, string='Gender', tracking=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('appointed', 'Appointed'),
    ])
    document = fields.Many2one('patient.medical.record', string='Document')

    @api.onchange('birth_date')
    def onchange_birth_date(self):
        td = datetime.today()
        if self.birth_date:
            self.age = td.year - self.birth_date.year - ((td.month, td.day) < (self.birth_date.month, self.birth_date.day))

    @api.model
    def create(self, vals):
        if vals.get('gender') == 'male':
            prefix = 'M'
        else:
            prefix = 'F'
        sequence_code = self.env['ir.sequence'].next_by_code('hospital_management.patient_code') or '/'
        vals['reference'] = f'{prefix}[{sequence_code}]'
        return super().create(vals)


class MedicalRecord(models.Model):
    _name = 'patient.medical.record'
    _description = 'Patient Medical Record Book'

    patient_id = fields.Many2one('hospital.patient', string='Patient', domain=[('is_patient', '=', True)])
    doctor_id = fields.Many2many('res.partner', string='Doctor', domain=[('is_doctor', '=', True)])
    appointment_date = fields.Datetime(string='Appointment Date', default=fields.Datetime.now)
    description = fields.Char(string='Description')
    # status = fields.Selection(
    #     [('appointing', 'Appointing'), ('reappoint', 'Reappointing'), ('inactive', 'Inactive')],
    #     string='Status',
    # )
    refer = fields.Char(string='Refer To')


class PatientCase(models.Model):
    _name = 'patient.case'
    _description = 'Patient Case'

    name = fields.Char(string='Name')
    parent_id = fields.Many2one('patient.case', string='Parent')
    child_ids = fields.One2many('patient.case', 'parent_id', string='Child')
    # doctor_ids = fields.One2many('res.partner', 'doctor_id', string='Doctor')
