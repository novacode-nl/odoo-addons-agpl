.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
   :target: https://www.gnu.org/licenses/agpl
   :alt: License: AGPL-3

========================================
Flow Calendar Project Task - Stage State
========================================

Task planning/calendar features by Stage State.

This module extends **Flow Calendar Project Task** (https://apps.odoo.com/apps/modules/10.0/flow_calendar_project_task).

Features
========

#. Automatically put a Task in the configured **Planned stage** (stage.state==planned), once its **first Calendar Event** is planned.
#. Exclude/(filter) Tasks marked *"Done"* or *"Cancelled"*, from the **Project-Task field** in the **Calendar Event (form).**
