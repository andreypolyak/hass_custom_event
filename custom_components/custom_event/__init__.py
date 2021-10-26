from homeassistant.helpers.typing import ConfigType, HomeAssistantType, ServiceCallType
import voluptuous as vol

DOMAIN = "custom_event"

CALL_SCHEMA = vol.Schema(
    {
        vol.Required("event_type"): vol.All(str, vol.Length(min=1, max=64)),
        vol.Optional("event_data", default={}): dict,
    }
)


async def async_setup(hass: HomeAssistantType, config: ConfigType):
    async def handle_fire(call: ServiceCallType):
        event_type = call.data.get("event_type")
        event_data = call.data.get("event_data")
        hass.bus.async_fire(event_type, event_data)

    hass.services.async_register(DOMAIN, "fire", handle_fire, CALL_SCHEMA)
    return True
