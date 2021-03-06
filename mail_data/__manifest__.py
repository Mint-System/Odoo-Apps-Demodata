{
    'name': "Mail Data",

    'summary': """
        Configure Odoo Development mail server.
    """,

    'author': 'Mint System GmbH, Odoo Community Association (OCA)',
    'website': 'https://www.mint-system.ch',
    'category': 'Technical',
    'version': '14.0.1.0.0',
    'license': 'AGPL-3',

    'depends': ['base'],

    'data': [
        'data/fetchmail.server.csv',
        'data/ir.mail_server.csv'
    ],

    'installable': True,
    'application': False,
}
