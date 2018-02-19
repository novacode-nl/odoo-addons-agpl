# -*- coding: utf-8 -*-
# Copyright 2018 Nova Code (http://www.novacode.nl)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

{
    'name': 'Flow Calendar Project Issue - Filter Issues by Stage State',
    'summary': 'Filter Issues in the Calendar Event (form).',
    'description': 'Filter/exclude Issues, marked done or cancelled, from the Project-Issue field in the Calendar Event (form).',
    'version': '0.1',
    'author': 'Nova Code',
    'website': 'https://www.novacode.nl',
    'license': 'AGPL-3',
    'category': 'Extra Tools',
    'depends': [
        # https://apps.odoo.com/apps/modules/10.0/flow_calendar_project_issue/
        'flow_calendar_project_issue',
        # https://github.com/OCA/project/tree/10.0/project_stage_state
        'project_stage_state'
    ],
    'data': [],
    'images': [
        'static/description/flow_calendar_project_issue_banner.jpg',
    ]
}
