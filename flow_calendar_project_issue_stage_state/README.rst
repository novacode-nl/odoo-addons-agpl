.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
   :target: https://www.gnu.org/licenses/agpl
   :alt: License: AGPL-3

=========================================
Flow Calendar Project Issue - Stage State
=========================================

Issue planning/calendar features by Stage State.

This module extends **Flow Calendar Project Issue** (https://apps.odoo.com/apps/modules/10.0/flow_calendar_project_issue/): Nova Code

Features
========

#. Automatically put an Issue in the configured **Planned stage** (stage.state==planned), once its **first Calendar Event** is planned.
#. Exclude/(filter) Issues marked *"Done"* or *"Cancelled"*, from the **Project-Issue field** in the **Calendar Event (form).**
