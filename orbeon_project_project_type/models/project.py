# -*- coding: utf-8 -*-
# Copyright 2017 Nova Code (http://www.novacode.nl)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import api, fields, models, _
import logging

_logger = logging.getLogger(__name__)


class Project(models.Model):
    _inherit = "project.project"

    @api.model
    def create(self, vals):
        res = super(Project, self).create(vals)
        runner = self.env["orbeon.runner"]

        for builder in res.type_id.orbeon_builder_form_ids:
            runner.create({
                'builder_id': builder.id,
                'project_id': res.id
            })

        return res
