from odoo import api, fields, models
from datetime import date, datetime, timedelta


class Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'

    name = fields.Char(string='Name')
    reference = fields.Char(string='Reference')
    age = fields.Integer(string='Age', store=True, readonly=True, default=1)
    birth_date = fields.Date(string='Birth Date')
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female')],
    )
    is_patient = fields.Boolean(string='Is Patient', readonly=True, default=True)
    document = fields.Many2one('patient.recordbook', string='Document')

    @api.onchange('birth_date')
    def onchange_birth_date(self):
        td = datetime.today()
        if self.birth_date:
            self.age = td.year - self.birth_date.year - ((td.month, td.day) < (self.birth_date.month, self.birth_date.day))


class RecordBook(models.Model):
    _name = 'patient.recordbook'
    _description = 'Patient RecordBook'

    patient_id = fields.Many2one('hospital.patient', string='Patient', domain=[('is_patient', '=', True)])
    # doctor_id = fields.Many2one('res.partner', string='Doctor', domain=[('is_doctor', '=', True)])
    appointment_date = fields.Datetime(string='Appointment Date', default=fields.Datetime.now)
    record_line_ids = fields.One2many('recordbook.record', 'record_id', string='Records')
    description = fields.Char(string='Description')
    status = fields.Selection(
        [('appointing', 'Appointing'), ('reappoint', 'Reappointing'), ('inactive', 'Inactive')],
        string='Status',
    )
    handover = fields.Char(string='Redirect')


class Records(models.Model):
    _name = 'recordbook.record'
    _description = 'Patient Records'

    book = fields.Many2one('patient.recordbook', string='Records')


class PatientCase(models.Model):
    _name = 'patient.case'
    _description = 'Patient Case'

    name = fields.Char(string='Name')
    parent_id = fields.Many2one('patient.case', string='Parent')
    child_ids = fields.One2many('patient.case', 'parent_id', string='Child')
    # doctor_ids = fields.One2many('res.partner', 'doctor_id', string='Doctor')
