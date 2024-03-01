from odoo import models, fields

class HrPayrollHours(models.Model):
    _name = 'hr.payroll.hours'
    _description = 'Add Extra and Double Payroll Hours'

    description = fields.Char(string='Description', required=True)
    date = fields.Date(string='Date', required=True, default=fields.Date.today)
    hours = fields.Float(string='Hours', required=True, default=1)
    type = fields.Selection([('extras', 'Extras'), ('double', 'Double')], string='Type', required=True)
    employee_id = fields.Many2one(comodel_name='hr.employee', string='Employee',
                                  required=True,
                                  help="Choose Employee for Extended Hours")
    payslip_ids = fields.Many2many('hr.payslip', copy=False)
