from datetime import timedelta

import pytest
from django.utils import timezone

from .models import Inventory


@pytest.mark.django_db
class TestInventoryExpiration:
    def test_create_item_with_expiration_date(self):
        item = Inventory.objects.create(
            name="Test Item",
            catalog_number="Test Catalog Number",
            lot_number="Test Lot Number",
            quantity=1,
            unit="mL",
            volume=100,
            expires_on=timezone.localdate() + timedelta(days=5),
            manufacturer="Test Manufacturer",
            provider="Test Provider",
            comments="Test Comments",
        )
        assert item.expires_on is not None

    def test_is_expired_false_when_no_expiration_date(self):
        item = Inventory(
            name="No Expiration Item",
        )
        assert item.is_expired is False

    def test_is_expired_true_when_expiration_date_in_past(self):
        item = Inventory(
            name="Expired Item",
            expires_on=timezone.localdate() - timedelta(days=5),
        )
        assert item.is_expired is True

    def test_is_expired_false_when_expiration_date_today(self):
        item = Inventory(
            name="Expires Today Item",
            expires_on=timezone.localdate(),
        )
        assert item.is_expired is False

    def test_is_expired_false_when_expiration_date_in_future(self):
        item = Inventory(
            name="Expired Future Item",
            expires_on=timezone.localdate() + timedelta(days=5),
        )
        assert item.is_expired is False
