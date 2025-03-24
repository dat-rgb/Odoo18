# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
import json
from urllib.parse import urlparse, parse_qs

from werkzeug.utils import redirect
from odoo import _, http

_logger = logging.getLogger(__name__)


class MainController(http.Controller):

    @http.route('/courses', type='http', auth="user", website=True)
    def get_courses(self):
        records = http.request.env['course.odoo'].search([])
        return http.request.render(
            "hello_world.course_list_template",
            {"courses": records},
        )

    @http.route('/courses/demo')
    def get_courses_demo(self):
        try:
            url = http.request.httprequest.url
            parsed_url = urlparse(url)
            params = {'hihi': parse_qs(parsed_url.query).get('vnp_TxnRef', [''])[0]}

            # Gọi method từ model
            http.request.env['payment.stack_payment'].isExistsOrder('')

            # Get tất cả dữ liệu
            records = http.request.env['course.odoo'].search([])

            # Get dữ liệu có điều kiện
            filtered_records = http.request.env['course.odoo'].search([('id', '=', 1)])

            return redirect('/courses')
        except Exception as e:
            _logger.error("Lỗi trong get_courses_demo: %s", e)
            return redirect('/courses')
