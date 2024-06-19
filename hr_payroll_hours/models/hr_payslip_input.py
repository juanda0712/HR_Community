from odoo import models, fields

class HrPayslipInput(models.Model):
    _inherit = 'hr.payslip.input'

    sequence = fields.Integer( index=True, default=10,
                               required=False,
                              help="Sequence")
    code = fields.Char(required=False,
                       help="The code that can be used in the salary rules")
    contract_id = fields.Many2one('hr.contract', string='Contract',
                                  help="The contract for which applied"
                                       " this input",
                                  required=False)