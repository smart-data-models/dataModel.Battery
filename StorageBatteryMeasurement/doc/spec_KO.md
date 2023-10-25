<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: StorageBatteryMeasurement  
==============================<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.Battery/blob/master/StorageBatteryMeasurement/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **저장 배터리 관찰 데이터 모델은 전기 에너지의 형태로 재분배할 수 있는 배터리의 남은 에너지 용량을 측정하기 위한 것입니다. 이 함수는 배터리 유형에 따라 달라지는 소스에서 적용됩니다(데이터 모델 `StorageBatteryDevice`의 'batteryType' 속성 참조).**  
버전: 0.0.3  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `activePower[number]`: 유효 전력, 여기서 '피'는 전압과 비교한 전류의 위상 편이입니다. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 지정합니다. 예를 들어 **KWT**는 킬로와트를 나타냅니다.  . Model: [https://schema.org/Number](https://schema.org/Number)- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.    
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호    
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `batteryAssessmentMethods[string]`: 배터리 상태를 평가하는 측정값에 대한 평가 및 계산 방법입니다. Enum:'ampereHourMetry, dischargeTest, electrolyteDensity, highFrequencyImpedance, lowFrequencyImpedance, mathematicalModel, operatingVoltageWithClosedCircuit, quiescentVoltageWithOpenCircuit'  - `batteryLevel[*]`: 디바이스의 배터리 잔량. 다음 값의 고유 값 0.0=배터리 비어 있음, 1.0=배터리 가득 찼음, -1.0=일시적으로 결정되지 않음  . Model: [https://schema.org/Number](https://schema.org/Number)- `batteryStatus[string]`: 측정 중 배터리 상태(에너지 제공 또는 미제공). Enum:'소비 에너지, 제공 에너지, 대기'  - `current[number]`: 현재. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 지정합니다. 예를 들어 **AMP**는 암페어를 나타냅니다.  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateEnergyMeteringStarted[date-time]`: ISO8601 UTC 형식의 에너지 계량 시작 날짜  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateObservedFrom[date-time]`: 관찰 기간: ISO8601 UTC 형식의 시작 날짜 및 시간입니다. 이 속성은 강조 표시할 시간 간격에 해당하는 경우 'dateObserved' 속성과 함께 사용할 수 있습니다.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateObservedTo[date-time]`: 관찰 기간: ISO8601 UTC 형식의 종료 날짜 및 시간입니다. 이 속성은 강조 표시할 시간 간격에 해당하는 경우 'dateObserved' 속성과 함께 사용할 수 있습니다.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `deepOfDischarge[number]`: 방전 깊이(코드 DoD)는 이미 방전된 용량과 축전지의 공칭 용량 사이의 비율을 %로 표시한 것입니다. 즉, 배터리에서 소비된 에너지를 의미합니다. 규칙 [DOD] = 100 % - [SOC]. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 지정됩니다. 예를 들어 **P1**은 퍼센트(%)를 나타냅니다.  . Model: [https://schema.org/Number](https://schema.org/Number)- `description[string]`: 이 항목에 대한 설명  - `id[*]`: 엔티티의 고유 식별자  - `inverterStatus[array]`: 인버터의 상태. 값의 조합입니다. Enum:'00-Onsector, 01-PowerFailure/OnBattery, 02-LossCommunication, 03-BatteryFault, 04-SystemShutDown, 05-TensionDip, 06-OverVoltage, 07-VoltageDrop, 08-VoltageIncrease, 09-LineNoise, 10-FrequencyVariation, 11-TransientDistortion, 12-HarmonicDistortion'  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `name[string]`: 이 항목의 이름  - `openCircuitVoltage[number]`: 볼트로 표시되는 개방 회로 전압(코드 OCV)은 회로에서 분리되었을 때 장치의 두 단자 사이의 전기 전위 차이를 나타냅니다. 외부 부하가 연결되지 않았고 단자 사이에 외부 전류가 흐르지 않습니다. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 부여합니다. 예를 들어 **VLT**는 볼트를 나타냅니다.  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `reactivePower[number]`: 회로에서 사용하는 무효 전력. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 지정합니다. 예를 들어 **K5**는 킬로볼트-암페어-무효 전력을 나타냅니다.  . Model: [https://schema.org/Number](https://schema.org/Number)- `refPointOfInterest[*]`: 리포지토리와 연결된 [관심 지점](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md)에 대한 참조  - `refStorageBatteryDevice[*]`: 이 관측을 캡처한 [저장 배터리 장치](https://github.com/FIWARE/data-models/blob/master/specs/Energy/StorageBatteryDevice/doc/spec.md)에 대한 참조(해당 엔티티를 사용하는 경우)  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `stateOfCharge[number]`: 충전 상태(코드 SoC)는 %로 표시되며 잔여 용량과 현재 용량 간의 비율로 정의됩니다. 현재 용량은 특정 방전 조건에서 완전히 충전된 배터리에서 인출할 수 있는 최대 용량입니다. 규칙 [SOC] + [DOD] = 100%. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 지정됩니다. 예를 들어 **P1**은 퍼센트를 나타냅니다.  . Model: [https://schema.org/Number](https://schema.org/Number)- `stateOfHealth[number]`: 건강 상태(코드 SoH)는 %로 표시되며, 완전 충전된 배터리가 공칭 방전 상태에서 제공할 수 있는 최대 충전량과 공칭 용량 간의 비율로 정의됩니다. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 지정됩니다. 예를 들어 **P1**은 퍼센트(%)를 나타냅니다.  . Model: [https://schema.org/Number](https://schema.org/Number)- `temperature[number]`: 장치의 공칭 기준 온도와 비교하여 관찰 시점에 기록된 주 온도입니다. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 지정합니다. 예를 들어 **CEL**은 섭씨도를 나타냅니다.  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSI 엔티티 유형. StorageBatteryMeasurement여야 합니다.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `dateObserved`  - `id`  - `location`  - `stateOfCharge`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬(자세한 내용을 보려면 클릭)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
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
        units: Kilowatt    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: 'The country. For example, Spain'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: 'The locality in which the street address is, and which is in the region'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: 'The region in which the locality is, and which is in the country'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: 'The post office box number for PO box addresses. For example, 03578'    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: 'The postal code. For example, 24004'    
          type: string    
          x-ngsi:    
            model: https://schema.org/https://schema.org/postalCode    
            type: Property    
        streetAddress:    
          description: The street address    
          type: string    
          x-ngsi:    
            model: https://schema.org/streetAddress    
            type: Property    
        streetNr:    
          description: Number identifying a specific property on a public street    
          type: string    
          x-ngsi:    
            type: Property    
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
      description: 'Device''s battery level. A unique value of the following value 0.0=battery empty, 1.0=Battery full, -1.0=Transiently not determined'    
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
      description: A sequence of characters identifying the provider of the harmonised data entity    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateEnergyMeteringStarted:    
      description: The starting date for metering energy in an ISO8601 UTC format    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateObservedFrom:    
      description: 'Observation period: Start date and time in an ISO8601 UTC format. The attribute can be used in addition to the ''dateObserved'' attribute when it corresponds to a time interval to be highlighted'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateObservedTo:    
      description: 'Observation period: End date and time in an ISO8601 UTC format. The attribute can be used in addition to the ''dateObserved'' attribute when it corresponds to a time interval to be highlighted'    
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
        model: https://schema.org/Number    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: Unique identifier of the entity    
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
        - description: Geojson reference to the item. Point    
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
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. LineString    
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
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. Polygon    
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
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiPoint    
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
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
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
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
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
      x-ngsi:    
        type: GeoProperty    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    openCircuitVoltage:    
      description: 'The Open Circuit Voltage (Code OCV) expressed in Volt is the difference of electrical potential between two terminals of a device when disconnected from any circuit. There is no external load connected and No external electric current flows between the terminals. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **VLT** represents Volt'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Volt    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf:    
          - description: Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Identifier format of any NGSI entity    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
        description: Unique identifier of the entity    
        x-ngsi:    
          type: Property    
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
        units: kilovolt-ampere-reactive    
    refPointOfInterest:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: 'Reference to a [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) linked with the Repository'    
      x-ngsi:    
        type: Relationship    
    refStorageBatteryDevice:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: 'Reference to a [Storage Battery Device](https://github.com/FIWARE/data-models/blob/master/specs/Energy/StorageBatteryDevice/doc/spec.md) which captured this observation, if the entity is used'    
      x-ngsi:    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    stateOfCharge:    
      description: 'The State of Charge (Code SoC) expressed in % is defined as the ratio between the remaining and the current capacities. The current capacity is the maximum capacity that can be withdrawn from the fully charged battery under specific discharge conditions. Rule [SOC] + [DOD] = 100 %. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **P1** represents Percent'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    stateOfHealth:    
      description: 'The State of Health  (Code SoH) expressed in % is defined as the ratio between the maximum amount of charge that a fully charged battery can provide under its nominal discharge regime, and its nominal capacity. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **P1** represents Percent'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    temperature:    
      description: 'Main Temperature recorded at the time of Observation compared to the  nominal reference temperature of the device. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **CEL** represents Degree Celsius'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'celsius degrees '    
    type:    
      description: NGSI Entity type. It has to be StorageBatteryMeasurement    
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
  x-version: 0.0.3    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 페이로드 예시  
#### StorageBatteryMeasurement NGSI-v2 키 값 예제  
다음은 키-값으로 JSON-LD 형식의 StorageBatteryMeasurement의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### StorageBatteryMeasurement NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 StorageBatteryMeasurement의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
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
      "coordinates": [  
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
</details>  
#### StorageBatteryMeasurement NGSI-LD 키 값 예시  
다음은 키 값으로 JSON-LD 형식의 StorageBatteryMeasurement의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
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
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Battery/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### StorageBatteryMeasurement NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 StorageBatteryMeasurement의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
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
          "coordinates": [  
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
      "https://raw.githubusercontent.com/smart-data-models/dataModel.Battery/master/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
