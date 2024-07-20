{
    'name': 'Hospital Doctor',
    'version': '17.0.0.1',
    'summary': '',
    'description': 'Hospital Doctor partner',
    'author': 'Htet Myat',
    'website': '',
    'license': '',
    'depends': ['base', 'mail', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'data/res_weekday.xml',
        'views/hospital_doctor_res_partner_inherit.xml',
    ],
    'installable': True,
    'auto_install': False,
}