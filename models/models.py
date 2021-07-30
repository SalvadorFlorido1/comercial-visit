from odoo import models, fields, api




class Visit(models.Model):
    _name = 'custom.crm.visit'
    _description = 'Visit'
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(string='Description')
    customer = fields.Many2one(string='Customer', comodel_name='res.partner')
    date = fields.Datetime(string='Date')
    type = fields.Selection([('presential', 'Presential'), ('email', 'Email'), ('telephone', 'Telephone')], required=True)
    done = fields.Boolean(string="Done")
    Notes = fields.Char(string="Notes")
    Image =fields.Binary(string="Image")
    stage = fields.Many2one(comodel_name="custom.crm.visit.stage", string="Stage")

    def toggle_state(self):
        self.done = not self.done


class visit_stage(models.Model):
    _name = 'custom.crm.visit.stage'
    

    name = fields.Char(string="stage")

