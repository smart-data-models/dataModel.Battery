Entität: StorageBatteryMeasurement  
==================================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Battery/blob/master/StorageBatteryMeasurement/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Storage Battery Observed Data Model dient der Messung der verbleibenden Energiekapazität in einer Batterie, die in Form von elektrischer Energie umverteilt werden kann. Diese Funktionen gelten aus einer Quelle, die vom Typ der Batterie abhängt (Verweis auf das Attribut 'batteryType' des Datenmodells `StorageBatteryDevice`).**  

## Liste der Eigenschaften  

- `activePower`: Wirkleistung, wobei 'phi' die Phasenverschiebung des Stroms im Vergleich zur Spannung ist. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **KWT** für Kilowatt  - `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `batteryAssessmentMethods`: Bewertungs- und Berechnungsmethoden für Messungen zur Beurteilung des Batteriezustandes. Enum:'ampereHourMetry, dischargeTest, electrolyteDensity, highFrequencyImpedance, lowFrequencyImpedance, mathematicalModel, operatingVoltageWithClosedCircuit, quiescentVoltageWithOpenCircuit'  - `batteryLevel`: Der Batteriestand des Geräts. Ein eindeutiger Wert des folgenden Wertes 0.0=Batterie leer, 1.0=Batterie voll, -1.0=Transiently not determined.  - `batteryStatus`: Status der Batterie während der Messung (Energie gebend oder nicht). Enum:'consumingEnergy, givingEnergy, standby'  - `current`: Aktuell. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **AMP** für Ampere.  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateEnergyMeteringStarted`: Das Startdatum für die Energiemessung in einem ISO8601 UTC-Format  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `dateObservedFrom`: Beobachtungszeitraum: Startdatum und -uhrzeit in einem ISO8601 UTC-Format. Das Attribut kann zusätzlich zum Attribut "dateObserved" verwendet werden, wenn es einem Zeitintervall entspricht, das hervorgehoben werden soll.  - `dateObservedTo`: Beobachtungszeitraum: Enddatum und -uhrzeit in einem ISO8601 UTC-Format. Das Attribut kann zusätzlich zum Attribut "dateObserved" verwendet werden, wenn es einem Zeitintervall entspricht, das hervorgehoben werden soll.  - `deepOfDischarge`: Die Entladetiefe (Code DoD), ausgedrückt in %, ist das Verhältnis zwischen der bereits entladenen Kapazität und der Nennkapazität des Akkus. Das heißt, die im Akku verbrauchte Energie. Regel [DOD] = 100 % - [SOC]. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel, **P1** steht für Prozent  - `description`: Eine Beschreibung dieses Artikels  - `id`: Eindeutiger Bezeichner der Entität  - `inverterStatus`: Status des Wechselrichters. Eine Kombination von Werten. Enum:'00-Onsector, 01-PowerFailure/OnBattery, 02-LossCommunication, 03-BatteryFault, 04-SystemShutDown, 05-TensionDip, 06-OverVoltage, 07-VoltageDrop, 08-VoltageIncrease, 09-LineNoise, 10-FrequencyVariation, 11-TransientDistortion, 12-HarmonicDistortion'  - `location`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name`: Der Name dieses Elements.  - `openCircuitVoltage`: Die Leerlaufspannung (Code OCV), ausgedrückt in Volt, ist die Differenz des elektrischen Potenzials zwischen zwei Klemmen eines Geräts, wenn es von einem Stromkreis getrennt ist. Es ist keine externe Last angeschlossen und es fließt kein externer elektrischer Strom zwischen den Klemmen. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **VLT** für Volt  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `reactivePower`: Blindleistung, die von Stromkreisen verwendet wird. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **K5** für Kilovolt-Ampere-Blindleistung  - `refPointOfInterest`: Verweis auf einen [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md), der mit dem Repository verknüpft ist.  - `refStorageBatteryDevice`: Verweis auf ein [Speicher-Batterie-Gerät](https://github.com/FIWARE/data-models/blob/master/specs/Energy/StorageBatteryDevice/doc/spec.md), das diese Beobachtung erfasst hat, falls die Entität verwendet wird.  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `stateOfCharge`: Der Ladezustand (Code SoC), ausgedrückt in %, ist definiert als das Verhältnis zwischen der verbleibenden und der aktuellen Kapazität. Die aktuelle Kapazität ist die maximale Kapazität, die der vollgeladenen Batterie unter bestimmten Entladebedingungen entnommen werden kann. Es gilt die Regel [SOC] + [DOD] = 100 %. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **P1** für Prozent  - `stateOfHealth`: Der Gesundheitszustand (Code SoH), ausgedrückt in %, ist definiert als das Verhältnis zwischen der maximalen Ladungsmenge, die eine vollständig geladene Batterie bei ihrer Nennentladung liefern kann, und ihrer Nennkapazität. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **P1** für Prozent  - `temperature`:  Haupttemperatur, die zum Zeitpunkt der Beobachtung aufgezeichnet wurde, verglichen mit der nominalen Referenztemperatur des Geräts. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **CEL** für Grad Celsius  - `type`: NGSI-Entitätstyp. Es muss StorageBatteryMeasurement sein    
Erforderliche Eigenschaften  
- `dateObserved`  - `id`  - `location`  - `stateOfCharge`  - `type`  ## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
StorageBatteryMeasurement:    
  description: 'Storage Battery Observed Data Model is intended to measure the remaining energy capacity in a battery, which can be redistributed in the form of electrical energy. These functions apply from a source which depends on the type of battery (reference to the attribute ''batteryType'' of the Data Model `StorageBatteryDevice`).'    
  properties:    
    activePower:    
      description: 'Active Power, where ''phi'' is the phase shift of the current compared to the voltage. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **KWT** represents Kilowatt'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
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
      type: Property    
      x-ngsi:    
        model: https://schema.org/address    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
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
      type: Property    
    batteryLevel:    
      description: 'Device''s battery level. A unique value of the following value 0.0=battery empty, 1.0=Battery full, -1.0=Transiently not determined.'    
      oneOf:    
        - maximum: 1    
          minimum: 0    
          type: number    
        - const: -1    
          type: number    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    batteryStatus:    
      description: 'Status of the battery during the measurement( giving or not energy). Enum:''consumingEnergy, givingEnergy, standby'''    
      enum:    
        - consumingEnergy    
        - givingEnergy    
        - standby    
      type: Property    
    current:    
      description: 'Current. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **AMP** represents Ampere. '    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: Ampere    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateEnergyMeteringStarted:    
      description: 'The starting date for metering energy in an ISO8601 UTC format'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime.    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateObservedFrom:    
      description: 'Observation period: Start date and time in an ISO8601 UTC format. The attribute can be used in addition to the ''dateObserved'' attribute when it corresponds to a time interval to be highlighted.'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    dateObservedTo:    
      description: 'Observation period: End date and time in an ISO8601 UTC format. The attribute can be used in addition to the ''dateObserved'' attribute when it corresponds to a time interval to be highlighted.'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    deepOfDischarge:    
      description: 'The Deep of Discharge (Code DoD) expressed in % is the ratio between the capacity already discharged and the nominal capacity of the accumulator. That is to say the energy consumed in the battery. Rule  [DOD] = 100 % - [SOC]. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **P1** represents Percent'    
      maximum: 1    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number.    
    description:    
      description: 'A description of this item'    
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
      type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: Property    
    openCircuitVoltage:    
      description: 'The Open Circuit Voltage (Code OCV) expressed in Volt is the difference of electrical potential between two terminals of a device when disconnected from any circuit. There is no external load connected and No external electric current flows between the terminals. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **VLT** represents Volt'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: Volt.    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *storagebatterymeasurement_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    reactivePower:    
      description: 'Reactive Power used by circuits. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **K5** represents kilovolt-ampere-reactive'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
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
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    stateOfCharge:    
      description: 'The State of Charge (Code SoC) expressed in % is defined as the ratio between the remaining and the current capacities. The current capacity is the maximum capacity that can be withdrawn from the fully charged battery under specific discharge conditions. Rule [SOC] + [DOD] = 100 %. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **P1** represents Percent'    
      maximum: 1    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number.    
    stateOfHealth:    
      description: 'The State of Health  (Code SoH) expressed in % is defined as the ratio between the maximum amount of charge that a fully charged battery can provide under its nominal discharge regime, and its nominal capacity. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **P1** represents Percent'    
      maximum: 1    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number.    
    temperature:    
      description: ' Main Temperature recorded at the time of Observation compared to the  nominal reference temperature of the device. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **CEL** represents Degree Celsius'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'celsius degrees .'    
    type:    
      description: 'NGSI Entity type. It has to be StorageBatteryMeasurement'    
      enum:    
        - StorageBatteryMeasurement    
      type: Property    
  required:    
    - id    
    - type    
    - location    
    - dateObserved    
    - stateOfCharge    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
#### SpeicherBatterieMessung NGSI-v2-Schlüsselwerte Beispiel  
Hier ist ein Beispiel für ein StorageBatteryMeasurement im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
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
#### SpeicherBatterieMessung NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für ein StorageBatteryMeasurement im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
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
#### SpeicherBatterieMessung NGSI-LD-Schlüsselwerte Beispiel  
Hier ist ein Beispiel für ein StorageBatteryMeasurement im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:StorageBatteryMeasurement:StorageBatteryMeasurement:MNCA-SBM-T1-G0-027",  
  "type": "StorageBatteryMeasurement",  
  "name": "SBM-T1-G0-027",  
  "alternateName": "AirPort â€“ global Observation",  
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
  ],  
  "@context": [  
    "https://schema.lab.fiware.org/ld/context",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### SpeicherBatterieMessung NGSI-LD normiert Beispiel  
Hier ist ein Beispiel für eine StorageBatteryMeasurement im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
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
    "value": "AirPort â€“ global Observation"  
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
      "@type": "DateTime",  
      "@value": "2020-03-17T08:45:00Z"  
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
  "deepOfDischarge": {  
    "type": "Property",  
    "value": 0.286  
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
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
