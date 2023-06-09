{
    "name": "Mail Demo",
    "summary": """
        Setup mail connection to local Mailhog container.
    """,
    "author": "Mint System GmbH, Odoo Community Association (OCA)",
    "website": "https://www.mint-system.ch",
    "category": "Technicaly",
    "version": "15.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["mail"],
    "data": ["data/base_setup_data.xml", "data/ir.mail_server.csv"],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
}
