# -*- coding: utf-8 -*-
# Copyright 2017 Nova Code (http://www.novacode.nl)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import fields, models


class ProjectType(models.Model):
    _inherit = "project.type"

    orbeon_builder_form_ids = fields.Many2many(
        "orbeon.builder",
        string="Orbeon Builder Forms",
    )
