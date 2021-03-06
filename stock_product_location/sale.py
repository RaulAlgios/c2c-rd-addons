# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#    Copyright (C) 2010-2012 ChriCar Beteiligungs- und Beratungs- GmbH (<http://www.camptocamp.at>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp.osv import orm
import logging

class sale_order(orm.Model):
    _inherit= "sale.order"
    _logger = logging.getLogger(__name__)

    def _prepare_order_line_move(self, cr, uid, order, line, picking_id,
                                    date_planned, context=None):
        res = super(sale_order,self)._prepare_order_line_move(cr, uid, order, line, picking_id, date_planned, context)
        location_id = line.product_id.property_stock_location.id or line.product_id.categ_id.property_stock_location.id or order.shop_id.warehouse_id.lot_stock_id.id
        self._logger.debug('_prepare_order_line_move `%s`', res)
        self._logger.debug('_prepare_order_line_move `%s`', location_id)
        res.update({'location_id':location_id})
        return res
