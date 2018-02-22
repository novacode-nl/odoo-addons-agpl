# -*- coding: utf-8 -*-
# Copyright 2018 Nova Code (http://www.novacode.nl)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ProjectTaskType(models.Model):
    _inherit = 'project.task.type'
    state = fields.Selection(selection_add=[("planned", "Planned")])

    @api.constrains('state')
    def _check_type_ids_state_planned(self):
        # Check only 1 "planned" stage exists, across all Project its stages.
        if self.search_count([('state', '=', 'planned')]) > 1:
            raise ValidationError(_("Only 1 stage can be referenced as Planned state."))
