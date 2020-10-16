Battery:
  - required:
    - 
    - 
  - type: "object"
    - allOf:
      - $ref: "https://jason-fox.github.io/swagger-datamodel-test/common.yaml#/Common"
   - description: >
      ## Description. Pending translation just a template
        
      ## Data Model

      For a full description of the following attributes refer to GSMA
      [IoT Big Data Harmonised Data Model](https://github.com/GSMADeveloper/NGSI-LD-Entities)
      
  - properties:  
    - acPowerInput:
      - x-ngsi:
        - type: "Property"
        - model: ""
      - type: "number"
      - description: "pending" 
    - address:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/address"
      - $ref: "https://github.com/smart-data-models/data-models/blob/master/common-schema.md#/Address"
    - autonomyTime:
      - x-ngsi:
        - type: "Property"
        - model: "pending"
      - type: "string"
      - format: "integer"
      - description: >
        pending description. to include "pattern": "^(-?)P(?=\\d|T\\d)(?:(\\d+)Y)?(?:(\\d+)M)?(?:(\\d+)([DW]))?(?:T(?:(\\d+)H)?(?:(\\d+)M)?(?:(\\d+(?:\\.\\d+)?)S)?)?$"
    - cycleLife:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/URL"
      - type: "number"
      - format: "integer"
      - description: >
        pending description
    - dataProvider:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/URL"
      - type: "string"
      - format: "URL"
      - description: >
        Specifies the URL to information about the provider of this information
    - dcPowerInput:
      - x-ngsi:
        - type: "Property"
        - model: ""
      - type: "number"
      - description: "pending"
    - dcPowerOutput:
      - x-ngsi:
        - type: "Property"
        - model: ""
      - type: "number"
      - description: "pending"  
    - description:
      - x-ngsi:
        - type: "Property"
        - model: "https://uri.etsi.org/ngsi-ld/description"
      - $ref: 'https://jason-fox.github.io/swagger-datamodel-test/common.yaml#/Description'       
    - owner:
      - x-ngsi:
       - type: "Relationship"
       - model: "https://schema.org/URL"
      - type: "string"
      - format: "URL"
      - description: >
            pending description
    - rechargeTime:
      - x-ngsi:
        - type: "Property"
        - model: "pending"
      - type: "string"
      - format: ""
      - description: >
        pending description. to include "pattern": "^(-?)P(?=\\d|T\\d)(?:(\\d+)Y)?(?:(\\d+)M)?(?:(\\d+)([DW]))?(?:T(?:(\\d+)H)?(?:(\\d+)M)?(?:(\\d+(?:\\.\\d+)?)S)?)?$"

    - refDevice:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/URL"
      - type: "string"
      - format: "URL"
      - description:
    - source:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Text", "https://schema.org/URL"
      - type: "string"
      - description: >
            A sequence of characters giving the source of the entity data.
    -status:
      - x-ngsi:
        - type: "Property"
        - model: ""
      - type: ""
      - description: > 
        pending description
    - location:
      - $ref: "https://github.com/smart-data-models/data-models/blob/master/common-schema.md#/Address"
      
    
        
      
