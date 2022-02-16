# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import Response
import json


class OdooPosSystem(http.Controller):
    @http.route('/api/products/<product_id>', auth='public', methods=['GET'])
    def get_attendance_hours(self, product_id, **kw):
        try:
            products = http.request.env['product.template'].sudo().search([])

            for product in products:
                if product['id'] == int(product_id):
                    name = product['name']
                    description = product['description']
                    list_price = product['list_price']
                    image = str(product['image_1920'])

                    return self.build_response(
                        {'name: ': name,
                         'description: ': description,
                         'list_price': list_price,
                         'image': image
                         }
                    )

            return self.build_response('product not found')

        except Exception as e:
            return self.build_response({'error': str(e)})

    @http.route('/api/products/', auth='public', methods=['GET'])
    def get_attendance_hours(self, **kw):
        try:
            products = http.request.env['product.template'].sudo().search([('name', '!=', 'Discount'),
                                                                           ('name', '!=', 'Tips')])
            product_list = []

            for product in products:

                name = product['name']
                description = product['description']
                list_price = product['list_price']
                image = str(product['image_1920'])

                product_list.append({'name: ': name,
                                     'description: ': description,
                                     'list_price': list_price,
                                     'image': image
                                     })

            return self.build_response(
                product_list
            )

        except Exception as e:
            return self.build_response({'error': str(e)})

    @http.route('/api/odoo_pos_system/', auth="public")
    def index(self, **kw):
        return "hello world"

    def build_response(self, entity):
        response = json.dumps(entity, ensure_ascii=False).encode('utf8')
        return Response(response, content_type='application/json;charset=utf-8', status=200)
