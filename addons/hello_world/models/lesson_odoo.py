# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, fields, models


class CourseOdoo(models.Model):
    _name = 'lesson.odoo'
    _description = 'Bài học'

    name = fields.Char(string='Tên bài học')
    is_active = fields.Boolean(string='Bài học có mở hay không', copy=False,
                               readonly=True, default=False, help="Bài học có mở hay không?")
    parent_id = fields.Many2one(
        comodel_name='course.odoo', string='Khoá học')

    def set_is_active_lesson(self):
        for item in self:
            item.is_active = False if item.is_active else True
        return {}
