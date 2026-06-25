from odoo import fields,models,api
from odoo.exceptions import ValidationError
class CustomerRequest(models.Model):
    _name="crm.customer.request" 

    product_id=fields.Many2one('product.template',required=True)
    opportunity_id=fields.Many2one('crm.lead',required=True)
    date=fields.Date(required=True,default=fields.Date.today)
    description=fields.Text()
    qty=fields.Float(default=1)
    @api.model
    def create(self, vals):
     lead = self.env['crm.lead'].browse(vals.get('opportunity_id'))
     
     if lead.stage_id.name != "New":
      raise ValidationError(
            "Chỉ được thêm khi Opportunity ở trạng thái New"
        )
     return super().create(vals)

    def write(self, vals):
     for rec in self:
        if rec.opportunity_id.stage_id.name != "New":
            raise ValidationError("Chỉ được sửa khi Opportunity ở trạng thái New")

     return super().write(vals)

    def unlink(self):
     for rec in self:
        if rec.opportunity_id.stage_id.name != "New":
            raise ValidationError("Chỉ được xóa khi Opportunity ở trạng thái New")

     return super().unlink()