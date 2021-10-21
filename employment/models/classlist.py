# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class classlist(models.Model):
    _name = 'classlist.educate'
    _description = 'Class Educate'

    name = fields.Text('Tên Khóa Học')
    startday = fields.Date('Ngày Bắt Đầu')
    endday = fields.Date('Ngày Kết Thúc')
    mentor = fields.Text('Người phụ trách')
    content = fields.Text('Nội dung')
    capacity = fields.Integer('Sĩ số')
    nbofweek = fields.Integer('Số Buổi Trong Tuần')
    time = fields.Selection([('8h10h','8h-10h'),('10h12h','10h-112h'),('13h15h','13h-15h'), ('15h17h','15h-17h')], "Thời Gian Biểu")
    note = fields.Text('Ghi chú')


    # _sql_constraints = [
    #     ('unique_room', 'unique(room)', u'Phòng đã tồn tại, hãy thử lại!'),
    #     ('unique_name', 'unique(name)', u'Tên môn học đã tồn tại, hãy thử lại!'),
    # ]

    # @api.constrains("room")
    # def _room_validate(self):
    #     for subjects in self:
    #         if len(subjects.room) < 4:
    #             raise exceptions.ValidationError(u"Tên phòng quá ngắn!")
    #
    # @api.constrains("amount")
    # def _amount_validate(self):
    #     for subjects in self:
    #         if subjects.amount < 0:
    #             raise exceptions.ValidationError(u"Số lượng không thể ít hơn được nữa!")
    #
    # @api.onchange("amount")
    # def _amount_onchange(self):
    #     if self.amount == 0:
    #         self.state = 'nghi'
    #     elif self.amount == 3:
    #         self.state = 'hocchinhthuc'
    #     else:
    #         self.state = 'hocbu'
