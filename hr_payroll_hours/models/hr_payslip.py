from odoo import api, fields, models

class HrPayslip(models.Model):
    _inherit = 'hr.payslip'

    extended_hours_ids = fields.Many2many('hr.payroll.hours',ondelete="restrict", copy=False)
    @api.onchange('employee_id')
    def onchange_employee(self):
        unlinked_extended_hours = self.env['hr.payroll.hours'].search([
            ('employee_id', '=', self.employee_id.id),
            ('date', '>=', self.date_from),
            ('date', '<=', self.date_to)
        ])
        self.extended_hours_ids = [(6, 0, unlinked_extended_hours.ids)]
        super(HrPayslip, self).onchange_employee()
    @api.onchange('date_from')
    def onchange_date_from(self):
        unlinked_extended_hours = self.env['hr.payroll.hours'].search([
            ('employee_id', '=', self.employee_id.id),
            ('date', '>=', self.date_from),
            ('date', '<=', self.date_to)
        ])
        self.extended_hours_ids = [(6, 0, unlinked_extended_hours.ids)]
        super(HrPayslip, self).onchange_date_from()
    @api.onchange('date_to')
    def onchange_date_to(self):
        unlinked_extended_hours = self.env['hr.payroll.hours'].search([
            ('employee_id', '=', self.employee_id.id),
            ('date', '>=', self.date_from),
            ('date', '<=', self.date_to)
        ])
        self.extended_hours_ids = [(6, 0, unlinked_extended_hours.ids)]
        super(HrPayslip, self).onchange_date_to()

    @api.onchange('struct_id')
    def onchange_struct_id(self):
        """Actualizar las líneas del recibo cuando se cambia la estructura salarial."""
        if not self.struct_id:
            return
        self.struct_id = self.struct_id