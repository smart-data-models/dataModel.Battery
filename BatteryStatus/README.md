# Battery Status

## Description

A `Battery` entity represent a phisical battery to serve a IoT device or any
other electrical device with energy consumption. The entity is dependent to
another instance which belongs. The battery has diferents attributtes whether
if is for DC power or AC. It entity can be useful for several verticals.

## Data Model

A JSON Schema corresponding to this data model can be found
[here](../schema.json).

-   `id` : Entity's unique identifier.

-   `type` : It must be equal to `Battery`.

-   `source` : A sequence of characters giving the source of the entity data.

    -   Attribute type: Text or URL
    -   Optional

-   `dataProvider` : Specifies the URL to information about the provider of this
    information

    -   Attribute type: URL
    -   Optional

-   `refBattery` : Battery entity which it belongs.

    -   Attribute type: List of Reference to entity(ies) of type
        [Battery](../../Battery/doc/spec.md)
    -   Mandatory

-   `dateObserved` : The date and time of this observation in ISO8601 UTCformat.
    It can be represented by an specific time instant or by an ISO8601 interval.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime) or an ISO8601
        interval represented as [Text](https://schema.org/Text).
    -   Mandatory

-   `status` : the battery can be no giving (or not) energy and the same time
    consuming (or not energy)

    -   Attribute type: Property.
    -   Allowed values: (`standby`, `consumingEnergy`, `givingEnergy`)
    -   Mandatory

-   `statusPercent` : a measure in percentage of the remaining energy stored
    in the battery

    -   Attribute type: Property. [Number](http://schema.org/Number)
    -   Allowed values: Any positive integer between 0 number and 100.
    -   Mandatory

-   `acPowerInput` : A instantaneous measurement at input present only present if the battery
    work with AC. This is like the consumption measurement for the battery.

    -   Attribute type: [Number](http://schema.org/Number)
    -   Default unit: KWT, The unit code (text) of measurement given using the UN/CEFACT
        Common Code (max. 3 characters).
    -   Optional

-   `acPowerOutput` : A instantaneous measurement present only if battery gives output in AC

    -   Attribute type: [Number](http://schema.org/Number)
    -   Default unit: KWT, The unit code (text) of measurement given using the UN/CEFACT
        Common Code (max. 3 characters).
    -   Optional

-   `dcPowerInput` : A instantaneous measurement present only if battery take input in DC.
    This is like the consumption measurement of the battery.

    -   Attribute type: [Number](http://schema.org/Number)
    -   Default unit: KWT, The unit code (text) of measurement given using the UN/CEFACT
        Common Code (max. 3 characters).
    -   Optional

-   `dcPowerOutput` :  A instantaneous measurement present only if battery take input in DC

    -   Attribute type: [Number](http://schema.org/Number)
    -   Default unit: KWT, The unit code (text) of measurement given using the UN/CEFACT
        Common Code (max. 3 characters).
    -   Optional

-   `dateModified` : Last update timestamp of this entity.

    -   Attribute type: [DateTime](https://schema.org/DateTime)
    -   Read-Only. Automatically generated.

-   `dateCreated` : Entity's creation timestamp.

    -   Attribute type: [DateTime](https://schema.org/DateTime)
    -   Read-Only. Automatically generated.

**Note**: JSON Schemas only capture the NGSI simplified representation, this
means that to test the JSON schema examples with a
[FIWARE NGSI version 2](http://fiware.github.io/specifications/ngsiv2/stable)
API implementation, you need to use the `keyValues` mode (`options=keyValues`).

## Examples

### Normalized Example



### key-value pairs Example

Sample uses simplified representation for data consumers `?options=keyValues`

```json
{
  "id": "BatteryStatus:santander:energy:d95372df39",
  "type": "BatteryStatus",
  "dataProvider": "bike-in.com",
  "dataObserved": "2019-09-23T15:59:09.224Z",
  "refBattery": "Battery:santander:energy:d95372df39",
  "status": ["standby"],
  "statusPercent": "100",
  "acPowerInput": 0,
  "acPowerOutput": 0,
}
```

```json
{
  "id": "BatteryStatus:santander:energy:d95372df39",
  "type": "BatteryStatus",
  "dataProvider": "bike-in.com",
  "dataObserved": "2019-09-23T15:59:09.224Z",
  "refBattery": "Battery:santander:energy:h95372df39",
  "status": ["consumingEnergy","givingEnergy"],
  "statusPercent": "25",
  "dcPowerInput": 0.1,
  "dcPowerOutput": 0.05,
}
```

## Test it with a real service

## Open Issues
