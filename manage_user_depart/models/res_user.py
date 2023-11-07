from odoo import models, fields, api


class User(models.Model):
    _inherit = 'res.users'

    # appraise_for = fields.One2many('create_achievement.appraise','user_id')

    mssv_mscb = fields.Char(string="MSSV/MSCB", required=True)
    gioi_tinh = fields.Selection([
        ('nam', 'Nam'),
        ('nu', 'Nữ'),
        ('khac', 'Khác')
    ], default="nam", string="Giới tính")
    sdt = fields.Char(string="Điện thoại", required=True)
    birthday = fields.Date(string="Ngày sinh")
    cmnd_cccd = fields.Char(string="CMND/CCCD")
    dantoc = fields.Char(string="Dân tộc")
    tongiao = fields.Char(string="Tôn Giáo")
    # ------Information-------
    province = fields.Many2one('user.province.info',  string='Tỉnh')
    district = fields.Many2one('user.district.info', string='Huyện')
    ward = fields.Many2one('user.ward.info', string='Xã')
    tenduong_sonha = fields.Char(string="Tên đường/Số nhà")
    # ------Contact-----------
    province_contact = fields.Many2one('user.province.info',  string='Tỉnh')
    district_contact = fields.Many2one('user.district.info', string='Huyện')
    ward_contact = fields.Many2one('user.ward.info', string='Xã')
    tenduong_sonha_contact = fields.Char(string="Tên đường/Số nhà")
    # -------------------------
    donvi = fields.Many2one('manage_user_depart.department',
                            string="Đơn vị", required=True)
    nghenghiep = fields.Char(string="Nghề nghiệp")
    # -------------------------
    hocvi = fields.Char(string="Học vị")
    trinhdo = fields.Char(string="Trình độ")
    # -------------------------

    is_fill_info = fields.Boolean(
        string="Đã cập nhập thông tin?", compute='_check_fill_info', store=True)
    is_unit_manager = fields.Boolean(
        string='Is Unit Manager', compute='_compute_is_unit_manager')

    lock_info = fields.Boolean(string='Is Unit Manager')

    is_thanh_vien = fields.Boolean(
        string="Thanh Vien?", compute='_role', store=True)
    is_ql_donvi = fields.Boolean(
        string="Quản lý đơn vị?", compute='_role', store=True)
    is_ql_hethong = fields.Boolean(
        string="Quản lý hệ thống?", compute='_role', store=True)
    is_ql_danhhieu = fields.Boolean(
        string="Quản lý danh hiệu?", compute='_role', store=True)
    is_thamdinh = fields.Boolean(
        string="Thẩm định viên?", compute='_role', store=True)

    def _compute_is_unit_manager(self):
        system_manager_group = self.env.ref(
            'access_right_user.group_system_manager')
        unit_manager_group = self.env.ref(
            'access_right_user.group_unit_manager')
        current_user = self.env.user
        for record in self:
            # Kiểm tra xem user có thuộc nhóm 'group_system_manager' hoặc không thuộc nhóm 'group_unit_manager'
            record.is_unit_manager = record.lock_info or (bool(
                unit_manager_group in current_user.groups_id) and not bool(system_manager_group in current_user.groups_id))

    @api.depends('mssv_mscb', 'sdt', 'donvi')
    def _check_fill_info(self):
        for record in self:
            if record.mssv_mscb and record.sdt and record.donvi:
                record.is_fill_info = True
            else:
                record.is_fill_info = False

    @api.model
    def create(self, vals):
        vals['lang'] = 'vi_VN'
        return super(User, self).create(vals)

    def save_success(self):
        text = """Thông tin đã được lưu thành công"""
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

    @api.model
    def action_user_by_donvi_error(self):
        user_dv_id = self.env.user.donvi.id
        domain = [('donvi', '=', user_dv_id), ('is_thamdinh', '=', False), ('is_ql_danhhieu', '=', False),
                  ('is_ql_hethong', '=', False), ('is_ql_donvi', '=', False), ('is_thanh_vien', '=', False)]
        action = {
            'name': 'Danh sách người dùng lỗi',
            'type': 'ir.actions.act_window',
            'res_model': 'res.users',
            'view_mode': 'tree,form,kanban',
            'domain': domain,
        }
        return action

    @api.model
    def action_user_by_donvi_thanhvien(self):
        user_dv_id = self.env.user.donvi.id
        domain = [('donvi', '=', user_dv_id), ('is_thanh_vien', '=', True)]
        action = {
            'name': 'Danh sách người dùng là thành viên',
            'type': 'ir.actions.act_window',
            'res_model': 'res.users',
            'view_mode': 'tree,form,kanban',
            'domain': domain,
        }
        return action

    @api.model
    def action_user_by_donvi_ql(self):
        user_dv_id = self.env.user.donvi.id
        domain = [('donvi', '=', user_dv_id), ('is_ql_donvi', '=', True)]
        action = {
            'name': 'Danh sách người dùng là Quản lý',
            'type': 'ir.actions.act_window',
            'res_model': 'res.users',
            'view_mode': 'tree,form,kanban',
            'domain': domain,
        }
        return action

    @api.depends('donvi')
    def _compute_donvi_selection(self):
        for record in self:
            record.donvi_domain = self.env.user.donvi.name

    donvi_domain = fields.Char(
        string='Domain', compute='_compute_donvi_selection')

    @api.model
    def action_user_by_donvi(self):
        user_dv_id = self.env.user.donvi.id
        domain = [('donvi', '=', user_dv_id)]
        action = {
            'name': 'Danh sách người dùng',
            'type': 'ir.actions.act_window',
            'res_model': 'res.users',
            'view_mode': 'tree,form,kanban',
            'domain': domain,
        }
        return action

    @api.depends('groups_id')
    def _role(self):
        for record in self:
            record.is_thanh_vien = bool(self.env.ref(
                'access_right_user.group_mem_user') in record.groups_id)
            record.is_ql_donvi = bool(self.env.ref(
                'access_right_user.group_unit_manager') in record.groups_id)
            record.is_ql_hethong = bool(self.env.ref(
                'access_right_user.group_system_manager') in record.groups_id)
            record.is_ql_danhhieu = bool(self.env.ref(
                'access_right_user.group_achievement_manager') in record.groups_id)
            record.is_thamdinh = bool(self.env.ref(
                'access_right_user.group_appraiser') in record.groups_id)
