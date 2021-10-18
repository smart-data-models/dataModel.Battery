Entidad: AlmacenamientoMedida  
=============================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Battery/blob/master/StorageBatteryMeasurement/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descripción global: **El Modelo de Datos Observados de la Batería de Almacenamiento está destinado a medir la capacidad de energía restante en una batería, que puede ser redistribuida en forma de energía eléctrica. Estas funciones se aplican desde una fuente que depende del tipo de batería (referencia al atributo "batteryType" del modelo de datos `StorageBatteryDevice`).**  
versión: 0.0.2  

## Lista de propiedades  

- `activePower`: Potencia activa, donde 'phi' es el desplazamiento de fase de la corriente en comparación con la tensión. El código de la unidad (texto) se indica utilizando los [Códigos comunes del UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Por ejemplo, **KWT** representa el kilovatio  - `address`: La dirección postal  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `batteryAssessmentMethods`: Métodos de evaluación y cálculo para las mediciones que evalúan el estado de la batería. Enum:'amperios-hora, prueba de descarga, densidad del electrolito, impedancia de alta frecuencia, impedancia de baja frecuencia, modelo matemático, tensión de funcionamiento con circuito cerrado, tensión de reposo con circuito abierto'.  - `batteryLevel`: Nivel de batería del dispositivo. Un valor único de los siguientes 0.0=batería vacía, 1.0=batería llena, -1.0=Transitoriamente no determinado.  - `batteryStatus`: Estado de la batería durante la medición (dando o no energía). Enum:'consumiendoEnergía, dandoEnergía, en espera'  - `current`: Actual. El código de la unidad (texto) se indica utilizando los [Códigos comunes del UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Por ejemplo, **AMP** representa el amperio.  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateEnergyMeteringStarted`: La fecha de inicio de la medición de energía en formato ISO8601 UTC  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `dateObservedFrom`: Período de observación: Fecha y hora de inicio en un formato ISO8601 UTC. El atributo puede utilizarse además del atributo "dateObserved" cuando corresponde a un intervalo de tiempo que debe destacarse.  - `dateObservedTo`: Período de observación: Fecha y hora de finalización en un formato ISO8601 UTC. El atributo puede utilizarse además del atributo "dateObserved" cuando corresponde a un intervalo de tiempo que debe destacarse.  - `deepOfDischarge`: La profundidad de descarga (código DoD) expresada en % es la relación entre la capacidad ya descargada y la capacidad nominal del acumulador. Es decir, la energía consumida en el acumulador. Regla [DOD] = 100 % - [SOC]. El código de la unidad (texto) se da utilizando los [Códigos comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Por ejemplo, **P1** representa el Porcentaje  - `description`: Una descripción de este artículo  - `id`: Identificador único de la entidad  - `inverterStatus`: Estado del inversor. Una combinación de valores. Enum:'00-Onsector, 01-Fallo de alimentación/en batería, 02-Pérdida de comunicación, 03-Avería de batería, 04-Apagado del sistema, 05-Descenso, 06-Sobretensión, 07-Caída de tensión, 08-Aumento de tensión, 09-Ruido de línea, 10-Variación de frecuencia, 11-Distorsión de transitorios, 12-Distorsión armónica'  - `location`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `name`: El nombre de este artículo.  - `openCircuitVoltage`: La tensión en circuito abierto (código OCV) expresada en voltios es la diferencia de potencial eléctrico entre dos terminales de un dispositivo cuando está desconectado de cualquier circuito. No hay ninguna carga externa conectada y no fluye ninguna corriente eléctrica externa entre los terminales. El código de la unidad (texto) se da utilizando los [Códigos comunes del UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Por ejemplo, **VLT** representa Volt  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `reactivePower`: Potencia reactiva utilizada por los circuitos. El código de la unidad (texto) se da utilizando los [Códigos comunes del UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Por ejemplo, **K5** representa el kilovoltio-amperio-reactivo  - `refPointOfInterest`: Referencia a un [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) vinculado con el Repositorio.  - `refStorageBatteryDevice`: Referencia a un [Dispositivo de Batería de Almacenamiento](https://github.com/FIWARE/data-models/blob/master/specs/Energy/StorageBatteryDevice/doc/spec.md) que capturó esta observación, si se utiliza la entidad.  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `stateOfCharge`: El Estado de Carga (Código SoC) expresado en % se define como la relación entre la capacidad restante y la actual. La capacidad actual es la capacidad máxima que puede extraerse de la batería totalmente cargada en condiciones específicas de descarga. Regla [SOC] + [DOD] = 100 %. El código de la unidad (texto) se da utilizando los [Códigos comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Por ejemplo, **P1** representa el Porcentaje  - `stateOfHealth`: El estado de salud (código SoH) expresado en % se define como la relación entre la cantidad máxima de carga que puede proporcionar una batería totalmente cargada en su régimen de descarga nominal, y su capacidad nominal. El código de la unidad (texto) se da utilizando los [Códigos comunes del UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Por ejemplo, **P1** representa el Porcentaje  - `temperature`: Temperatura principal registrada en el momento de la observación comparada con la temperatura nominal de referencia del dispositivo. El código de la unidad (texto) se indica utilizando los [Códigos comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Por ejemplo, **CEL** representa el grado Celsius  - `type`: Tipo de entidad NGSI. Tiene que ser StorageBatteryMeasurement    
Propiedades requeridas  
- `dateObserved`  - `id`  - `location`  - `stateOfCharge`  - `type`  ## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
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
        - const: -1    
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
  version: 0.0.2    
```  
</details>    
## Ejemplo de carga útil  
#### StorageBatteryMeasurement NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de una StorageBatteryMeasurement en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### AlmacenamientoMedición de la batería NGSI-v2 normalizado Ejemplo  
Este es un ejemplo de una StorageBatteryMeasurement en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
#### StorageBatteryMeasurement NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de una StorageBatteryMeasurement en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### AlmacenamientoMedición NGSI-LD normalizado Ejemplo  
Este es un ejemplo de una StorageBatteryMeasurement en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
