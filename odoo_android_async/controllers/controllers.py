# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import Response
import json


class OdooAndroidAsync(http.Controller):
    @http.route('/api/attendance/hours/<user_id>/<day_week>', auth='user', methods=['GET'])
    def get_attendance_hours(self, user_id, day_week, **kw):
        try:
            calendar_id = http.request.env['hr.employee'].sudo().search(
                [('user_id', '=', int(user_id))]).resource_calendar_id.id

            hours = http.request.env['resource.calendar.attendance'].sudo().search_read(
                [('calendar_id', '=', int(calendar_id)),
                 ('dayofweek', '=', day_week)],
                ['hour_from', 'hour_to']
            )

            return self.build_response(hours)

        except Exception as e:
            return self.build_response({'error': str(e)})

    @http.route('/api/employee/<user_id>', auth='user', methods=['GET'])
    def get_employee(self, user_id, **kw):
        try:
            employee_id = http.request.env['hr.employee'].sudo().search(
                [('user_id', '=', int(user_id))]).id

            return self.build_response(
                {
                    "employee_id":employee_id
                })
        except Exception as e:
            return self.build_response({'error': str(e)})

    @http.route('/api/attendance', auth="user", type="json", methods=['POST'], csrf=False)
    def insert_attendance(self, **kw):
        try:
            attendance = json.loads(str(http.request.httprequest.data, 'utf-8'))
            http.request.env['hr.attendance'].sudo().create(attendance)
            return self.build_response({'message': 'inserted'})
        except Exception as e:
            return self.build_response({'err': str(e)})

    def build_response(self, entity):
        response = json.dumps(entity, ensure_ascii=False).encode('utf8')
        return Response(response, content_type='application/json;charset=utf-8', status=200)
