{
    'name': 'Hospital Management',
    'version': '17.0.0.1',
    'summary': '',
    'description': 'Hospital management module',
    'category': 'Manufacturing',
    'author': 'Htet Myat',
    'website': '',
    'license': '',
    'depends': ['base', 'web_enterprise'],
    'data': [
        'security/ir.model.access.csv',
        'views/hospital_patient.xml',
    ],
    'assets': {
            'web._assets_primary_variables': [
                ('after', 'web/static/src/scss/primary_variables.scss', 'web_enterprise/static/src/**/*.variables.scss'),
                ('before',
                 'web_enterprise/static/src/scss/primary_variables.scss',
                 'hospital_management/static/src/scss/customize_backend_theme_color.scss'),
            ]
        },
    'installable': True,
    'auto_install': False,
}