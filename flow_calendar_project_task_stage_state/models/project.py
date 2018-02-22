# -*- coding: utf-8 -*-
# Copyright 2017 Nova Code (http://www.novacode.nl)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import models, fields, api


class ProjectTaskType(models.Model):
    _inherit = 'project.task.type'

    state = fields.Selection(selection_add=[("planned", "Planned")])


class Task(models.Model):
    _inherit = "project.task"

    stage_id = fields.Many2one('project.task.type', compute='_compute_stage_id_by_flowcal_event_ids', store=True)

    @api.depends('flowcal_event_ids')
    def _compute_stage_id_by_flowcal_event_ids(self):
        for task in self:
            if task.flowcal_event_ids:
                planned_task_type = task.project_id.type_ids.filtered(lambda r: r.state == 'planned')
                task.stage_id = planned_task_type.id
