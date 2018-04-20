# -*- coding: utf-8 -*-
# Copyright 2017 Nova Code (http://www.novacode.nl)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

{
    "name": "Orbeon Forms on Projects by Project Type",
    'summary': 'Orbeon Forms on Projects by Project Type',
    "version": "0.1",
    'author': 'Nova Code',
    'website': 'https://www.novacode.nl',
    'license': "AGPL-3",
    "category": "Project",
    "depends": [
        "project",
        # https://github.com/open2bizz/odoo-addons/project_type
        "project_type",
        "orbeon",
        "orbeon_project",
    ],
    "data": [
        "views/project_type.xml",
    ],
    "application": False,
    "installable": True,
}
