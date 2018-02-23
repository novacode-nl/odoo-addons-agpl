# -*- coding: utf-8 -*-
# Copyright 2017 Nova Code (http://www.novacode.nl)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import models, fields, api


class Issue(models.Model):
    _inherit = "project.issue"

    stage_id = fields.Many2one('project.task.type', compute='_compute_stage_id_by_flowcal_event_ids', store=True)

    @api.depends('flowcal_event_ids')
    def _compute_stage_id_by_flowcal_event_ids(self):
        for issue in self:
            if issue.flowcal_event_ids:
                planned_task_type = issue.project_id.type_ids.filtered(lambda r: r.state == 'planned')
                issue.stage_id = planned_task_type.id
