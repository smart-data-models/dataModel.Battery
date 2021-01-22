Entity: StorageBatteryDevice  
============================  
[Open License](https://github.com/smart-data-models//dataModel.Battery/blob/master/StorageBatteryDevice/LICENSE.md)  
Global description: **The storage battery device data model is intended to describe the technical characteristics of the battery and the charging and discharging conditions of the energy. The charging functionalities apply from a power source which can be an 'on-board system, solar panel, wind turbine, generator, power supply'. Hydraulic sources are not included in this version. The discharge functions apply to all types of system requiring energy consumption from a storage battery. *Remark*: This Data Model can be used directly as a main entity to describe the device *Battery Storage* or as a sub - entity of the Data Model *DEVICE* using a reference by the *refDevice* attribute.**  

## List of properties  

- `address`:   - `alternateName`: Alternative Name given to the observation  - `application`: Target application of the Device regarding the storage. A combination of :  - `areaServed`: Zone of level higher to the attributes Location & Address to gather and cross information (ex district, etc)  - `batteryAssessmentMethods`:   - `batteryType`: Type of battery used. A unique value of :  - `brandName`: Brand Name  - `dataProvider`: Specifies the URL to information about the provider of this information  - `dateLastReported`: A timestamp which denotes the last time when the device successfully reported data. Date and time in an ISO8601 UTCformat.  - `description`:   - `documentation`: Technical Documentation (Installation / maintenance / used).  - `installationCondition`:   - `installationMode`:   - `location`:   - `manufacturerName`: Manufacturer Name.  - `modelName`:  Model Name.  - `name`:   - `owner`:   - `owners`: The owners of the Device. A list of [Text], [Person], [Organisation] or [URLs].  - `possibilityOfUse`: Possibility of use. A unique value of :  - `rechargeEnergySource`: Recharge Energy Source. A unique value of :  - `serialNumber`: Serial numbers.  - `source`:   - `typeEnergySource`: Type of Energy Source regarding RechargeEnergySource attribute. A combination of :  - `typeOfUse`: Accepted use regarding its positioning in an indoor / outdoor environment. A unique value of :    
Required properties  
- `batteryType`  - `dateLastReported`  - `id`  - `location`  - `rechargeEnergySource`  - `type`    
The charging functionalities apply from a power source which can be an 'on-board system, solar panel, wind turbine, generator, power supply'. Hydraulic sources are not included in this version. The discharge functions apply to all types of system requiring energy consumption from a storage battery. *Remark* This Data Model can be used directly as a main entity to describe the device *Battery Storage* or as a sub - entity of the Data Model *DEVICE* using a reference by the *refDevice* attribute.  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
StorageBatteryDevice:    
      required:    
        - id    
        - type    
        - location    
        - dateLastReported    
        - batteryType    
        - rechargeEnergySource    
      allOf:    
        - $ref: >-    
            https://smart-data-models.github.io/data-models/ngsi-ld.yaml#/Common    
      type: object    
      description: >-    
        The storage battery device data model is intended to describe the technical    
        characteristics of the battery and the charging and discharging conditions    
        of the energy. The charging functionalities apply from a power source which    
        can be an 'on-board system, solar panel, wind turbine, generator, power    
        supply'. Hydraulic sources are not included in this version. The discharge    
        functions apply to all types of system requiring energy consumption from a    
        storage battery. *Remark*: This Data Model can be used directly as a main    
        entity to describe the device *Battery Storage* or as a sub - entity of the    
        Data Model *DEVICE* using a reference by the *refDevice* attribute.    
      properties:    
        address:    
          $ref: 'https://smart-data-models.github.io/data-models/schema.org.yaml#/address'    
        alternateName:    
          x-ngsi:    
            type: Property    
            model: 'https://schema.org/Text'    
          type: string    
          description: 'Alternative Name given to the observation'    
        application:    
          x-ngsi:    
            type: Property    
          type: array    
          description: 'Target application of the Device regarding the storage. A combination of :'    
          items:    
            type: string    
            enum:    
              - electricMobility    
              - energyStorage    
              - emergencyStorage    
              - lighting    
              - industrialStorage    
              - houseHoldStorage    
              - robotics    
              - production    
              - other    
        areaServed:    
          x-ngsi:    
            type: Property    
            model: 'https://schema.org/Text'    
          type: string    
          description: 'Zone of level higher to the attributes Location & Address to gather and cross information (ex district, etc)'    
        batteryAssessmentMethods:    
          x-ngsi:    
            type: Property    
            model: 'https://schema.org/Text'    
          type: string    
          description: ''    
        batteryType:    
          x-ngsi:    
            type: Property    
            model: 'https://schema.org/Text'    
          type: string    
          description: 'Type of battery used. A unique value of :'    
        brandName:    
          x-ngsi:    
            type: Property    
            model: 'https://schema.org/Text'    
          type: string    
          description: 'Brand Name'    
        dataProvider:    
          x-ngsi:    
            type: Property    
            model: 'https://schema.org/Text'    
          type: string    
          description: 'Specifies the URL to information about the provider of this information'    
        dateLastReported:    
          x-ngsi:    
            type: Property    
            model: 'https://schema.org/DateTime'    
          type: string    
          description: 'A timestamp which denotes the last time when the device successfully reported data. Date and time in an ISO8601 UTCformat.'    
          format: date-time    
        description:    
          $ref: >-    
            https://smart-data-models.github.io/data-models/ngsi-ld.yaml#/description    
        documentation:    
          x-ngsi:    
            type: Property    
            model: 'https://schema.org/Text'    
          type: string    
          description: 'Technical Documentation (Installation / maintenance / used).'    
        installationCondition:    
          x-ngsi:    
            type: Property    
          type: array    
          description: ''    
          items:    
            type: string    
            enum:    
              - extremeHeat    
              - extremeCold    
              - extremeHumidity    
              - extremeClimate    
              - desert    
              - sand    
              - marine    
              - saline    
              - dust    
              - seismic    
              - other    
        installationMode:    
          x-ngsi:    
            type: Property    
            model: 'https://schema.org/Text'    
          type: string    
          description: ''    
        location:    
          $ref: >-    
            https://smart-data-models.github.io/data-models/ngsi-ld.yaml#/location    
        manufacturerName:    
          x-ngsi:    
            type: Property    
            model: 'https://schema.org/Text'    
          type: string    
          description: 'Manufacturer Name.'    
        modelName:    
          x-ngsi:    
            type: Property    
            model: 'https://schema.org/Text'    
          type: string    
          description: ' Model Name.'    
        name:    
          $ref: >-    
            https://smart-data-models.github.io/data-models/ngsi-ld.yaml#/name    
        owner:    
          $ref: >-    
            https://smart-data-models.github.io/data-models/fiware-terms.yaml#/owner    
        owners:    
          x-ngsi:    
            type: Property    
          type: array    
          description: 'The owners of the Device. A list of [Text], [Person], [Organisation] or [URLs].'    
          items:    
            type: string    
        possibilityOfUse:    
          x-ngsi:    
            type: Property    
            model: 'https://schema.org/Text'    
          type: string    
          description: 'Possibility of use. A unique value of :'    
        rechargeEnergySource:    
          x-ngsi:    
            type: Property    
            model: 'https://schema.org/Text'    
          type: string    
          description: 'Recharge Energy Source. A unique value of :'    
        serialNumber:    
          x-ngsi:    
            type: Property    
            model: 'https://schema.org/Text'    
          type: string    
          description: 'Serial numbers.'    
        source:    
          $ref: >-    
            https://smart-data-models.github.io/data-models/fiware-terms.yaml#/source    
        typeEnergySource:    
          x-ngsi:    
            type: Property    
          type: array    
          description: 'Type of Energy Source regarding RechargeEnergySource attribute. A combination of :'    
          items:    
            type: string    
            enum:    
              - network    
              - photovoltaic    
              - generator    
              - sea    
              - river    
              - dam    
              - fall    
              - waterTurbine    
              - wind    
              - other    
        typeOfUse:    
          x-ngsi:    
            type: Property    
            model: 'https://schema.org/Text'    
          type: string    
          description: 'Accepted use regarding its positioning in an indoor / outdoor environment. A unique value of :'    
```  
</details>    
## Example payloads    
#### StorageBatteryDevice NGSI V2 key-values Example    
Here is an example of a StorageBatteryDevice in JSON format as key-values. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:StorageBatteryDevice:StorageBatteryDevice:MNCA-SBD-T1-G0-027",  
  "type": "StorageBatteryDevice",  
  "name": "SBD-T1-G0-027",  
  "alternateName": "AirPort – global Observation",  
  "description": "Description of the Solar Storage Battery Device",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      43.66481,  
      7.196545  
    ]  
  },  
  "address": {  
    "addressCountry": "FR",  
    "addressLocality": "Nice",  
    "streetAddress": "Airport - Terminal 1 - Ground 0 - Local  27"  
  },  
  "areaServed": "Nice Aeroport",  
  "dateLastReported": "2020-03-17T08:45:00Z",  
  "brandName": "LG ELEC",  
  "modelName": "SBRESU10H",  
  "manufacturerName": "OSCPOWER",  
  "serialNumber": "BSSMA10267841259",  
  "application": [  
    "energyStorage",  
    "emergencyStorage"  
  ],  
  "typeOfUse": "mixed",  
  "installationMode": "ground",  
  "installationCondition": [  
    "extremeClimate"  
  ],  
  "possibilityOfUse": "stationary",  
  "batteryType": "Li-Ion",  
  "rechargeEnergySource": "electric",  
  "typeEnergySource": [  
    "network",  
    "photovoltaic"  
  ],  
  "documentation": "https://www.myStoragebattery.fr",  
  "owners": [  
    "Airport-Division Maintenance"  
  ],  
  "dimension": {  
    "width": 74.4,  
    "height": 90.7,  
    "depth": 20.6  
  },  
  "weight": 175,  
  "protectionIP": "55",  
  "protectionIK": 10,  
  "temperature": 25,  
  "operatingTemperature": {  
    "storage": [  
      -10,  
        50  
    ],  
    "charge": [  
      0,  
      40  
    ],  
    "discharge": [  
      -15,  
      40  
    ]  
  },  
  "nominalVoltage": 48,  
  "nominalAmpere": 20,  
  "nominalFrequency": 60,  
  "nominalCapacity": 63,  
  "storableEnergy": 3.025,  
  "usableEnergy": 3.012,  
  "operatingVoltage": {  
    "min": 38.5,  
    "max": 55.0  
  },  
  "operatingAmpere": {  
    "min": 1.0,  
    "max": 1.5  
  },  
  "operatingFrequency": {  
    "min": 57,  
    "max": 63  
  },  
  "massEnergyDensity": {  
    "min": 30,  
    "max": 50  
  },  
  "volEnergyDensity": {  
    "min": 75,  
    "max": 120  
  },  
  "maxOutputPower": 12.8,  
  "peakPower": 5.0,  
  "durationPeakPower": 10,  
  "communication": [  
    "CAN 2.0 B",  
    "RS485Inverter",  
    "RS485BMS",  
    "dryContactTerminal",  
    "maintenanceInterface"  
  ],  
  "operatingAltitude": {  
    "min": 0,  
    "max": 500  
  },  
  "averageLife": 15,  
  "lifeCycleNumber": {  
    "min": 600,  
    "max": 2400  
  },  
  "toolBMS": true,  
  "chargingModeAllowed": [  
    "normal"  
  ],  
  "overloadAccepted": true,  
  "overloadAcceptedTime": "00:00:03"  
  ,  
  "selfDischargeRate": 0.02,  
  "capacityCnnn": {  
    "C001": [  
      153.9,  
      1.6  
    ],  
    "C005": [  
      214.0,  
      1.75  
    ],  
    "C010": [  
      250.0,  
      1.8  
    ],  
    "C020": [  
      260.0,  
      1.8  
    ]  
  },  
  "roundTripEfficiency": 0.968,  
  "chargeDischargeReactivity": 0.4,  
  "chargePower": 123,  
  "chargeEfficiency": 0.98,  
  "maximumVoltageEOC": 48.6,  
  "dischargePower": 96.8,  
  "dischargeEfficiency": 0.95,  
  "minimumVoltageEOD": 47.3  
}  
```  
#### StorageBatteryDevice NGSI V2 normalized Example    
Here is an example of a StorageBatteryDevice in JSON format as normalized. This is compatible with NGSI V2 when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:StorageBatteryDevice:StorageBatteryDevice:MNCA-SBD-T1-G0-027",  
  "type": "StorageBatteryDevice",  
  "name": {  
    "type": "Property",  
    "value": "SBD-T1-G0-027"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "AirPort – global Observation"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Description of the Solar Storage Battery Device"  
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
  "dateLastReported": {  
    "type": "Property",  
    "value": {  
      "type": "DateTime",  
      "value": "2020-03-17T08:45:00Z"  
    }  
  },  
  "brandName": {  
    "type": "Property",  
    "value": "LG ELEC"  
  },  
  "modelName": {  
    "type": "Property",  
    "value": "SBRESU10H"  
  },  
  "manufacturerName": {  
    "type": "Property",  
    "value": "OSCPOWER"  
  },  
  "serialNumber": {  
    "type": "Property",  
    "value": "BSSMA10267841259"  
  },  
  "application": {  
    "type": "Property",  
    "value": [  
      "energyStorage",  
      "emergencyStorage"  
    ]  
  },  
  "typeOfUse": {  
    "type": "Property",  
    "value": "mixed"  
  },  
  "installationMode": {  
    "type": "Property",  
    "value": "ground"  
  },  
  "installationCondition": {  
    "type": "Property",  
    "value": [  
      "extremeClimate"  
    ]  
  },  
  "possibilityOfUse": {  
    "type": "Property",  
    "value": "stationary"  
  },  
  "batteryType": {  
    "type": "Property",  
    "value": "Li-Ion"  
  },  
  "rechargeEnergySource": {  
    "type": "Property",  
    "value": "electric"  
  },  
  "typeEnergySource": {  
    "type": "Property",  
    "value": [  
      "network",  
      "photovoltaic"  
    ]  
  },  
  "documentation": {  
    "type": "Property",  
    "value": "https://www.myStoragebattery.fr"  
  },  
  "owners": {  
    "type": "Property",  
    "value": [  
      "Airport-Division Maintenance"  
    ]  
  },  
  "dimension": {  
    "type": "Property",  
    "value": {  
      "width": 74.4,  
      "height": 90.7,  
      "depth": 20.6  
    }  
  },  
  "weight": {  
    "type": "Property",  
    "value": 175  
  },  
  "protectionIP": {  
    "type": "Property",  
    "value": "55"  
  },  
  "protectionIK": {  
    "type": "Property",  
    "value": 10  
  },  
  "temperature": {  
    "type": "Property",  
    "value": 25  
  },  
  "operatingTemperature": {  
    "type": "Property",  
    "value": {  
      "storage": [  
        -10,  
        50  
      ],  
      "charge": [  
        0,  
        40  
      ],  
      "discharge": [  
        -15,  
        40  
      ]  
    }  
  },  
  "nominalVoltage": {  
    "type": "Property",  
    "value": 48  
  },  
  "nominalAmpere": {  
    "type": "Property",  
    "value": 20  
  },  
  "nominalFrequency": {  
    "type": "Property",  
    "value": 60  
  },  
  "nominalCapacity": {  
    "type": "Property",  
    "value": 63  
  },  
  "storableEnergy": {  
    "type": "Property",  
    "value": 3.025  
  },  
  "usableEnergy": {  
    "type": "Property",  
    "value": 3.012  
  },  
  "operatingVoltage": {  
    "type": "Property",  
    "value": {  
      "min": 38.5,  
      "max": 55.0  
    }  
  },  
  "operatingAmpere": {  
    "type": "Property",  
    "value": {  
      "min": 1.0,  
      "max": 1.5  
    }  
  },  
  "operatingFrequency": {  
    "type": "Property",  
    "value": {  
      "min": 57,  
      "max": 63  
    }  
  },  
  "massEnergyDensity": {  
    "type": "Property",  
    "value": {  
      "min": 30,  
      "max": 50  
    }  
  },  
  "volEnergyDensity": {  
    "type": "Property",  
    "value": {  
      "min": 75,  
      "max": 120  
    }  
  },  
  "maxOutputPower": {  
    "type": "Property",  
    "value": 12.8  
  },  
  "peakPower": {  
    "type": "Property",  
    "value": 5.0  
  },  
  "durationPeakPower": {  
    "type": "Property",  
    "value": 10  
  },  
  "communication": {  
    "type": "Property",  
    "value": [  
      "CAN 2.0 B",  
      "RS485Inverter",  
      "RS485BMS",  
      "dryContactTerminal",  
      "maintenanceInterface"  
    ]  
  },  
  "operatingAltitude": {  
    "type": "Property",  
    "value": {  
      "min": 0,  
      "max": 500  
    }  
  },  
  "averageLife": {  
    "type": "Property",  
    "value": 15  
  },  
  "lifeCycleNumber": {  
    "type": "Property",  
    "value": {  
      "min": 600,  
      "max": 2400  
    }  
  },  
  "toolBMS": {  
    "type": "Property",  
    "value": true  
  },  
  "chargingModeAllowed": {  
    "type": "Property",  
    "value": [  
      "normal"  
    ]  
  },  
  "overloadAccepted": {  
    "type": "Property",  
    "value": true  
  },  
  "overloadAcceptedTime": {  
    "type": "Property",  
    "value": {  
      "type": "DateTime",  
      "value": "T00:00:03"  
    }  
  },  
  "selfDischargeRate": {  
    "type": "Property",  
    "value": 2  
  },  
  "capacityCnnn": {  
    "type": "Property",  
    "value": {  
      "C001": [  
        153.9,  
        1.60  
      ],  
      "C005": [  
        214.0,  
        1.75  
      ],  
      "C010": [  
        250.0,  
        1.80  
      ],  
      "C020": [  
        260.0,  
        1.80  
      ]  
    }  
  },  
  "roundTripEfficiency": {  
    "type": "Property",  
    "value": 96.8  
  },  
  "chargeDischargeReactivity": {  
    "type": "Property",  
    "value": 0.4  
  },  
  "chargePower": {  
    "type": "Property",  
    "value": 123  
  },  
  "chargeEfficiency": {  
    "type": "Property",  
    "value": 98  
  },  
  "maximumVoltageEOC": {  
    "type": "Property",  
    "value": 48.6  
  },  
  "dischargePower": {  
    "type": "Property",  
    "value": 96.8  
  },  
  "dischargeEfficiency": {  
    "type": "Property",  
    "value": 95  
  },  
  "minimumVoltageEOD": {  
    "type": "Property",  
    "value": 47.3  
  }  
}  
```  
#### StorageBatteryDevice NGSI-LD key-values Example    
Here is an example of a StorageBatteryDevice in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:StorageBatteryDevice:StorageBatteryDevice:MNCA-SBD-T1-G0-027",  
  "type": "StorageBatteryDevice",  
  "name": "SBD-T1-G0-027",  
  "alternateName": "AirPort â€“ global Observation",  
  "description": "Description of the Solar Storage Battery Device",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      43.66481,  
      7.196545  
    ]  
  },  
  "address": {  
    "addressCountry": "FR",  
    "addressLocality": "Nice",  
    "streetAddress": "Airport - Terminal 1 - Ground 0 - Local  27"  
  },  
  "areaServed": "Nice Aeroport",  
  "dateLastReported": "2020-03-17T08:45:00Z",  
  "brandName": "LG ELEC",  
  "modelName": "SBRESU10H",  
  "manufacturerName": "OSCPOWER",  
  "serialNumber": "BSSMA10267841259",  
  "application": [  
    "energyStorage",  
    "emergencyStorage"  
  ],  
  "typeOfUse": "mixed",  
  "installationMode": "ground",  
  "installationCondition": [  
    "extremeClimate"  
  ],  
  "possibilityOfUse": "stationary",  
  "batteryType": "Li-Ion",  
  "rechargeEnergySource": "electric",  
  "typeEnergySource": [  
    "network",  
    "photovoltaic"  
  ],  
  "documentation": "https://www.myStoragebattery.fr",  
  "owners": [  
    "Airport-Division Maintenance"  
  ],  
  "dimension": {  
    "width": 74.4,  
    "height": 90.7,  
    "depth": 20.6  
  },  
  "weight": 175,  
  "protectionIP": "55",  
  "protectionIK": 10,  
  "temperature": 25,  
  "operatingTemperature": {  
    "storage": [  
      -10,  
      50  
    ],  
    "charge": [  
      0,  
      40  
    ],  
    "discharge": [  
      -15,  
      40  
    ]  
  },  
  "nominalVoltage": 48,  
  "nominalAmpere": 20,  
  "nominalFrequency": 60,  
  "nominalCapacity": 63,  
  "storableEnergy": 3.025,  
  "usableEnergy": 3.012,  
  "operatingVoltage": {  
    "min": 38.5,  
    "max": 55.0  
  },  
  "operatingAmpere": {  
    "min": 1.0,  
    "max": 1.5  
  },  
  "operatingFrequency": {  
    "min": 57,  
    "max": 63  
  },  
  "massEnergyDensity": {  
    "min": 30,  
    "max": 50  
  },  
  "volEnergyDensity": {  
    "min": 75,  
    "max": 120  
  },  
  "maxOutputPower": 12.8,  
  "peakPower": 5.0,  
  "durationPeakPower": 10,  
  "communication": [  
    "CAN 2.0 B",  
    "RS485Inverter",  
    "RS485BMS",  
    "dryContactTerminal",  
    "maintenanceInterface"  
  ],  
  "operatingAltitude": {  
    "min": 0,  
    "max": 500  
  },  
  "averageLife": 15,  
  "lifeCycleNumber": {  
    "min": 600,  
    "max": 2400  
  },  
  "toolBMS": true,  
  "chargingModeAllowed": [  
    "normal"  
  ],  
  "overloadAccepted": true,  
  "overloadAcceptedTime": "00:00:03",  
  "selfDischargeRate": 0.02,  
  "capacityCnnn": {  
    "C001": [  
      153.9,  
      1.6  
    ],  
    "C005": [  
      214.0,  
      1.75  
    ],  
    "C010": [  
      250.0,  
      1.8  
    ],  
    "C020": [  
      260.0,  
      1.8  
    ]  
  },  
  "roundTripEfficiency": 0.968,  
  "chargeDischargeReactivity": 0.4,  
  "chargePower": 123,  
  "chargeEfficiency": 0.98,  
  "maximumVoltageEOC": 48.6,  
  "dischargePower": 96.8,  
  "dischargeEfficiency": 0.95,  
  "minimumVoltageEOD": 47.3,  
  "@context": [  
    "https://schema.lab.fiware.org/ld/context",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### StorageBatteryDevice NGSI-LD normalized Example    
Here is an example of a StorageBatteryDevice in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
	"id": "urn:ngsi-ld:StorageBatteryDevice:StorageBatteryDevice:MNCA-SBD-T1-G0-027",  
	"type": "StorageBatteryDevice",  
	"name": {  
		"type": "Property",  
		"value": "SBD-T1-G0-027"  
	},  
	"alternateName": {  
		"type": "Property",  
		"value": "AirPort â€“ global Observation"  
	},  
	"description": {  
		"type": "Property",  
		"value": "Description of the Solar Storage Battery Device"  
	},  
	"location": {  
		"type": "GeoProperty",  
		"value": {  
			"type": "Point",  
			"coordinates ": [43.664810, 7.196545]  
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
	"dateLastReported": {  
		"type": "Property",  
		"value": {  
			"type": "DateTime",  
			"value": "2020-03-17T08:45:00Z"  
		}  
	},  
	"brandName": {  
		"type": "Property",  
		"value": "LG ELEC"  
	},  
	"modelName": {  
		"type": "Property",  
		"value": "SBRESU10H"  
	},  
	"manufacturerName": {  
		"type": "Property",  
		"value": "OSCPOWER"  
	},  
	"serialNumber": {  
		"type": "Property",  
		"value": "BSSMA10267841259"  
	},  
	"application": {  
		"type": "Property",  
		"value": ["energyStorage", "emergencyStorage"]  
	},  
	"typeOfUse": {  
		"type": "Property",  
		"value": "mixed"  
	},  
	"installationMode": {  
		"type": "Property",  
		"value": "ground"  
	},  
	"installationCondition": {  
		"type": "Property",  
		"value": ["extremeClimate"]  
	},  
	"possibilityOfUse": {  
		"type": "Property",  
		"value": "stationary"  
	},  
	"batteryType": {  
		"type": "Property",  
		"value": "Li-Ion"  
	},  
	"rechargeEnergySource": {  
		"type": "Property",  
		"value": "electric"  
	},  
	"typeEnergySource": {  
		"type": "Property",  
		"value": ["network", "photovoltaic"]  
	},  
	"documentation": {  
		"type": "Property",  
		"value": "https://www.myStoragebattery.fr"  
	},  
	"owners": {  
		"type": "Property",  
		"value": ["Airport-Division Maintenance"]  
	},  
	"dimension": {  
		"type": "Property",  
		"value": {  
			"width": 74.4,  
			"height": 90.7,  
			"depth": 20.6  
		}  
	},  
	"weight": {  
		"type": "Property",  
		"value": 175  
	},  
	"protectionIP": {  
		"type": "Property",  
		"value": "55"  
	},  
	"protectionIK": {  
		"type": "Property",  
		"value": 10  
	},  
	"temperature": {  
		"type": "Property",  
		"value": 25  
	},  
	"operatingTemperature": {  
		"type": "Property",  
		"value": {  
			"storage": [-10, 50],  
			"charge": [0, 40],  
			"discharge": [-15, 40]  
		}  
	},  
	"nominalVoltage": {  
		"type": "Property",  
		"value": 48  
	},  
	"nominalAmpere": {  
		"type": "Property",  
		"value": 20  
	},  
	"nominalFrequency": {  
		"type": "Property",  
		"value": 60  
	},  
	"nominalCapacity": {  
		"type": "Property",  
		"value": 63  
	},  
	"storableEnergy": {  
		"type": "Property",  
		"value": 3.025  
	},  
	"usableEnergy": {  
		"type": "Property",  
		"value": 3.012  
	},  
	"operatingVoltage": {  
		"type": "Property",  
		"value": {  
			"min": 38.5,  
			"max": 55.0  
		}  
	},  
	"operatingAmpere": {  
		"type": "Property",  
		"value": {  
			"min": 1.0,  
			"max": 1.5  
		}  
	},  
	"operatingFrequency": {  
		"type": "Property",  
		"value": {  
			"min": 57,  
			"max": 63  
		}  
	},  
	"massEnergyDensity": {  
		"type": "Property",  
		"value": {  
			"min": 30,  
			"max": 50  
		}  
	},  
	"volEnergyDensity": {  
		"type": "Property",  
		"value": {  
			"min": 75,  
			"max": 120  
		}  
	},  
	"maxOutputPower": {  
		"type": "Property",  
		"value": 12.8  
	},  
	"peakPower": {  
		"type": "Property",  
		"value": 5.0  
	},  
	"durationPeakPower": {  
		"type": "Property",  
		"value": 10  
	},  
	"communication": {  
		"type": "Property",  
		"value": [  
			"CAN 2.0 B",  
			"RS485Inverter",  
			"RS485BMS",  
			"dryContactTerminal",  
			"maintenanceInterface"  
		]  
	},  
	"operatingAltitude": {  
		"type": "Property",  
		"value": {  
			"min": 0,  
			"max": 500  
		}  
	},  
	"averageLife": {  
		"type": "Property",  
		"value": 15  
	},  
	"lifeCycleNumber": {  
		"type": "Property",  
		"value": {  
			"min": 600,  
			"max": 2400  
		}  
	},  
	"toolBMS": {  
		"type": "Property",  
		"value": true  
	},  
	"chargingModeAllowed": {  
		"type": "Property",  
		"value": ["normal"]  
	},  
	"overloadAccepted": {  
		"type": "Property",  
		"value": true  
	},  
	"overloadAcceptedTime": {  
		"type": "Property",  
		"value": {  
			"type": "DateTime",  
			"value": "T00:00:03"  
		}  
	},  
	"selfDischargeRate": {  
		"type": "Property",  
		"value": 2  
	},  
	"capacityCnnn": {  
		"type": "Property",  
		"value": {  
			"C001": [153.9,1.60],  
			"C005": [214.0,1.75],  
			"C010": [250.0,1.80 ],  
			"C020": [260.0,1.80]  
		}  
	},  
	"roundTripEfficiency": {  
		"type": "Property",  
		"value": 96.8  
	},  
	"chargeDischargeReactivity": {  
		"type": "Property",  
		"value": 0.4  
	},  
	"chargePower": {  
		"type": "Property",  
		"value": 123  
	},  
	"chargeEfficiency": {  
		"type": "Property",  
		"value": 98  
	},  
	"maximumVoltageEOC": {  
		"type": "Property",  
		"value": 48.6  
	},  
	"dischargePower": {  
		"type": "Property",  
		"value": 96.8  
	},  
	"dischargeEfficiency": {  
		"type": "Property",  
		"value": 95  
	},  
	"minimumVoltageEOD": {  
		"type": "Property",  
		"value": 47.3  
	},  
	"@context": [  
		"https://schema.lab.fiware.org/ld/context",  
		"https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
	]  
}  
```  
