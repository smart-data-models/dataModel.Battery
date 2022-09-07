[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: StorageBatteryMeasurement  
=================================  
[Open License](https://github.com/smart-data-models//dataModel.Battery/blob/master/StorageBatteryMeasurement/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Global description: **Storage Battery Observed Data Model is intended to measure the remaining energy capacity in a battery, which can be redistributed in the form of electrical energy. These functions apply from a source which depends on the type of battery (reference to the attribute 'batteryType' of the Data Model `StorageBatteryDevice`).**  
version: 0.0.2  

## List of properties  

- `activePower`: Active Power, where 'phi' is the phase shift of the current compared to the voltage. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **KWT** represents Kilowatt  - `address`: The mailing address  - `alternateName`: An alternative name for this item  - `areaServed`: The geographic area where a service or offered item is provided  - `batteryAssessmentMethods`: Assessment and calculation methods for measurements assessing the condition of the battery. Enum:'ampereHourMetry, dischargeTest, electrolyteDensity, highFrequencyImpedance, lowFrequencyImpedance, mathematicalModel, operatingVoltageWithClosedCircuit, quiescentVoltageWithOpenCircuit'  - `batteryLevel`: Device's battery level. A unique value of the following value 0.0=battery empty, 1.0=Battery full, -1.0=Transiently not determined.  - `batteryStatus`: Status of the battery during the measurement( giving or not energy). Enum:'consumingEnergy, givingEnergy, standby'  - `current`: Current. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **AMP** represents Ampere.   - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateEnergyMeteringStarted`: The starting date for metering energy in an ISO8601 UTC format  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `dateObservedFrom`: Observation period: Start date and time in an ISO8601 UTC format. The attribute can be used in addition to the 'dateObserved' attribute when it corresponds to a time interval to be highlighted.  - `dateObservedTo`: Observation period: End date and time in an ISO8601 UTC format. The attribute can be used in addition to the 'dateObserved' attribute when it corresponds to a time interval to be highlighted.  - `deepOfDischarge`: The Deep of Discharge (Code DoD) expressed in % is the ratio between the capacity already discharged and the nominal capacity of the accumulator. That is to say the energy consumed in the battery. Rule  [DOD] = 100 % - [SOC]. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **P1** represents Percent  - `description`: A description of this item  - `id`: Unique identifier of the entity  - `inverterStatus`: Status of the inverter. A combination of values. Enum:'00-Onsector, 01-PowerFailure/OnBattery, 02-LossCommunication, 03-BatteryFault, 04-SystemShutDown, 05-TensionDip, 06-OverVoltage, 07-VoltageDrop, 08-VoltageIncrease, 09-LineNoise, 10-FrequencyVariation, 11-TransientDistortion, 12-HarmonicDistortion'  - `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `name`: The name of this item.  - `openCircuitVoltage`: The Open Circuit Voltage (Code OCV) expressed in Volt is the difference of electrical potential between two terminals of a device when disconnected from any circuit. There is no external load connected and No external electric current flows between the terminals. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **VLT** represents Volt  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `reactivePower`: Reactive Power used by circuits. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **K5** represents kilovolt-ampere-reactive  - `refPointOfInterest`: Reference to a [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) linked with the Repository.  - `refStorageBatteryDevice`: Reference to a [Storage Battery Device](https://github.com/FIWARE/data-models/blob/master/specs/Energy/StorageBatteryDevice/doc/spec.md) which captured this observation, if the entity is used.  - `seeAlso`: list of uri pointing to additional resources about the item  - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `stateOfCharge`: The State of Charge (Code SoC) expressed in % is defined as the ratio between the remaining and the current capacities. The current capacity is the maximum capacity that can be withdrawn from the fully charged battery under specific discharge conditions. Rule [SOC] + [DOD] = 100 %. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **P1** represents Percent  - `stateOfHealth`: The State of Health  (Code SoH) expressed in % is defined as the ratio between the maximum amount of charge that a fully charged battery can provide under its nominal discharge regime, and its nominal capacity. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **P1** represents Percent  - `temperature`: Main Temperature recorded at the time of Observation compared to the  nominal reference temperature of the device. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **CEL** represents Degree Celsius  - `type`: NGSI Entity type. It has to be StorageBatteryMeasurement    
Required properties  
- `dateObserved`  - `id`  - `location`  - `stateOfCharge`  - `type`  ## Data Model description of properties  
Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
StorageBatteryMeasurement:    
  description: 'Storage Battery Observed Data Model is intended to measure the remaining energy capacity in a battery, which can be redistributed in the form of electrical energy. These functions apply from a source which depends on the type of battery (reference to the attribute ''batteryType'' of the Data Model `StorageBatteryDevice`).'    
  properties:    
    activePower:    
      description: 'Active Power, where ''phi'' is the phase shift of the current compared to the voltage. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **KWT** represents Kilowatt'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Kilowatt.    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    batteryAssessmentMethods:    
      description: 'Assessment and calculation methods for measurements assessing the condition of the battery. Enum:''ampereHourMetry, dischargeTest, electrolyteDensity, highFrequencyImpedance, lowFrequencyImpedance, mathematicalModel, operatingVoltageWithClosedCircuit, quiescentVoltageWithOpenCircuit'''    
      enum:    
        - ampereHourMetry    
        - dischargeTest    
        - electrolyteDensity    
        - highFrequencyImpedance    
        - lowFrequencyImpedance    
        - mathematicalModel    
        - operatingVoltageWithClosedCircuit    
        - quiescentVoltageWithOpenCircuit    
      type: string    
      x-ngsi:    
        type: Property    
    batteryLevel:    
      description: 'Device''s battery level. A unique value of the following value 0.0=battery empty, 1.0=Battery full, -1.0=Transiently not determined.'    
      oneOf:    
        - maximum: 1    
          minimum: 0    
          type: number    
        - enum:    
            - -1    
          type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    batteryStatus:    
      description: 'Status of the battery during the measurement( giving or not energy). Enum:''consumingEnergy, givingEnergy, standby'''    
      enum:    
        - consumingEnergy    
        - givingEnergy    
        - standby    
      type: string    
      x-ngsi:    
        type: Property    
    current:    
      description: 'Current. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **AMP** represents Ampere. '    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Ampere    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateEnergyMeteringStarted:    
      description: 'The starting date for metering energy in an ISO8601 UTC format'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime.    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateObservedFrom:    
      description: 'Observation period: Start date and time in an ISO8601 UTC format. The attribute can be used in addition to the ''dateObserved'' attribute when it corresponds to a time interval to be highlighted.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateObservedTo:    
      description: 'Observation period: End date and time in an ISO8601 UTC format. The attribute can be used in addition to the ''dateObserved'' attribute when it corresponds to a time interval to be highlighted.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    deepOfDischarge:    
      description: 'The Deep of Discharge (Code DoD) expressed in % is the ratio between the capacity already discharged and the nominal capacity of the accumulator. That is to say the energy consumed in the battery. Rule  [DOD] = 100 % - [SOC]. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **P1** represents Percent'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number.    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &storagebatterymeasurement_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    inverterStatus:    
      description: 'Status of the inverter. A combination of values. Enum:''00-Onsector, 01-PowerFailure/OnBattery, 02-LossCommunication, 03-BatteryFault, 04-SystemShutDown, 05-TensionDip, 06-OverVoltage, 07-VoltageDrop, 08-VoltageIncrease, 09-LineNoise, 10-FrequencyVariation, 11-TransientDistortion, 12-HarmonicDistortion'''    
      items:    
        enum:    
          - 00-OnSector    
          - 01-PowerFailure/OnBattery    
          - 02-LossCommunication    
          - 03-BatteryFault    
          - 04-SystemShutDown    
          - 05-TensionDip    
          - 06-OverVoltage    
          - 07-VoltageDrop    
          - 08-VoltageIncrease    
          - 09-LineNoise    
          - 10-FrequencyVariation    
          - 11-TransientDistortion    
          - 12-HarmonicDistortion    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Point'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON LineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Polygon'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPoint'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiLineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPolygon'    
          type: object    
      x-ngsi:    
        type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    openCircuitVoltage:    
      description: 'The Open Circuit Voltage (Code OCV) expressed in Volt is the difference of electrical potential between two terminals of a device when disconnected from any circuit. There is no external load connected and No external electric current flows between the terminals. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **VLT** represents Volt'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Volt.    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *storagebatterymeasurement_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    reactivePower:    
      description: 'Reactive Power used by circuits. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **K5** represents kilovolt-ampere-reactive'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: kilovolt-ampere-reactive.    
    refPointOfInterest:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to a [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) linked with the Repository.'    
      x-ngsi:    
        type: Relationship    
    refStorageBatteryDevice:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to a [Storage Battery Device](https://github.com/FIWARE/data-models/blob/master/specs/Energy/StorageBatteryDevice/doc/spec.md) which captured this observation, if the entity is used.'    
      x-ngsi:    
        type: Relationship    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    stateOfCharge:    
      description: 'The State of Charge (Code SoC) expressed in % is defined as the ratio between the remaining and the current capacities. The current capacity is the maximum capacity that can be withdrawn from the fully charged battery under specific discharge conditions. Rule [SOC] + [DOD] = 100 %. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **P1** represents Percent'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number.    
        type: Property    
    stateOfHealth:    
      description: 'The State of Health  (Code SoH) expressed in % is defined as the ratio between the maximum amount of charge that a fully charged battery can provide under its nominal discharge regime, and its nominal capacity. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **P1** represents Percent'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number.    
        type: Property    
    temperature:    
      description: 'Main Temperature recorded at the time of Observation compared to the  nominal reference temperature of the device. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **CEL** represents Degree Celsius'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'celsius degrees .'    
    type:    
      description: 'NGSI Entity type. It has to be StorageBatteryMeasurement'    
      enum:    
        - StorageBatteryMeasurement    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - location    
    - dateObserved    
    - stateOfCharge    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Battery/blob/master/StorageBatteryMeasurement/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/data-models.Energy/StorageBatteryMeasurement/schema.json    
  x-model-tags: ""    
  x-version: 0.0.2    
```  
</details>    
## Example payloads    
#### StorageBatteryMeasurement NGSI-v2 key-values Example    
Here is an example of a StorageBatteryMeasurement in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:StorageBatteryMeasurement:StorageBatteryMeasurement:MNCA-SBM-T1-G0-027",  
  "type": "StorageBatteryMeasurement",  
  "name": "SBM-T1-G0-027",  
  "alternateName": "AirPort – global Observation",  
  "description": "Measurement of the level of Solar Storage Battery",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      43.664810,  
      7.196545  
    ]  
  },  
  "address": {  
    "addressCountry": "FR",  
    "addressLocality": "Nice",  
    "streetAddress": "Airport - Terminal 1 - Ground 0 - Local  27"  
  },  
  "areaServed": "Nice Aeroport",  
  "dateObserved": "2020-03-17T08:45:00Z",  
  "refStorageBatteryDevice": "urn:ngsi-ld:StorageBatteryDevice:SBD-T1-G0-027",  
  "batteryLevel": -1,  
  "batteryStatus": "standby",  
  "batteryAssessmentMethods": "dischargeTest",  
  "dateEnergyMeteringStarted": "2020-03-16T10:30:00Z",  
  "stateOfCharge": 0.70,  
  "deepOfDischarge": 0.286,  
  "stateOfHealth": 0.8235,  
  "openCircuitVoltage": 47.3,  
  "inverterStatus": [  
    "00-OnSector",  
    "06-OverVoltage"  
  ]  
}  
```  
#### StorageBatteryMeasurement NGSI-v2 normalized Example    
Here is an example of a StorageBatteryMeasurement in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:StorageBatteryMeasurement:StorageBatteryMeasurement:MNCA-SBM-T1-G0-027",  
  "type": "StorageBatteryMeasurement",  
  "name": {  
    "type": "Property",  
    "value": "SBM-T1-G0-027"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "AirPort – global Observation"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Measurement of the level of Solar Storage Battery"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates ": [  
        43.664810,  
        7.196545  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "addressCountry": "FR",  
      "addressLocality": "Nice",  
      "streetAddress": "Airport - Terminal 1 - Ground 0 - Local  27"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Nice Aeroport"  
  },  
  "dateObserved": {  
    "type": "Property",  
    "value": {  
      "type": "DateTime",  
      "value": "2020-03-17T08:45:00Z"  
    }  
  },  
  "refStorageBatteryDevice": {  
    "type": "RelationShip",  
    "object": "urn:ngsi-ld:StorageBatteryDevice:SBD-T1-G0-027"  
  },  
  "batteryLevel": {  
    "type": "Property",  
    "value": -1  
  },  
  "batteryStatus": {  
    "type": "Property",  
    "value": "standby"  
  },  
  "batteryAssessmentMethods": {  
    "type": "Property",  
    "value": "dischargeTest"  
  },  
  "dateEnergyMeteringStarted": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2020-03-16T10:30:00Z"  
    }  
  },  
  "stateOfCharge": {  
    "type": "Property",  
    "value": 0.70  
  },  
  "measurementInterval": {  
    "type": "Property",  
    "value": 1  
  },  
  "temperature": {  
    "type": "Property",  
    "value": 25.2  
  },  
  "deepOfDischarge": {  
    "type": "Property",  
    "value": 0.286  
  },  
  "measurementInterval": {  
    "type": "Property",  
    "value": 1  
  },  
  "temperature": {  
    "type": "Property",  
    "value": 24.3  
  },  
  "stateOfHealth": {  
    "type": "Property",  
    "value": 0.8235  
  },  
  "openCircuitVoltage": {  
    "type": "Property",  
    "value": 47.3  
  },  
  "inverterStatus": {  
    "type": "Property",  
    "value": [  
      "00-OnSector",  
      "06-OverVoltage"  
    ]  
  }  
}  
```  
#### StorageBatteryMeasurement NGSI-LD key-values Example    
Here is an example of a StorageBatteryMeasurement in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
    "id": "urn:ngsi-ld:StorageBatteryMeasurement:StorageBatteryMeasurement:MNCA-SBM-T1-G0-027",  
    "type": "StorageBatteryMeasurement",  
    "address": {  
        "addressCountry": "FR",  
        "addressLocality": "Nice",  
        "streetAddress": "Airport - Terminal 1 - Ground 0 - Local  27"  
    },  
    "alternateName": "AirPort \u2013 global Observation",  
    "areaServed": "Nice Aeroport",  
    "batteryAssessmentMethods": "dischargeTest",  
    "batteryLevel": -1,  
    "batteryStatus": "standby",  
    "dateEnergyMeteringStarted": "2020-03-16T10:30:00Z",  
    "dateObserved": "2020-03-17T08:45:00Z",  
    "deepOfDischarge": 0.286,  
    "description": "Measurement of the level of Solar Storage Battery",  
    "inverterStatus": [  
        "00-OnSector",  
        "06-OverVoltage"  
    ],  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            43.66481,  
            7.196545  
        ]  
    },  
    "name": "SBM-T1-G0-027",  
    "openCircuitVoltage": 47.3,  
    "refStorageBatteryDevice": "urn:ngsi-ld:StorageBatteryDevice:SBD-T1-G0-027",  
    "stateOfCharge": 0.7,  
    "stateOfHealth": 0.8235,  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Battery/master/context.jsonld"  
    ]  
}  
```  
#### StorageBatteryMeasurement NGSI-LD normalized Example    
Here is an example of a StorageBatteryMeasurement in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
    "id": "urn:ngsi-ld:StorageBatteryMeasurement:StorageBatteryMeasurement:MNCA-SBM-T1-G0-027",  
    "type": "StorageBatteryMeasurement",  
    "address": {  
        "type": "Property",  
        "value": {  
            "addressCountry": "FR",  
            "addressLocality": "Nice",  
            "streetAddress": "Airport - Terminal 1 - Ground 0 - Local  27"  
        }  
    },  
    "alternateName": {  
        "type": "Property",  
        "value": "AirPort \u2013 global Observation"  
    },  
    "areaServed": {  
        "type": "Property",  
        "value": "Nice Aeroport"  
    },  
    "batteryAssessmentMethods": {  
        "type": "Property",  
        "value": "dischargeTest"  
    },  
    "batteryLevel": {  
        "type": "Property",  
        "value": -1  
    },  
    "batteryStatus": {  
        "type": "Property",  
        "value": "standby"  
    },  
    "dateEnergyMeteringStarted": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2020-03-16T10:30:00Z"  
        }  
    },  
    "dateObserved": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2020-03-17T08:45:00Z"  
        }  
    },  
    "deepOfDischarge": {  
        "type": "Property",  
        "value": 0.286  
    },  
    "description": {  
        "type": "Property",  
        "value": "Measurement of the level of Solar Storage Battery"  
    },  
    "inverterStatus": {  
        "type": "Property",  
        "value": [  
            "00-OnSector",  
            "06-OverVoltage"  
        ]  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates ": [  
                43.66481,  
                7.196545  
            ]  
        }  
    },  
    "name": {  
        "type": "Property",  
        "value": "SBM-T1-G0-027"  
    },  
    "openCircuitVoltage": {  
        "type": "Property",  
        "value": 47.3  
    },  
    "refStorageBatteryDevice": {  
        "type": "RelationShip",  
        "object": "urn:ngsi-ld:StorageBatteryDevice:SBD-T1-G0-027"  
    },  
    "stateOfCharge": {  
        "type": "Property",  
        "value": 0.7  
    },  
    "stateOfHealth": {  
        "type": "Property",  
        "value": 0.8235  
    },  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units  
