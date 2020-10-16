BatteryStatus:
  - required:
    -  type
  - type: "object"
    - allOf:
      - $ref: "https://raw.githubusercontent.com/smart-data-models/data-models/master/ngsi-ld.yaml#/Common"
   - description: >
      ## Description
        
      ## Data Model

      For a full description of the following attributes refer to GSMA
      [IoT Big Data Harmonised Data Model](https://github.com/GSMADeveloper/NGSI-LD-Entities)
      
  - properties:
    - acPowerInput:
      - x-ngsi:
        - type: "Property"
      - type: "number"
      - description: >
        pending
    - acPowerOutput:
      - x-ngsi:
        - type: "Property"
      - type: "number"
      - description: >
        pending
    - address:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/address"
      - $ref: "https://github.com/smart-data-models/data-models/blob/master/common-schema.md#/Address"
    - dcPowerInput:
      - x-ngsi:
        - type: "Property"
      - type: "number"
      - description: >
        pending
    - dcPowerOutput:
      - x-ngsi:
        - type: "Property"
      - type: "number"
      - description: >
        pending    
    - dataProvider:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/URL"
      - type: "string"
      - format: "URL"
      - description: >
        Specifies the URL to information about the provider of this information  
    - description:
      - x-ngsi:
        - type: "Property"
        - model: "https://uri.etsi.org/ngsi-ld/description"
      - $ref: 'https://raw.githubusercontent.com/smart-data-models/data-models/master/ngsi-ld.yaml#/description'       
    - floorsAboveGround:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Integer"
      - type: "integer"
      - format: "int32"
      - description: >
            Number of floors above ground within the building
    - location:
      - $ref: "https://github.com/smart-data-models/data-models/blob/master/common-schema.md#/Address"
    - owner:
      - x-ngsi:
        - type: "Relationship"
        - model: "https://schema.org/URL"
      - type: "string"
      - format: "URL"
      - description: >
            The owner of this building
    - refBattery:
      - x-ngsi:
        - type: "Relationship"
        - model: "https://schema.org/URL"
      - type: "string"
      - format: "URL"
      - description: >
        pending  
    - refMap:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/URL"
      - type: "string"
      - format: "URL"
      - description: >
            The URL holding a map of the building       
    - source:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Text", "https://schema.org/URL"
      - type: "string"
      - description: >
            A sequence of characters giving the source of the entity data.
    - statusPercent:
      - x-ngsi:
        - type: "Property"
      - type: "number"
      - description: >
        pending  

