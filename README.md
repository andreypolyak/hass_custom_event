# custom_event — Home Assistant service to fire events

This component creates ```custom_event.fire``` service in Home Assistant which can be used to fire any event. This service may be used when it's not possible to fire event using other built-in ways. Several examples:
- fire event when button in Lovelace was pressed
- fire event when action happened with template entity (template switch, template cover, universal media player, etc.)

## Installation

1. Add ```https://github.com/andreypolyak/hass_custom_event``` as custom repository in HACS
2. Install ```custom_event``` custom component in HACS
3. Add ```custom_event:``` to configuration.yaml file in Home Assistant

## Usage

```custom_event.fire``` service has two data attributes:

| Attribute name | Optional | Description |
|-|-|-|
| ```event_type``` | No | Event type |
| ```event_data``` | Yes | Dictionary which will be passed as data to event | 

## Examples

**Service call without event data**

```yaml
service: custom_event.fire
data:
  event_type: test
```

This call will fire following event:

```json
{
  "event_type": "test",
  "data": {},
  "origin": "LOCAL",
  "time_fired": "2021-10-26T20:10:55.598258+00:00",
  "context": {
    "id": "fd8a6ece74789ab1631f394754ba430f",
    "parent_id": null,
    "user_id": null
  }
}
```

**Service call without event data**

```yaml
service: custom_event.fire
data:
  event_type: test
  event_data:
    attribute1: test1
    attribute2: test2
```

This call will fire following event:

```json
{
  "event_type": "test",
  "data": {
    "attribute1": "test1",
    "attribute2": "test2"
  },
  "origin": "LOCAL",
  "time_fired": "2021-10-26T20:14:27.518716+00:00",
  "context": {
    "id": "fe36f40052002231cc6159c72ecc01f8",
    "parent_id": null,
    "user_id": null
  }
}
```

**Template switch which fires events when switch is turned on or off**

```yaml
switch:
  - platform: template
    switches:
      ac:
        friendly_name: AC
        value_template: >
          {% if is_state("binary_sensor.living_room_ac_door", "off") %}
            off
          {% else %}
            on
          {% endif %}
        turn_on:
          service: custom_event.fire
          data_template:
            event_type: manual_ac_on
        turn_off:
          service: custom_event.fire
          data_template:
            event_type: manual_ac_off
```

**Custom button card which fires event when button is pressed**

```yaml
type: custom:button-card
template: base_label
label: Add
tap_action:
  action: call-service
  service: custom_event.fire
  service_data:
    event_type: add_logged_entity
    event_data:
      mode: entities
````
