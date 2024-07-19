from odoo import api, fields, models


class PatientAppointmentWizard(models.TransientModel):
    _name = 'patient.appointment.wizard'
    _description = 'Patient Appointment Wizard'

    name = fields.Char(string='Appointment Name')
    patient_id = fields.Many2one('res.partner', string='Patient', required=True)
    doctor_id = fields.Many2one('res.partner', string='Doctor')
    date = fields.Date(string='Date', default=fields.Date.default)
    reason = fields.Many2one('patient.case', string='Reason')

    @api.onchange('patient_id', 'reason')
    def _onchange_reason(self):
        if self.reason:
            self.doctor_id = self.reason.doctor_ids

    def create_appointment(self):
        self.ensure_one()
        self.env['patient.recordbook'].create({

        })

