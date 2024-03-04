from appconf import AppConf
from django.conf import settings


class DNAustriaAppConf(AppConf):
    EVENT_TARGET_AUDIENCE = [60, 70]
    EVENT_TOPICS = [400]
    EVENT_CLASSIFICATION = "scheduled"
    EVENT_IS_ONLINE = False
    ORGANIZATION_NAME = "Medizinische Universität Graz"
    EVENT_ADDRESS_STREET = "Neue Stiftingtalstraße 6"
    EVENT_ADDRESS_CITY = "Graz"
    EVENT_ADDRESS_ZIP = "8010"
    EVENT_ADDRESS_STATE = "Steiermark"
    EVENT_FALLBACK_CONTACT = "Med Uni Graz, Events"
    EVENT_FALLBACK_EMAIL = "events@medunigraz.at"
    LOCATION = [47.08064, 15.46992]
    DESCRIPTION_LENGTH = 200

    class Meta:
        prefix = "dnaustria"
