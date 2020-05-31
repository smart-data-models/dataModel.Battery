# Battery

## Description

A `Battery` entity represent a phisical battery which belongs to IoT device or
any other electrical device with energy consumption. The entity is dependent to
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
    information.

    -   Attribute type: URL
    -   Optional

-   `refDevice` : A reference to the device(s) Entity device which it use this battery.

    -   Attribute type: List of Reference to entity(ies) of type
        [Device](https://github.com/Fiware/dataModels/blob/master/specs/Device/Device/doc/spec.md)
    -   Mandatory

-   `location` : Location of the weather observation represented by a GeoJSON
    geometry.

    -   Attribute type: Property. `geo:json`.
    -   Normative References:
        [https://tools.ietf.org/html/rfc7946](https://tools.ietf.org/html/rfc7946)
    -   Optional

-   `status` : Status of the battery.

    -   Attribute type: Property. List of [Text](http://schema.org/Text)
    -   Allowed values:
        -   (`working`, `outOfService`, `withIncidence`)
        -   Or any other application-specific.
    -   Metadata:
        -   `timestamp` : Timestamp corresponding to the last attribute value.
            (`observedAt` in NGSI-LD)
            -   Type: [DateTime](https://schema.org/DateTime)
    -   Optional

-   `cycleLife`: A number of reference of discharge-charge cycles until the battery
    decrease its performance

    -   Attribute type: [Number](http://schema.org/Number)
    -   Optional

-   `autonomyTime` :  time duration expressed in 8601 duration until drain battery.

    -   Attribute type: use the ISO 8601 to express [https://en.wikipedia.org/wiki/ISO_8601#Durations](https://en.wikipedia.org/wiki/ISO_8601#Durations)
    -   Optional

-   `rechargeTime` : time duration expressed in 8601 duration until re fill 100 the battery.

    -   Attribute type: use the ISO 8601 to express [https://en.wikipedia.org/wiki/ISO_8601#Durations](https://en.wikipedia.org/wiki/ISO_8601#Durations)
    -   Optional

-   `acPowerInput` : A measurement at input present only present if the battery
    work with AC. This is like the consumption measurement for the battery.

    -   Attribute type: [Number](http://schema.org/Number)
    -   Default unit: KWT, The unit code (text) of measurement given using the UN/CEFACT
        Common Code (max. 3 characters).
    -   Optional

-   `acPowerOutput` : A measurement present only if battery gives output in AC

    -   Attribute type: [Number](http://schema.org/Number)
    -   Default unit: KWT, The unit code (text) of measurement given using the UN/CEFACT
        Common Code (max. 3 characters).
    -   Optional

-   `dcPowerInput` : A measurement present only if battery take input in DC.
    This is like the consumption measurement of the battery.

    -   Attribute type: [Number](http://schema.org/Number)
    -   Default unit: KWT, The unit code (text) of measurement given using the UN/CEFACT
        Common Code (max. 3 characters).
    -   Optional

-   `dcPowerOutput` :  A measurement present only if battery take input in DC

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

Normalized NGSI

### key-value pairs Example

for AC battery

```json
{
    "id": "Battery:santander:d95372df39",
    "type": "Battery",
    "dataProvider": "bike-in.com",
    "status": ["working"],
    "location": {
        "coordinates": [-4.747901, 41.618265],
        "type": "Point"
    },
    "refDevice": "Device:santander:energy:d95372df39",
    "cicleLife": 20000,
    "autonomyTime": "PT1H",
    "rechargeTime":"PT6H",
    "acPowerInput": 1.5,
    "acPowerOutput": 0.5
}
```
for DC battery

```json
{
    "id": "Battery:santander:d95372df39",
    "type": "Battery",
    "dataProvider": "bike-in.com",
    "status": ["working"],
    "location": {
        "coordinates": [-4.747901, 41.618265],
        "type": "Point"
    },
    "refDevice": "Device:santander:energy:d95372df39",
    "cicleLife": 20000,
    "autonomyTime": "PT3H",
    "rechargeTime": "PT6H",
    "dcPowerInput": 0.01,
    "dcPowerOutput": 0.01
}
```

## Test it with a real service

## Open Issues
