from odoo import fields, models, api


class HrPayslipRun(models.Model):
    """Create new model for getting Payslip Batches"""
    _inherit = 'hr.payslip.run'
    _description = 'Payslip Batches'

    struct_id = fields.Many2one(comodel_name='hr.payroll.structure',
                                string='Structure',
                                help='Sets rules for all payslips')

    @api.onchange('struct_id')
    def _onchange_struct_id(self):
        for payslip in self.slip_ids:
            payslip.struct_id = self.struct_id

    def action_compute_all_sheet(self):
        self.slip_ids.action_compute_sheet()
        return True




