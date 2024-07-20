from odoo import api, fields, models


class PatientAppointmentWizard(models.TransientModel):
    _name = 'patient.appointment.wizard'
    _description = 'Patient Appointment Wizard'

    name = fields.Char(string='Appointment Name')
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    doctor_id = fields.Many2one('res.partner', string='Doctor')
    appointment_date = fields.Date(string='Date', default=lambda self: self.fields.Date.Today)
    available_hour = fields.Datetime(string='Available Hour', readonly=True)
    symptoms = fields.Text(string='Reason')  # ရောဂါလက္ခာဏာများ

    @api.onchange('doctor_id')  # must be doctor_id
    @api.depends('doctor_id')
    def onchange_doctor_id(self):
        if self.doctor_id:
            if self.doctor_id.available_hour:
                self.available_hour = self.doctor_id.available_hour
        else:
            self.symptoms.__setattr__('required', True)


class PatientAppointment(models.Model):
    _name = 'hospital.appointment'

    patient = fields.Char(string='Patient', readonly=True)
    email = fields.Char(string='Email', tracking=True)
    phone = fields.Char(string='Phone')
    birth_date = fields.Date(string='Birth Date', required=True, tracking=True)
    # doctor = fields.Many2one('res.partner', string='Doctor')
    appointment_date = fields.Date(string='Appointment Date')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
    ])

    @api.onchange('state')
    @api.depends('state')
    def onchange_state(self):
        if self.state == 'confirmed':
            self.env['hospital.patient'].create({
                'name': self.patient,
                'birth_date': self.birth_date,
                'phone': self.phone,
                'email': self.email or False,
                'appointment_date': self.appointment_date,
                'available_hour': self.available_hour,
            })