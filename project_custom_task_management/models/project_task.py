from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class ProjectTask(models.Model):
    _inherit = 'project.task'

    # الحقول الإضافية
    date_start = fields.Date(string='Start Date')
    date_end = fields.Date(string='End Date')
    payment_terms = fields.Char(string='Payment Terms')
    payment_due_date = fields.Date(string='Payment Due Date')
    total_payment_amount = fields.Float(string='Total Payment Amount')
    payment_status = fields.Selection([
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('overdue', 'Overdue')
    ], string='Payment Status', default='pending')
    completion_percentage = fields.Float(string='Completion Percentage', compute='_compute_completion_percentage',
                                         store=True)

    @api.depends('date_start', 'date_end')
    def _compute_completion_percentage(self):
        for task in self:
            if task.date_start and task.date_end:
                duration = (task.date_end - task.date_start).days
                today = fields.Date.context_today(self)
                if today < task.date_start:
                    task.completion_percentage = 0.0
                elif today > task.date_end:
                    task.completion_percentage = 100.0
                else:
                    task.completion_percentage = (today - task.date_start).days / duration * 100
            else:
                task.completion_percentage = 0.0

    def _send_internal_notification(self, subject, body):
        self.message_post(
            body=body,
            subject=subject,
            subtype_id=self.env.ref('mail.mt_note').id
        )

    def _check_payment_due_dates(self):
        today = fields.Date.context_today(self)
        tasks_due_today = self.search([('payment_due_date', '=', today), ('payment_status', '=', 'pending')])
        for task in tasks_due_today:
            task._send_internal_notification(
                subject="Reminder: Payment Due Date for Task {} is Today".format(task.name),
                body="Reminder: The payment due date for Task {} is today. Please take the necessary actions.".format(
                    task.name)
            )

        overdue_tasks = self.search([('payment_due_date', '<', today), ('payment_status', '=', 'pending')])
        for task in overdue_tasks:
            task.payment_status = 'overdue'
            task._send_internal_notification(
                subject="Reminder: Payment for Task {} is Overdue".format(task.name),
                body="Reminder: The payment for Task {} is overdue. Please take the necessary actions.".format(
                    task.name)
            )

    @api.model
    def cron_send_due_date_notifications(self):
        _logger.info("Running cron_send_due_date_notifications...")
        self._check_payment_due_dates()  # تحقق من تواريخ الاستحقاق اليومي

    @api.model
    def cron_send_overdue_notifications(self):
        _logger.info("Running cron_send_overdue_notifications...")
        self._check_payment_due_dates()  # تحقق من تواريخ الدفع المتأخرة
