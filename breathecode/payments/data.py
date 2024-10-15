from breathecode.payments.utils import ConsumableType, consumable, service_item

__all__ = ["get_virtual_consumables"]


def get_virtual_consumables() -> list[ConsumableType]:
    return [
        consumable(
            service_item=1,
            cohort_set=1,
            event_type_set=1,
            mentorship_service_set=1,
        ),
        consumable(
            service_item=service_item(service=1, unit_type="unit", how_many=1),
            cohort_set=1,
            event_type_set=1,
            mentorship_service_set=1,
        ),
    ]
