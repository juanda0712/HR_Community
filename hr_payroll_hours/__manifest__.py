{
    'name': 'JRM HR',
    'version': '17.0',
    'author': 'JRM Tech Solutions',
    'maintainer': 'JRM Tech Solutions',
    'license': 'AGPL-3',
    'category': 'Extra Tools',
    'summary': 'Short summary.',
    'depends': ['base','hr_payroll_community'],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_payroll_hours_views.xml',
        'views/hr_payslip_views.xml',
        'views/hr_payslip_run_views.xml',
        'data/hr_payroll_data.xml'
    ],
}
