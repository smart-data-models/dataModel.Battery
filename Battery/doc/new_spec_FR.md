Entité : Batterie  
=================  
Cette spécification est une **version temporelle**. Elle est générée automatiquement à partir des propriétés documentées décrites dans le schema.json condensé dans le fichier `model.yaml`. Un fichier temporaire `nouveau_modèle.yaml` a été créé dans chaque modèle de données pour éviter d'avoir un impact sur les scripts existants. Ainsi, la spécification sera incomplète tant que le fichier schema.json n'est pas mis à jour au nouveau format (documentation des propriétés). Une fois mis à jour, le fichier `model.yaml` (`nouveau_model.yaml`) doit être mis à jour également (automatiquement) . Plus d'informations dans ce [lien](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). Tant qu'il s'agit d'un format provisoire, tout [feedback est le bienvenu dans ce formulaire](https://smartdatamodels.org/index.php/submit-an-issue-2/) en choisissant l'option "Feedback sur la nouvelle spécification".  
Description globale : **Représente une batterie physique avec ses spécifications matérielles**  

## Liste des biens  

- `acPowerInput`:   - `acPowerOutput`:   - `address`: L'adresse postale.  - `alternateName`: Un autre nom pour cet article  - `areaServed`: La zone géographique où un service ou un article offert est fourni.  - `autonomyTime`:   - `cycleLife`:   - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dcPowerInput`:   - `dcPowerOutput`:   - `description`: Une description de cet article  - `id`:   - `location`:   - `name`: Le nom de cet article.  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `rechargeTime`:   - `refDevice`: Définitions communes pour décrire les scemas de dispositifs et de modèles de dispositifs.  - `seeAlso`:   - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `status`:   - `type`: NGSI Type d'entité  ## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Battery:    
  description: 'Represent a physical battery with its hardware specifications'    
  properties:    
    acPowerInput:    
      type: number    
    acPowerOutput:    
      type: number    
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
    autonomyTime:    
      pattern: ^(-?)P(?=\d|T\d)(?:(\d+)Y)?(?:(\d+)M)?(?:(\d+)([DW]))?(?:T(?:(\d+)H)?(?:(\d+)M)?(?:(\d+(?:\.\d+)?)S)?)?$    
      type: string    
    cycleLife:    
      type: integer    
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
    dcPowerInput:    
      type: number    
    dcPowerOutput:    
      type: number    
    description:    
      description: 'A description of this item'    
      type: Property    
    id:    
      anyOf: &battery_-_properties_-_owner_-_items_-_anyof    
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
        anyOf: *battery_-_properties_-_owner_-_items_-_anyof    
      type: Property    
    rechargeTime:    
      pattern: ^(-?)P(?=\d|T\d)(?:(\d+)Y)?(?:(\d+)M)?(?:(\d+)([DW]))?(?:T(?:(\d+)H)?(?:(\d+)M)?(?:(\d+(?:\.\d+)?)S)?)?$    
      type: string    
    refDevice:    
      $id: https://smart-data-models.github.io/dataModel.Device/device-schema.json    
      $schema: "http://json-schema.org/schema#"    
      definitions:    
        CategoryType:    
          items: &battery_-_properties_-_refdevice_-_definitions_-_device-commons_-_category_-_items    
            enum:    
              - actuator    
              - beacon    
              - endgun    
              - HVAC    
              - implement    
              - irrSystem    
              - irrSection    
              - meter    
              - network    
              - multimedia    
              - sensor    
            type: string    
          type: array    
        ControlledPropertyType:    
          items: &battery_-_properties_-_refdevice_-_definitions_-_device-commons_-_controlledproperty_-_items    
            enum:    
              - temperature    
              - humidity    
              - light    
              - motion    
              - fillingLevel    
              - occupancy    
              - power    
              - pressure    
              - smoke    
              - energy    
              - airPollution    
              - noiseLevel    
              - weatherConditions    
              - precipitation    
              - windSpeed    
              - windDirection    
              - atmosphericPressure    
              - solarRadiation    
              - depth    
              - pH    
              - conductivity    
              - conductance    
              - tss    
              - tds    
              - turbidity    
              - salinity    
              - orp    
              - cdom    
              - waterPollution    
              - location    
              - speed    
              - heading    
              - weight    
              - waterConsumption    
              - gasComsumption    
              - electricityConsumption    
              - eatingActivity    
              - milking    
              - movementActivity    
              - soilMoisture    
            type: string    
          type: array    
        Device-Commons:    
          category:    
            items: *battery_-_properties_-_refdevice_-_definitions_-_device-commons_-_category_-_items    
            type: array    
          controlledProperty:    
            items: *battery_-_properties_-_refdevice_-_definitions_-_device-commons_-_controlledproperty_-_items    
            type: array    
          macAddress:    
            pattern: ^([[:xdigit:]]{2}[:.-]?){5}[[:xdigit:]]{2}$    
            type: string    
          supportedProtocol:    
            items: &battery_-_properties_-_refdevice_-_definitions_-_supportedprotocoltype_-_items    
              enum:    
                - 3g    
                - bluetooth    
                - 'bluetooth LE'    
                - cat-m    
                - coap    
                - ec-gsm-iot    
                - gprs    
                - http    
                - lwm2m    
                - lora    
                - lte-m    
                - mqtt    
                - nb-iot    
                - onem2m    
                - sigfox    
                - ul20    
                - websocket    
              type: string    
            type: array    
          type: object    
        MacAddressType:    
          pattern: ^([[:xdigit:]]{2}[:.-]?){5}[[:xdigit:]]{2}$    
          type: string    
        SupportedProtocolType:    
          items: *battery_-_properties_-_refdevice_-_definitions_-_supportedprotocoltype_-_items    
          type: array    
      description: 'Common defintions to describe Device and Device Model scemas.'    
      title: ' - Device  Commons schema'    
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
    status:    
      items:    
        enum:    
          - working    
          - outOfService    
          - withIncidence    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
    type:    
      description: 'NGSI Entity type'    
      enum:    
        - Battery    
      type: string    
  required:    
    - id    
    - type    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### Batterie NGSI V2 valeurs clés Exemple  
Voici un exemple d'une batterie au format JSON comme valeurs clés. Ce format est compatible avec NGSI V2 lorsqu'on utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "Battery:d95372df39",  
  "type": "Battery",  
  "dataProvider": "bike-in.com",  
  "refDevice": "Device:d95372df39",  
  "location": {  
    "type": "Point",  
    "coordinates": [-4.754444444, 41.640833333]  
  },  
  "status": ["working"],  
  "cicleLife": 20000,  
  "autonomyTime": "PT1H",  
  "rechargeTime":"PT6H",  
  "acPowerInput": 1.5,  
  "acPowerOutput": 0.5  
}  
```  
#### Batterie NGSI V2 normalisée Exemple  
Voici un exemple de batterie au format JSON normalisé. Il est compatible avec NGSI V2 lorsqu'il utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "Battery:santander:d95372df39",  
  "type": "Battery",  
  "source": {  
    "type": "string",  
    "value": "bike-in.com"  
  },  
  "dataProvider": {  
    "type": "string",  
    "value": "bike-in.com"  
  },  
  "refDevice": {  
    "type": "string",  
    "value": "Device:santander:d95372df39"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [-8.768460000000001, 42.60214472222222]  
    }  
  },  
  "status": {  
    "type":"array",  
    "value":["working"]  
  },  
  "cicleLife": {  
    "type": "integer",  
    "value": 20000  
  },  
  "autonomyTime": {  
    "type": "string",  
    "value": "PT1H"  
  },  
  "rechargeTime": {  
    "type": "string",  
    "value": "PT6H"  
  },  
  "acPowerInput": {  
    "type": "number",  
    "value": 1.5  
  },  
  "acPowerOutput": {  
    "type": "number",  
    "value": 0.5  
  }  
}  
```  
#### Batterie NGSI-LD valeurs clés Exemple  
Voici un exemple d'une batterie au format JSON-LD comme valeurs clés. Ce format est compatible avec le format NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:Battery:santander:d95372df39",  
  "type": "Battery",  
  "source": "bike-in.com",  
  "dataProvider": "bike-in.com",  
  "refDevice": "urn:ngsi-ld:Device:santander:d95372df39",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -4.754444444,  
      41.640833333  
    ]  
  },  
  "status": ["working"],  
  "cicleLife": 20000,  
  "autonomyTime": "PT1H",  
  "rechargeTime": "PT6H",  
  "acPowerInput": 1.5,  
  "acPowerOutput": 0.5,  
  "@context": ["https://smart-data-models.github.io/data-models/context.jsonld"]  
}  
```  
#### Batterie NGSI-LD normalisée Exemple  
Voici un exemple de batterie au format JSON-LD normalisé. Ce format est compatible avec le format NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:Battery:santander:d95372df39",  
  "type": "Battery",  
  "source": {  
    "type": "Property",  
    "value": "bike-in.com"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "bike-in.com"  
  },  
  "refDevice": {  
    "type": "Property",  
    "value": "urn:ngsi-ld:Device:santander:d95372df39"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
          -4.754444444,  
          41.640833333  
      ]  
    }  
  },  
  "status": {  
    "type": "Property",  
    "value": ["working"]  
  },  
  "cicleLife": {  
    "type": "Property",  
    "value": 20000  
  },  
  "autonomyTime": {  
    "type": "Property",  
    "value": "PT1H"  
  },  
  "rechargeTime": {  
    "type": "Property",  
    "value": "PT6H"  
  },  
  "acPowerInput": {  
    "type": "Property",  
    "value": 1.5  
  },  
  "acPowerOutput": {  
    "type": "Property",  
    "value": 0.5  
  },  
  "@context": [  
    "https://schema.lab.fiware.org/ld/context",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
