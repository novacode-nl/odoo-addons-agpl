# -*- coding: utf-8 -*-
# Copyright 2018 Nova Code (http://www.novacode.nl)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import api, fields, models, _


class Meeting(models.Model):
    _inherit = "calendar.event"

    flowcal_issue_id = fields.Many2one(
        'project.issue',
        domain="[('project_id', '=', flowcal_issue_project_id), ('stage_id.state', 'not in', ['done', 'cancelled'])]")
    flowcal_issue_stage_state = fields.Selection(related='flowcal_issue_id.stage_id.state', string='Issue Stage State')

    @api.model
    def create(self, vals):
        if vals.get('flowcal_issue_id'):
            issue = self.env['project.issue'].browse(vals.get('flowcal_issue_id'))
            if not issue.flowcal_event_ids:
                planned_type = issue.project_id.type_ids.filtered(lambda r: r.state == 'planned')
                issue.stage_id = planned_type.id

        return super(Meeting, self).create(vals)
