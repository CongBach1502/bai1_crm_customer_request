from odoo import fields,models,api
class Crmlead(models.Model):
    _inherit='crm.lead'
    
    request_ids =fields.One2many(
        'crm.customer.request',
        'opportunity_id'
    )
    sales_qty=fields.Float(
        string="Doanh Số",
        compute='_compute_sales_qty'
    )
    
    @api.depends('request_ids.qty')
    def _compute_sales_qty(self):
        for lead in self:
            lead.sales_qty=sum(lead.request_ids.mapped('qty'))
    expected_revenue=fields.Float(
         string="Doanh Thu",
         compute='_compute_expected_revenue')
    @api.depends('request_ids.qty','request_ids.product_id.list_price')
    def _compute_expected_revenue(self):
        for lead in self:
            lead.expected_revenue=sum(line.qty * line.product_id.list_price
            for line in lead.request_ids
            )
   
    def _prepare_opportunity_quotation_context(self):
     context = super()._prepare_opportunity_quotation_context()

     order_lines = []

     for req in self.request_ids:
        order_lines.append((0, 0, {
            'product_id': req.product_id.product_variant_id.id,
            'product_uom_qty': req.qty,
        }))

     context['default_order_line'] = order_lines

     return context
