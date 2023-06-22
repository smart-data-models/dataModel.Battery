<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: BatteryStatus  
======================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Battery/blob/master/BatteryStatus/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Status für eine physische Batterie darstellen.**  
Version: 0.0.3  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.  
- `acPowerInput[number]`: Eigenschaft. Modell:'http://schema.org/Number'. Numerischer Wert in Volt für die Wechselstromladung. Einheiten:'volts'  . Model: [http://schema.org/Number](http://schema.org/Number)- `acPowerOutput[number]`: Eigenschaft. Modell:'http://schema.org/Number'. Numerischer Wert in Volt für den alternativen Ausgang. Einheiten:'volts'  . Model: [http://schema.org/Number](http://schema.org/Number)- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated[string]`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified[string]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `dcPowerInput[number]`: Eigenschaft. Modell:'http://schema.org/Number'. Numerischer Wert in Volt für die Dauerstromladung. Einheiten:'Volt'.  . Model: [http://schema.org/Number](http://schema.org/Number)- `dcPowerOutput[number]`: Eigenschaft. Modell:'http://schema.org/Number'. Numerischer Wert in Volt für die Dauerstromladung. Einheiten:'Volt'.  . Model: [http://schema.org/Number](http://schema.org/Number)- `description[string]`: Eine Beschreibung dieses Artikels  - `id[*]`: Eindeutiger Bezeichner der Entität  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name[string]`: Der Name dieses Artikels.  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `refBattery[*]`: Verwandtschaft. Modell:'http://schema.org/URL'. Verweis auf die Entität Batterie  . Model: [http://schema.org/URL](http://schema.org/URL)- `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Es wird empfohlen, den voll qualifizierten Domänennamen des Quellanbieters oder die URL des Quellobjekts zu verwenden.  - `statusPercent[number]`: Eigenschaft. Modell:'http://schema.org/Number'. Prozentualer Anteil der für die Batterie verfügbaren Ladung  . Model: [http://schema.org/Number](http://schema.org/Number)- `type[string]`: Eigenschaft. NGSI-Entitätstyp. Es muss BatteryStatus sein  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- `id`  - `refBattery`  - `statusPercent`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
BatteryStatus:    
  description: Represent a status for a physical battery.    
  properties:    
    acPowerInput:    
      description: 'Property. Model:''http://schema.org/Number''. Numeric value in volts for the alternate current charge. Units:''volts'''    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: volts    
    acPowerOutput:    
      description: 'Property. Model:''http://schema.org/Number''. Numeric value in volts for the alternate output. Units:''volts'''    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: volts    
    address:    
      description: The mailing address    
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
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government.'    
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
        streetNr:    
          description: Number identifying a specific property on a public street.    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity.    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dcPowerInput:    
      description: 'Property. Model:''http://schema.org/Number''. Numeric value in volts for the continuous current charge. Units:''volts'''    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: volts    
    dcPowerOutput:    
      description: 'Property. Model:''http://schema.org/Number''. Numeric value in volts for the continuous current charge. Units:''volts'''    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: volts    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &batterystatus_-_properties_-_owner_-_items_-_anyof    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: GeoProperty. Geojson reference to the item. Point    
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
          title: GeoJSON Point    
          type: object    
        - description: GeoProperty. Geojson reference to the item. LineString    
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
          title: GeoJSON LineString    
          type: object    
        - description: GeoProperty. Geojson reference to the item. Polygon    
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
          title: GeoJSON Polygon    
          type: object    
        - description: GeoProperty. Geojson reference to the item. MultiPoint    
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
          title: GeoJSON MultiPoint    
          type: object    
        - description: GeoProperty. Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiLineString    
          type: object    
        - description: GeoProperty. Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiPolygon    
          type: object    
      x-ngsi:    
        type: GeoProperty    
    name:    
      description: The name of this item.    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *batterystatus_-_properties_-_owner_-_items_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Property    
    refBattery:    
      description: 'Relationship. Model:''http://schema.org/URL''. Reference to the battery entity'    
      oneOf:    
        - format: uri    
          type: string    
        - anyOf: *batterystatus_-_properties_-_owner_-_items_-_anyof    
          description: Property. Unique identifier of the entity    
      x-ngsi:    
        model: http://schema.org/URL    
        type: Relationship    
    seeAlso:    
      description: list of uri pointing to additional resources about the item    
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
    statusPercent:    
      description: 'Property. Model:''http://schema.org/Number''. Percentage of charge available for the battery'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    type:    
      description: Property. NGSI Entity type. It has to be BatteryStatus    
      enum:    
        - BatteryStatus    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - refBattery    
    - statusPercent    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Battery/blob/master/BatteryStatus/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Battery/BatteryStatus/schema.json    
  x-model-tags: ""    
  x-version: 0.0.3    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
#### BatteryStatus NGSI-v2 Schlüsselwerte Beispiel  
Hier ist ein Beispiel für einen BatteryStatus im JSON-LD-Format als Key-Values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und gibt die Kontextdaten einer einzelnen Entität zurück.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "BatteryStatus:santander:energy:d95372df39",  
  "type": "BatteryStatus",  
  "dataProvider": "bike-in.com",  
  "dateObserved": "2019-09-23T15:59:09.224Z",  
  "refBattery": "Battery:santander:energy:bac-d95372df39",  
  "statusPercent": 0.97,  
  "acPowerInput": 0,  
  "acPowerOutput": 0.01  
}  
```  
</details>  
#### BatteryStatus NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen BatteryStatus im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "BatteryStatus:santander:energy:d95372df39",  
  "type": "BatteryStatus",  
  "dataProvider": {  
    "type":"string",  
    "value":"bike-in.com"  
  },  
  "dateObserved": {  
    "type": "string",  
    "value": "2019-09-23T15:59:09.224Z"  
  },  
  "refBattery": {  
    "type": "string",  
    "value": "Battery:santander:energy:d95372df39"  
  },  
  "statusPercent": {  
    "type": "integer",  
    "value": 0.90  
  },  
  "acPowerInput": {  
    "type": "number",  
    "value": 0.01  
  },  
  "acPowerOutput": {  
    "type": "number",  
    "value": 0.02  
  }  
}  
```  
</details>  
#### Batteriestatus NGSI-LD-Schlüsselwerte Beispiel  
Hier ist ein Beispiel für einen BatteryStatus im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:BatteryStatus:santander:energy:d95372df39",  
    "type": "BatteryStatus",  
    "acPowerInput": 0,  
    "acPowerOutput": 0.01,  
    "dataProvider": {  
        "type": "Property",  
        "value": "bike-in.com"  
    },  
    "dateObserved": "2019-09-23T15:59:09.224Z",  
    "refBattery": "urn:ngsi-ld:Battery:santander:d95372df39",  
    "source": {  
        "type": "Property",  
        "value": "bike-in.com"  
    },  
    "statusPercent": 0.98,  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Battery/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### Batteriestatus NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für einen BatteryStatus im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:BatteryStatus:santander:energy:bs-ac-d95372df39",  
    "type": "BatteryStatus",  
    "acPowerInput": {  
        "type": "Property",  
        "value": 0.01  
    },  
    "acPowerOutput": {  
        "type": "Property",  
        "value": 0.0  
    },  
    "dataProvider": {  
        "type": "Property",  
        "value": "bike-in.com"  
    },  
    "dateObserved": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2019-09-23T15:59:09.224Z"  
        }  
    },  
    "refBattery": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Battery:santander:energy:ac-d95372df39"  
    },  
    "statusPercent": {  
        "type": "Property",  
        "value": 0.9  
    },  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Battery/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
