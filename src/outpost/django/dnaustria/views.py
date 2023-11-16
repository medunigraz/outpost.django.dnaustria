from textwrap import wrap

from braces.views import JSONResponseMixin
from bs4 import BeautifulSoup
from django.utils import timezone
from django.views.generic import View
from outpost.django.typo3.models import (
    Category,
    Event,
)

from .conf import settings


# https://django-braces.readthedocs.io/en/latest/other.html#jsonresponsemixin
class DataView(JSONResponseMixin, View):
    def get(self, *args, **kwargs):
        events = Event.objects.filter(
            categories=Category.objects.get(pk=269), start__gte=timezone.now()
        )
        # context_dict = dict(events=list())
        context_dict = dict(events=list())

        for event in events:

            description = BeautifulSoup(event.body).get_text()

            context_dict.get("events").append(
                {
                    "event_title": event.title,
                    "event_description": wrap(
                        description, settings.DNAUSTRIA_DESCRIPTION_LENGTH
                    )[0],
                    "event_link": event.link,
                    "event_target_audience": settings.DNAUSTRIA_EVENT_TARGET_AUDIENCE,
                    "event_topics": settings.DNAUSTRIA_EVENT_TOPICS,
                    "event_start": event.start.isoformat(),
                    "event_end": event.end.isoformat(),
                    "event_classification": settings.DNAUSTRIA_EVENT_CLASSIFICATION,
                    "event_has_fees": event.attending_fees,
                    "event_is_online": settings.DNAUSTRIA_EVENT_IS_ONLINE,
                    "organization_name": settings.DNAUSTRIA_ORGANIZATION_NAME,
                    "event_contact_name": event.contact,
                    "event_contact_email": event.email,
                    "event_address_street": settings.DNAUSTRIA_EVENT_ADDRESS_STREET,
                    "event_address_city": settings.DNAUSTRIA_EVENT_ADDRESS_CITY,
                    "event_address_zip": settings.DNAUSTRIA_EVENT_ADDRESS_ZIP,
                    "event_address_state": settings.DNAUSTRIA_EVENT_ADDRESS_STATE,
                    "location": settings.DNAUSTRIA_LOCATION,
                }
            )

        # https://github.com/Julian/jsonschema
        return self.render_json_response(context_dict)
