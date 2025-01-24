from odoo import models, fields, api

class HrPayrollHoursBatch(models.Model):
    _name = 'hr.payroll.hours.batch'
    _description = 'Batch for Extra and Double Payroll Hours'

    description = fields.Char(string='Description', required=True)
    date = fields.Date(string='Date', required=True, default=fields.Date.today)
    hours = fields.Float(string='Hours', required=True, default=1)
    type = fields.Selection([
        ('extras', 'Extras'),
        ('double', 'Double'),
        ('holiday', 'Holiday'),
        ('holiday_extra', 'Extra (In holiday)')
    ], string='Type', required=True)
    employee_ids = fields.Many2many(
        comodel_name='hr.employee',
        string='Employees',
        required=True,
        help="Select employees for batch extra hours."
    )
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done')
    ], string='State', default='draft', required=True)
    payroll_hours_ids = fields.One2many('hr.payroll.hours', 'batch_id', string='Generated Payroll Hours')

    def action_generate_individual_hours(self):
        for record in self:
            for employee in record.employee_ids:
                self.env['hr.payroll.hours'].create({
                    'description': record.description,
                    'date': record.date,
                    'hours': record.hours,
                    'type': record.type,
                    'employee_id': employee.id,
                    'batch_id': record.id,
                })
            record.state = 'done'

    def unlink(self):
        for batch in self:
            if batch.payroll_hours_ids:
                batch.payroll_hours_ids.unlink()
        return super(HrPayrollHoursBatch, self).unlink()

    def set_to_draft(self):
        for batch in self:
            batch.state = 'draft'
