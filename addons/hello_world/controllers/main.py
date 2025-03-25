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
    _payment_progess = '/payment/vnpay/payment-return/'
    
    @http.route(_payment_progess)
    def vnpay_payment_return(seft):
        
        url = request.httprequest.url
        
        parsed_url = urlparse(url)
        
        trading_code = parse_qs(parsed_url.query)['vnp_TxnRef'][0]
        
        params = {'vnp_TxnRef': trading_code,
                  'vnp_Amount': int(parse_qs(parsed_url.query)['vnp_Amount'][0]),
                  'vnp_OrderInfo': parse_qs(parsed_url.query)['vnp_OderInfo'][0],
                  'vnp_TransactionNo': parse_qs(parsed_url.query)['vnp_TransactionNo'][0],
                  'vnp_ResponseCode': parse_qs(parsed_url.query)['vnp_ResponseCode'][0],
                  'vnp_TmnCode': parse_qs(parsed_url.query)['vnp_TmnCode'][0],
                  'vnp_PayDate': parse_qs(parsed_url.query)['vnp_PayDate'][0],
                  'vnp_BankCode': parse_qs(parsed_url.query)['vnp_BankCode'][0],
                  'vnp_CardType': parse_qs(parsed_url.query)['vnp_CardType'][0],
                  'vnp_BankTranNo': parse_qs(parsed_url.query)['vnp_BankTranNo'][0],
                  'vnp_TransactionStatus': parse_qs(parsed_url.query)['vnp_TransactionStatus'][0],
                  'vnp_SecureHash': parse_qs(parsed_url.query)['vnp_SecureHash'][0]}
        try:
            keyPayment = request.env['payment.provider'].sudo().search(
                [('code', '=', 'vnpay')])
            status = ''
            if vnpay_service.validate_respone(keyPayment['vnpay_hash_secret_key'], params):
                if params['vnp_ResponseCode'] == "00":
                    status = 'paid'
                elif params['vnp_ResponseCode'] == "02":
                    status = 'pending'
                elif params['vnp_ResponseCode'] == "04":
                    status = 'expired'
                elif params['vnp_ResponseCode'] == "03":
                    status = 'failed'
            else:
                status = 'canceled'
            exits_order = request.env['payment.stack_payment'].isExistOder(
                trading_code, '')
            request.env['payment.transaction'].sudo()._handle_notification_data('vnpay', {'reference': exits_order, 'status': status})
            return redirect(seft._payment_status)
        except:
            _logger.error("Lỗi thanh toán")
            exits_order = request.env['payment.stack_payment'].isExistsOrder(trading_code, '')
            status = ''
            request.env['payment.transaction'].sudo()._handle_notification_data('vnpay',{'reference': exits_order, 'status': status})
            
            return redirect(seft._payment_status)    
                    
                    