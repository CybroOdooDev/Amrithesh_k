# -*- coding: utf-8 -*-

from odoo import fields, models
from odoo.exceptions import ValidationError


class RunQuery(models.Model):
    """runs query from the model"""
    _name = 'run.query'

    name = fields.Char()

    def action_execute_query(self):
        """function to execute sql query"""
        try:
            self.env.cr.execute(f'{self.name}')
            return {
                'effect': {
                    'fadeout': 'slow',
                    'message': 'Query Executed',
                    'type': 'rainbow_man',
                }
            }
        except:
            raise ValidationError("Invalid Query")

