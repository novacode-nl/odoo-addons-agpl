# -*- coding: utf-8 -*-
# Copyright 2018 Nova Code (http://www.novacode.nl)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import api, fields, models, _


class Meeting(models.Model):
    _inherit = "calendar.event"

    flowcal_task_id = fields.Many2one(
        'project.task',
        domain="[('project_id', '=', flowcal_task_project_id), ('stage_id.state', 'not in', ['done', 'cancelled'])]")
    flowcal_task_stage_state = fields.Selection(related='flowcal_task_id.stage_id.state', string='Task Stage State')
