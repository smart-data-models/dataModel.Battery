Entity: BatteryStatus  
=====================  
This specification is a **temporal version**. It is automatically generated from the  documented properties described in the schema.json condensed into the file `model.yaml`. A temporary `new_model.yaml` file has been created in every data model to avoid impacting into existing scripts. Thus, the specification will be incomplete as long as the schema.json is not updated to the new format (documenting properties). Once updated the `model.yaml` (`new_model.yaml`) needs to be updated as well (automatically) . Further info in this [link](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). As long as it is a provisional format any [feedback is welcomed in this form](https://smartdatamodels.org/index.php/submit-an-issue-2/) choosing option `Feedback on the new specification`  
Global description: **Represent a status for a physical battery.**  

## List of properties  

- `address`: The mailing address.  - `alternateName`: An alternative name for this item  - `areaServed`: The geographic area where a service or offered item is provided.  - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description`: A description of this item  - `id`:   - `location`:   - `name`: The name of this item.  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `seeAlso`:   - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `type`: NGSI Entity type  ## Data Model description of properties  
Sorted alphabetically  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
BatteryStatus:    
  description: 'Represent a status for a physical battery.'    
  properties:    
    address:    
      description: 'The mailing address.'    
      properties:    
        addressCountry:    
          type: string    
        addressLocality:    
          type: string    
        addressRegion:    
          type: string    
        areaServed:    
          type: string    
        postOfficeBoxNumber:    
          type: string    
        postalCode:    
          type: string    
        streetAddress:    
          type: string    
      type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided.'    
      type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    description:    
      description: 'A description of this item'    
      type: Property    
    id:    
      anyOf: &batterystatus_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
    location:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf:    
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
      title: 'GeoJSON Geometry'    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *batterystatus_-_properties_-_owner_-_items_-_anyof    
      type: Property    
    seeAlso:    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'NGSI Entity type'    
      enum:    
        - BatteryStatus    
      type: string    
  required:    
    - id    
    - type    
    - refBattery    
    - status    
    - statusPercent    
  type: object    
```  
</details>    
#### BatteryStatus NGSI V2 key-values Example    
Here is an example of a BatteryStatus in JSON format as key-values. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
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
#### BatteryStatus NGSI V2 normalized Example    
Here is an example of a BatteryStatus in JSON format as normalized. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
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
#### BatteryStatus NGSI-LD key-values Example    
Here is an example of a BatteryStatus in JSON-LD format as key-values. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:BatteryStatus:santander:energy:d95372df39",  
  "type": "BatteryStatus",  
  "source": {  
    "type": "Property",  
    "value": "bike-in.com"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "bike-in.com"  
  },  
  "dateObserved": "2019-09-23T15:59:09.224Z",  
  "refBattery": "urn:ngsi-ld:Battery:santander:d95372df39",  
  "statusPercent": 0.98,  
  "acPowerInput": 0,  
  "acPowerOutput": 0.01,  
  "@context": ["https://smart-data-models.github.io/data-models/context.jsonld"]  
}  
```  
#### BatteryStatus NGSI-LD normalized Example    
Here is an example of a BatteryStatus in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:BatteryStatus:santander:energy:bs-ac-d95372df39",  
  "type": "BatteryStatus",  
  "dataProvider": {  
    "type":"Property",  
    "value":"bike-in.com"  
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
    "value": 0.90  
  },  
  "acPowerInput": {  
    "type": "Property",  
    "value": 0.01  
  },  
  "acPowerOutput": {  
    "type": "Property",  
    "value": 0.0  
  },  
  "@context": [  
    "https://schema.lab.fiware.org/ld/context",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
