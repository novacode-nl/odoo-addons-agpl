# -*- coding: utf-8 -*-
# Copyright 2018 Nova Code (http://www.novacode.nl)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

{
    'name': 'Flow Calendar Project Task - Filter Tasks by Stage State',
    'summary': 'Filter Tasks in the Calendar Event (form).',
    'description': 'Filter/exclude Tasks, marked done or cancelled, from the Project-Task field in the Calendar Event (form).',
    'version': '0.1',
    'author': 'Nova Code',
    'website': 'https://www.novacode.nl',
    'license': 'AGPL-3',
    'category': 'Extra Tools',
    'depends': [
        # https://apps.odoo.com/apps/modules/10.0/flow_calendar_project_task/
        'flow_calendar_project_task',
        # https://github.com/OCA/project/tree/10.0/project_stage_state
        'project_stage_state'
    ],
    'data': [],
    'images': [
        'static/description/flow_calendar_project_task_banner.jpg',
    ]
}