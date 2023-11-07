from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime, time, timedelta
from pytz import timezone
from io import StringIO
import csv
import base64


class Achievement(models.Model):
    _name = 'create_achievement.achievement'
    _description = 'Achievement Model of Create-Achievement Module'

    be_appraise_by = fields.One2many(
        'create_achievement.appraise', 'achievement_id', string="Phân nhiệm vụ cho các thẩm định viên")
    criteria_ids = fields.One2many(
        'create_achievement.group_criterias', 'parent_id', string="Tập tiêu chí danh hiệu")

    name = fields.Char(default="", required=True, string="Danh hiệu")
    description = fields.Text(string="Mô tả")
    start_at = fields.Datetime(string="Ngày bắt đầu nộp", required=True)
    end_submit_at = fields.Datetime(
        string="Ngày kết thúc nộp", required=True)
    end_at = fields.Datetime(
        string="Ngày kết thúc duyệt", required=True)
    delete_at = fields.Datetime()
    last_updated = fields.Datetime(
        default=fields.Datetime.now())
    status = fields.Char(
        string="Tình Trạng", compute='_compute_status', store=True)

    name_title = fields.Char(default="Danh hiệu mới", compute="_change_title")
    computed_numbers = fields.Integer(
        'Function for sort', compute='_compute_numbers', store=True)
    appraise_status = fields.Selection([
        ('pending', 'Chưa thẩm định'),
        ('active', 'Mở thẩm định'),
        ('end', 'Kết thúc thẩm định'),
    ], default='pending', string="Trạng thái")

    exported_data  = fields.Binary(string='Danh sách hồ sơ')
    csv_name = fields.Char(string="Tên file csv")

    @api.depends('criteria_ids')
    def _compute_numbers(self):
        for record in self:
            number = 1  # Initialize the number to start from 1
            for group_criteria in record.criteria_ids:
                group_criteria.display_name = str(
                    number) + '. ' + group_criteria.name
                number += 1

    @api.depends('name')
    def _change_title(self):
        for record in self:
            record.name_title = "Danh hiệu - " + record.name

    @api.depends('last_updated', 'status')
    def _compute_status(self):
        for record in self:
            if record.end_at and record.start_at:
                if (record.last_updated < record.start_at):
                    record.status = "Trạng thái chờ"
                if (record.last_updated >= record.start_at and record.last_updated <= record.end_submit_at):
                    record.status = "Đang tiến hành"
                if (record.last_updated > record.end_submit_at and record.last_updated <= record.end_at):
                    record.status = "Đang tiến hành duyệt"
                if (record.last_updated > record.end_at):
                    record.status = "Đã kết thúc"

    @api.constrains('start_at')
    def _check_start_time(self):
        for record in self:
            tz = timezone('Asia/Bangkok')
            future_date = record.create_date + timedelta(days=0)
            default_time = time(hour=0, minute=0, second=0)
            naive_datetime = datetime.combine(future_date, default_time)
            local_datetime = tz.localize(naive_datetime)
            utc_datetime = local_datetime.astimezone(timezone('UTC'))
            check_time = utc_datetime.replace(tzinfo=None)
            if record.start_at < check_time:
                raise ValidationError(
                    "Thời gian bắt đầu phải kể từ ngày khi được tạo")

    @api.constrains('start_at', 'end_at', 'end_submit_at')
    def _check_fields(self):
        for record in self:
            if record.start_at >= record.end_at:
                raise ValidationError(
                    "Thời gian kết thúc duyệt phải sau thời gian bắt đầu nộp")
            if record.start_at >= record.end_submit_at or record.end_submit_at >= record.end_at:
                raise ValidationError(
                    "Thời gian kết thúc nộp phải nằm trong khoảng thời gian bắt đầu và kết thúc duyệt của danh hiệu"
                )

    @api.model
    def default_get(self, fields):
        defaults = super(Achievement, self).default_get(fields)
        if 'start_at' in fields and 'start_at' not in defaults:
            tz = timezone('Asia/Bangkok')  # Set the desired timezone
            current_date = datetime.now(tz).date()
            future_date = current_date + timedelta(days=1)
            default_time = time(hour=0, minute=0, second=0)
            naive_datetime = datetime.combine(future_date, default_time)
            local_datetime = tz.localize(naive_datetime)
            utc_datetime = local_datetime.astimezone(timezone('UTC'))
            defaults['start_at'] = utc_datetime.replace(tzinfo=None)
        if 'end_submit_at' in fields and 'end_submit_at' not in defaults:
            tz = timezone('Asia/Bangkok')  # Set the desired timezone
            current_date = datetime.now(tz).date()
            future_date = current_date + timedelta(days=1)
            default_time = time(hour=23, minute=59, second=59)
            naive_datetime = datetime.combine(future_date, default_time)
            local_datetime = tz.localize(naive_datetime)
            utc_datetime = local_datetime.astimezone(timezone('UTC'))
            defaults['end_submit_at'] = utc_datetime.replace(tzinfo=None)
        if 'end_at' in fields and 'end_at' not in defaults:
            tz = timezone('Asia/Bangkok')  # Set the desired timezone
            current_date = datetime.now(tz).date()
            future_date = current_date + timedelta(days=2)
            default_time = time(hour=23, minute=59, second=59)
            naive_datetime = datetime.combine(future_date, default_time)
            local_datetime = tz.localize(naive_datetime)
            utc_datetime = local_datetime.astimezone(timezone('UTC'))
            defaults['end_at'] = utc_datetime.replace(tzinfo=None)
        return defaults

    @api.onchange('end_submit_at')
    def set_time_end_submit_at(self):
        for record in self:
            tz = timezone('Asia/Bangkok')  # Set the desired timezone
            current_date = record.end_submit_at + timedelta(days=1)
            default_time = time(hour=23, minute=59, second=59)
            naive_datetime = datetime.combine(current_date, default_time)
            local_datetime = tz.localize(naive_datetime)
            utc_datetime = local_datetime.astimezone(timezone('UTC'))
            print(utc_datetime)
            print(utc_datetime.replace(tzinfo=None))
            record.end_submit_at = utc_datetime.replace(tzinfo=None)

    @api.onchange('end_at')
    def set_time_end_at(self):
        for record in self:
            tz = timezone('Asia/Bangkok')  # Set the desired timezone
            current_date = record.end_at + timedelta(days=1)
            default_time = time(hour=23, minute=59, second=59)
            naive_datetime = datetime.combine(current_date, default_time)
            local_datetime = tz.localize(naive_datetime)
            utc_datetime = local_datetime.astimezone(timezone('UTC'))
            record.end_at = utc_datetime.replace(tzinfo=None)

    @api.model
    def search_read(self, domain=None, fields=None, offset=0, limit=None, order=None):
        records = super(Achievement, self).search_read(
            domain=domain, fields=fields, offset=offset, limit=limit, order=order)
        access_time = datetime.now()
        for record in records:
            self.browse(record['id']).write({'last_updated': access_time})
        return records

    def save_and_redirect(self):
        text = """Lưu danh hiệu thành công"""
        query = 'delete from display_dialog_box'
        self.env.cr.execute(query)
        value = self.env['display.dialog.box'].sudo().create({'text': text})
        return {
            'type': 'ir.actions.act_window',
            'name': 'Thông báo',
            'res_model': 'display.dialog.box',
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
            'res_id': value.id
        }

    def action_view_graph(self):
        exist = self.env['achievement.graph.report'].search([
            ('achievement_id', '=', self.id)
        ])
        department_list = self.env['manage_user_depart.department'].search([])
        if not exist:
            for department in department_list:

                total_list = self.env['achievement.user.list'].search([
                    ("donvi_name", '=', department.name),
                    ("achievement_id", '=', self.id)
                ])
                current_list = self.env['achievement.user.list'].search([
                    ('achievement_id.id', '=', self.id),
                    ('user_approve', '=', True),
                    ('donvi_name', '=', department.name),
                ])

                total = int(len(total_list))
                current = int(len(current_list))

                self.env['achievement.graph.report'].create({
                    'achievement_id': self.id,
                    'depart_name': department.name,
                    'type': "a_submit",
                    'num': total,
                })

                self.env['achievement.graph.report'].create({
                    'achievement_id': self.id,
                    'depart_name': department.name,
                    'type': "b_accepted",
                    'num': current,
                })
        else:
            for department in department_list:
                total_list = self.env['achievement.user.list'].search([
                    ("donvi_name", '=', department.name),
                    ("achievement_id", '=', self.id)
                ])
                current_list = self.env['achievement.user.list'].search([
                    ('achievement_id.id', '=', self.id),
                    ('user_approve', '=', True),
                    ('donvi_name', '=', department.name),
                ])
                total = int(len(total_list))
                current = int(len(current_list))
                temp_submit = self.env['achievement.graph.report'].search([
                    ('achievement_id', '=', self.id),
                    ('depart_name', '=', department.name),
                    ('type', '=', 'a_submit')
                ])
                temp_submit.write({
                    'num': total,
                })
                temp_accepted = self.env['achievement.graph.report'].search([
                    ('achievement_id', '=', self.id),
                    ('depart_name', '=', department.name),
                    ('type', '=', 'b_accepted')
                ])
                temp_accepted.write({
                    'num': current,
                })

        return {
            'name': self.name,
            'type': 'ir.actions.act_window',
            'view_mode': 'graph',
            'view_id': self.env.ref('graph_view_achievement.achievement_statistic_view_graph').id,
            'res_model': 'achievement.graph.report',
            'target': 'current',
            'context': {
                'search_default_achievement_id': self.id,
            }

        }

    def action_view_graph_achievement(self):
        exist = self.env['achievement.department.statistic'].search([
            ('achievement_id', '=', self.id)
        ])
        department_list = self.env['manage_user_depart.department'].search([])
        if not exist:
            for department in department_list:
                total_list = self.env['achievement.user.list'].search([
                    ("donvi_name", '=', department.name),
                    ("achievement_id", '=', self.id)
                ])
                current_list = self.env['achievement.user.list'].search([
                    ('achievement_id.id', '=', self.id),
                    ('user_approve', '=', True),
                    ('donvi_name', '=', department.name),
                ])
                num_A_list = self.env['achievement.user.list'].search([
                    ('achievement_id.id', '=', self.id),
                    ('user_approve', '=', True),
                    ('status_user', '=', 'Đã đạt (A)'),
                    ('donvi_name', '=', department.name),])
                num_B_list = self.env['achievement.user.list'].search([
                    ('achievement_id.id', '=', self.id),
                    ('user_approve', '=', True),
                    ('status_user', '=', 'Cần bổ sung (B)'),
                    ('donvi_name', '=', department.name),])
                num_C_list = self.env['achievement.user.list'].search([
                    ('achievement_id.id', '=', self.id),
                    ('user_approve', '=', True),
                    ('status_user', '=', 'Không đạt (C)'),
                    ('donvi_name', '=', department.name),])
                # -------------------------------------------------
                total = int(len(total_list))
                current = int(len(current_list))
                num_A = int(len(num_A_list))
                num_B = int(len(num_B_list))
                num_C = int(len(num_C_list))
                # -------------------------------------------------
                self.env['achievement.department.statistic'].create({
                    'achievement_id': self.id,
                    'depart_id': department.code,
                    'depart_name': department.name,
                    'num_of_submit': total,
                    'num_of_accept': current,
                    'num_of_A': num_A,
                    'num_of_B': num_B,
                    'num_of_C': num_C,

                })
        else:
            for department in department_list:
                total_list = self.env['achievement.user.list'].search([
                    ("donvi_name", '=', department.name),
                    ("achievement_id", '=', self.id)
                ])
                current_list = self.env['achievement.user.list'].search([
                    ('achievement_id.id', '=', self.id),
                    ('user_approve', '=', True),
                    ('donvi_name', '=', department.name),
                ])
                num_A_list = self.env['achievement.user.list'].search([
                    ('achievement_id.id', '=', self.id),
                    ('user_approve', '=', True),
                    ('status_user', '=', 'Đã đạt (A)'),
                    ('donvi_name', '=', department.name),])
                num_B_list = self.env['achievement.user.list'].search([
                    ('achievement_id.id', '=', self.id),
                    ('user_approve', '=', True),
                    ('status_user', '=', 'Cần bổ sung (B)'),
                    ('donvi_name', '=', department.name),])
                num_C_list = self.env['achievement.user.list'].search([
                    ('achievement_id.id', '=', self.id),
                    ('user_approve', '=', True),
                    ('status_user', '=', 'Không đạt (C)'),
                    ('donvi_name', '=', department.name),])
                # -------------------------------------------------
                total = int(len(total_list))
                current = int(len(current_list))
                num_A = int(len(num_A_list))
                num_B = int(len(num_B_list))
                num_C = int(len(num_C_list))
                # -------------------------------------------------
                temp = self.env['achievement.department.statistic'].search([
                    ('achievement_id', '=', self.id),
                    ('depart_id', '=', department.code),
                    ('depart_name', '=', department.name),
                ])
                temp.write({
                    'num_of_submit': total,
                    'num_of_accept': current,
                    'num_of_A': num_A,
                    'num_of_B': num_B,
                    'num_of_C': num_C,
                })
        return {
            'name': self.name,
            'type': 'ir.actions.act_window',
            'view_mode': 'tree',
            'view_id': self.env.ref('graph_view_achievement.achievement_statistic_view_tree').id,
            'res_model': 'achievement.department.statistic',
            'target': 'current',
            'flags': {'hasSelectors': False},
            'context': {
                'graph_buttons': [{
                    'action': "action_view_graph",
                    'name': "Xem biểu đồ",
                    'model': 'create_achievement.achievement'
                }]
            },
            'domain': [('achievement_id', '=', self.id)],
        }
    def import_chuadien(self):
        # test = self.env['achievement.user.list'].browse(502)
        # for submit in test.submit_list:
        #     print(submit.id)
        #     print(submit.criteria_name)
        #     print(submit.submit_content)
        temp = self.env['achievement.submit'].search([
            ('submit_content','=', False),
        ])
        for record in temp:
            if(record.parent_id.user_name):
                record.submit_content = "Chưa điền"
            else: 
                print (record.user_id.name)
                record.unlink()


    def get_info(self, record):
        ten = "Họ và tên: " + str(record.user_name) if record.user_name else ""
        mssv = "MSSV: " + str(record.mssv_mscb) if record.mssv_mscb else ""
        ngaysinh = "Ngày sinh: " + fields.Date.to_string(record.birthday) if record.birthday else ""
        email =  "Email: " + record.user_id.email if record.user_id and record.user_id.email else ""
        donvi = "Đơn vị: " + str(record.donvi_name) if record.donvi_name else ""
        sdt = "SĐT: " + str(record.sdt) if record.sdt else ""
        print(ten)
        print(mssv)
        print(ngaysinh)
        print(email)
        print(donvi)
        print(sdt)
        return ten + '\n' + mssv + '\n' + donvi + '\n' + email + '\n' + sdt

    def get_content(self, record):
        submit_list = record.submit_list.filtered(lambda r: r.submit_content != 'Chưa điền')
        content = ""
        content_extra = ""
        current_group_name = ""
        current_group_name_extra = ""
        for submit in submit_list:
            group_name = submit.criteria.parent_id.parent_id.name
            if 'tiêu biểu' in group_name.lower():
                if current_group_name_extra == "":
                    current_group_name_extra = group_name
                    content_extra = "* " + current_group_name_extra
                elif current_group_name_extra != group_name:
                    current_group_name_extra = group_name
                    content_extra += '\n'+ "* " + current_group_name_extra
                print(submit.parent_id.user_name)
                print(submit.criteria_name)
                print(submit.submit_content)
                content_extra += '\n' + "- " + submit.criteria_name + ": " + submit.submit_content
            else:
                if current_group_name == "":
                    current_group_name = group_name
                    content = "* " + current_group_name
                elif current_group_name != group_name:
                    current_group_name = group_name
                    content += '\n'+ "* " + current_group_name
                print(submit.parent_id.user_name)
                print(submit.criteria_name)
                print(submit.submit_content)
                content += '\n' + "- " + submit.criteria_name + ": " + submit.submit_content
        return content, content_extra

    def action_export_list(self):
        record_list = self.env['achievement.user.list'].search([
            ('achievement_id','=', self.id),
        ])

        sorted_record_list = record_list.sorted(key=lambda r: r.donvi_name)

        buffer = StringIO()
        writer = csv.writer(buffer)

        header = ["STT", "Thông tin cá nhân", "Nội dung khai thành tích", "Đề cử tiêu biểu"]
        header = ["STT", "Thông tin cá nhân"]
        writer.writerow(header)
        stt = 1
        for record in sorted_record_list:
            content = self.get_content(record)
            thongtincanhan=self.get_info(record)
            noidungkhai=content[0]
            decutieubieu=content[1]
            data_row = [stt, thongtincanhan]
            data_row = [stt, thongtincanhan, noidungkhai, decutieubieu]
            writer.writerow(data_row)
        

        self.exported_data = base64.b64encode(buffer.getvalue().encode('utf-8'))

        buffer.close()
        self.csv_name = "danh_sach_ho_so.csv"
      
        return {
            'name': 'exported_data.csv',
            'type': 'ir.actions.act_url',
            'url': "web/content/?model=create_achievement.achievement&id=" + str(self.id) + "&filename_field=csv_name&field=exported_data&download=true&name=hehe",
            'target': 'self',
        }
