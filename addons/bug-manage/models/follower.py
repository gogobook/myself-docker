# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Follower(models.Model):
    _inherit='res.partner'
    bug_ids=fields.Many2many('bm.bug',string='bug')