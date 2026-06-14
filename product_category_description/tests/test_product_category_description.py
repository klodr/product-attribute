# Copyright 2026 Altixia (https://altixia.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase


class TestProductCategoryDescription(TransactionCase):
    def test_category_description(self):
        category = self.env["product.category"].create(
            {"name": "Test category", "description": "Some description"}
        )
        self.assertEqual(category.description, "Some description")

    def test_description_default_empty(self):
        category = self.env["product.category"].create({"name": "No desc"})
        self.assertEqual(category.description, "")
