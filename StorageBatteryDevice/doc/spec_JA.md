Entityです。StorageBatteryDevice  
=============================  
[オープンライセンス](https://github.com/smart-data-models//dataModel.Battery/blob/master/StorageBatteryDevice/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな記述です。**蓄電池デバイスデータモデルは、電池の技術的特性とエネルギーの充放電条件を記述することを目的としています**。  

## プロパティのリスト  

- `address`: 郵送先住所  - `alternateName`: このアイテムの別称  - `application`: Enum:'electricMobility, energyStorage, emergencyStorage, houseHoldStorage, industrialStorage, lighting, production, robotics, other'.ストレージに関するデバイスのターゲットアプリケーション。列挙されたものを組み合わせたもの。  - `areaServed`: サービスや提供されるアイテムが提供される地理的なエリア  - `averageLife`: 基準温度における通常の電池使用条件での平均寿命。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて与えられます。例えば、**ANN**は年を表します。  - `batteryAssessmentMethods`: Enum:'ampereHourMeter, dischargeTest, electrolyteDensity, highFrequencyImpedance, lowFrequencyImpedance, mathematicalModel, operatingVoltageWithClosedCircuit, quiescentVoltageWithOpenCircuit'（アンペア時間計、放電試験、電解質密度、高周波インピーダンス、低周波インピーダンス、数学モデル、閉回路付き動作電圧、開回路付き静止電圧）。    - `batteryType`: Enum:'alkaline, gel, lead, lead-AGM, Li-Ion, Li-Po, Li-Po4, LMP, Li-Air, Na-NiCl2(Zebra), Ni-Cd, Ni-MH, Ni-Zn, other'.使用した電池の種類  - `brandName`: アイテムのブランド名  - `capacityCnnn`: 基準温度に応じた6つのキーの放電時間の関数としての残りのエネルギー。各キーは、{`Cnnn`:[`value1`,`value2`]}というフォーマットの構造化された値で、[CapacityCnnn]の異なる測定値を記述しています。  - `chargeDischargeReactivity`: Charge and Discharge Reactivity（充放電反応性） システムの反応性を特徴づけるもの。単位コード（テキスト）は，[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて与えられる。例えば、**SEC**はSecondを表します。  - `chargeEfficiency`: 充電効率 *(コード PV-BAT)*。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて与えられます。例えば、**P1**はPercentを表します。  - `chargePower`: ロードパワー。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて与えられる。例えば、**VLT**はVoltを表します。  - `chargingModeAllowed`: バッテリーへのダメージを避けるために許可されている充電モード enum:'fast, normal, quick'  - `communication`: メーカー別の他機器との通信プロトコルの一覧。Enum:'CAN 2.0 B, dryContactTerminal, maintenanceInterface, RS485, RS485BMS, RS485Inverter, other'.  - `dataProvider`: 調和されたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateLastReported`: デバイスがデータの報告に成功した最後の時間を示すタイムスタンプ。ISO8601 UTC形式の日付と時刻。  - `dateModified`: エンティティが最後に変更された時のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `description`: このアイテムの説明  - `dimension`: パネルの外寸。フォーマットは3項目のサブプロパティで構成される。単位コード（テキスト）は，[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて与えられる。例えば，**CMT**はCentimeter（センチメートル）を表す。  - `dischargeEfficiency`: 放電効率 *(コード PV-OND)*。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて与えられる。例えば、**P1**はPercentを表す。  - `dischargePower`: 放電量。単位コード（テキスト）は，[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて与えられる。例えば、**VLT**はVoltを表します。  - `documentation`: テクニカルドキュメント（インストール／メンテナンス／使用方法）。  - `durationPeakPower`: 属性[peakPower]に記録された基準時間。単位コード(テキスト)は[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて与えられる。例えば、**SEC**はSecondを表します。  - `id`: エンティティのユニークな識別子  - `installationCondition`: Enum:'desert, dust, extremeClimate, extremeCold, extremeHeat, extremeHumidity, marine, saline, sand, seismic, other'.以下の環境での使用が可能な状態と可能性。  - `installationMode`: Enum:'aerial, ground, pole, roofing, underGround, wall, other'.地上基準システムに対するデバイスの位置決め。  - `lifeCycleNumber`: 許容される充放電ライフサイクルの数。フォーマットは、2項目のサブプロパティで構成されています。  - `location`: アイテムへのGeojson参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygonのいずれかです。  - `manufacturerName`: メーカー名 商品名  - `massEnergyDensity`: 質量エネルギー密度*（コードD）*。一定の時間、一定の電力を供給するための電池の容量と、その重量の比。フォーマットは2項目のサブプロパティで構成されています。測定の単位コード（テキスト）は **Wh/Kg** WattHour per Kilogram  - `maxOutputPower`: 最大のパワー単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて与えられる。例えば、**KWT**はキロワットを表します。  - `maximumVoltageEOC`: 充電が終了し、かつバッテリーが充電器に接続されたままの状態での最大許容電圧。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を使用して与えられます。例えば、**VLT**はVoltを表します。  - `minimumVoltageEOD`: 放電終了後、充電器に接続されていない状態での最低電圧。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて与えられます。例えば、**VLT**はVoltを表します。  - `modelName`: アイテムのモデル名。  - `name`: このアイテムの名前です。  - `nominalAmpere`: 公称アンペア数。*(コードI)*.単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて与えられます。例えば、**AMP**はアンペアを表します。  - `nominalCapacity`: 公称エネルギー容量。*(Code C)*を属性[CapacityCnnn]とリンクさせ、放電レジームの事前定義されたレベルパラメータC / xx hを測定する。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて与えられる。例えば、 **AMH** はアンペアアワーを表します。  - `nominalFrequency`: 公称周波数。単位コード（テキスト）は，[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて与えられる。例えば、**HTZ**はHertzを表します。  - `nominalVoltage`: 公称電池電圧。*(Code U)* 単位コード(テキスト)は，[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて与えられます。例えば，**VLT**はVoltを表します。  - `operatingAltitude`: 高さと深さに対する最小と最大の抵抗を持つ動作高度。フォーマットは、[min] =<0 および [max] >=0 をキーとする2項目のサブプロパティで構成されています。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を使用して与えられます。例えば、**MTR**はメートルを表します。  - `operatingAmpere`: 許容される最小アンペアと最大アンペア。フォーマットは2項目のサブプロパティで構成されています。単位コード（テキスト）は[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて与えられる。例えば、**AMP**はアンペアを表します。  - `operatingFrequency`: 許容される最小周波数と最大周波数。フォーマットは2項目のサブプロパティで構成されています。単位コード（テキスト）は，[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて与えられる。例えば，**HTZ**はHertzを表す。  - `operatingTemperature`: 動作周囲温度の範囲。これは[イベント]の寒さや暑さに対する耐性の最小値と最大値です。フォーマットは{`event`:[min`,`max`]}という形式の3項目のサブプロパティで構成されています。単位コード（テキスト）は[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて与えられます。例えば、**CEL**は摂氏何度を表します。  - `operatingVoltage`: 許される最小電圧と最大電圧。フォーマットは2項目のサブプロパティで構成されています。単位コード（テキスト）は，[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて与えられる。例えば，**VLT**はVoltを表す。  - `overloadAccepted`: 閾値を超えるとオーバーロードを許可する(yesの場合は`true`)  - `overloadAcceptedTime`: バッテリーにダメージを与えることなく過充電時間を受け入れることができます。  - `owner`: オーナーのIDを参照するJSONエンコードされた文字列を含むリスト  - `peakPower`: 短時間で抽出可能な最大強度。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて与えられる。例えば、**KWT**はキロワットを表します。  - `possibilityOfUse`: 使用の可能性。固有の値。Enum:'mobile, mixed, stationary, other'.    - `protectionIK`: IK「機械的保護」レベル 国際電気技術委員会規格（EN 62-262）に基づき、外部からの機械的な衝撃に対する電気機器の筐体の保護の程度を数値で分類したもの。- IKは、0（最小抵抗）から10（最大抵抗）まで変化し、衝撃エネルギー（単位ジュール）を表します。  - `protectionIP`: ジャンクションボックスのIP*Ingress Protection*。国際電気標準会議の規格（EN 60-529）に基づいて、機械的な筐体や電気的な筐体が、侵入、塵埃、偶発的な接触、水に対する保護の度合いを分類、評価したものです。- 1桁目1桁目：固体粒子に対する保護等級（単一の数字：0～6または「X」）。- 2桁目1桁目：固体粒子に対する保護等級（数字0～6またはX） 2桁目：液体に対する保護等級（数字0～9またはX- 3桁目3桁目：危険な部品へのアクセスに対する個人保護（オプションの追加文字）。- 4桁目その他の保護機能（オプションで追加文字）。  - `rechargeEnergySource`: Enum:'electric, hydraulic, windTurbine, other'.Recharge Energy Sourceの略。リストのユニークな値  - `refDevice`: 2番目のリンクとして使用される場合、Main Entity [Device](https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md)への参照。  - `refPointOfInterest`: 観測データに関連する[PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md)への参照。  - `roundTripEfficiency`: Round-Trip Efficiencyの略。蓄積されたエネルギーと還元されたエネルギーの比率として定義される効率。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて与えられる。例えば、**P1**はPercentを表す。  - `seeAlso`: アイテムに関する追加リソースを示すuriのリスト  - `selfDischargeRate`: 基準温度]による1ヶ月のベースラインでの未使用時のバッテリー放電率。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を使用して与えられます。例えば、**P1**はPercentageを表します。  - `serialNumber`: アイテムのシリアルナンバー  - `source`: エンティティデータのオリジナルソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `storableEnergy`: 総蓄電量＝[nominalVoltage] * [nominalCapacity]。単位コード（テキスト）は，[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて与えられる。例えば、**KWH**はKilowatt Hourを表します。  - `toolBMS`: バッテリーの寿命を保護、保証、最適化するためのバッテリー管理システムツールの使用。(はいの場合は`true`)  - `type`: StorageBatteryDeviceである必要があります。  - `typeEnergySource`: Enum:'dam, fall, generator, network, photovoltaic, river, sea, waterTurbine, wind, other'.RechargeEnergySource`属性に関するエネルギー源のタイプ。  - `typeOfUse`: 屋内／屋外環境での配置に関する使用を認める。列挙：'屋内、混合、屋外、その他'  - `usableEnergy`: 使えるエネルギー。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて与えられる。例えば、**KWH**はKilowatt Hourを表します。  - `volEnergyDensity`: 体積 エネルギー密度 *(コードD)*。フォーマットは2項目のサブプロパティで構成されています。測定単位コード（テキスト）は **Wh/L** WattHour per Liter  - `weight`: 重量です。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を使用して与えられます。例えば、**KGM**はKiloGrammeを表します。    
必須項目  
- `batteryType`  - `dateLastReported`  - `id`  - `location`  - `rechargeEnergySource`  - `type`    
充電機能は、「オンボードシステム、ソーラーパネル、風力発電機、発電機、電源」などの電源から適用されます。本バージョンでは、油圧源は含まれていません。放電機能は、蓄電池からのエネルギー消費を必要とするすべてのタイプのシステムに適用されます。*Remark* このデータモデルは、デバイス *Battery Storage* を記述するメインエンティティとして直接使用することも、*refDevice* 属性による参照を使用してデータモデル *DEVICE* のサブエンティティとして使用することもできます。  
## データモデルによるプロパティの記述  
アルファベット順（クリックすると詳細が表示されます）  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
StorageBatteryDevice:    
  description: 'The storage battery device data model is intended to describe the technical characteristics of the battery and the charging and discharging conditions of the energy.'    
  properties:    
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
    application:    
      description: 'Enum:''electricMobility, energyStorage, emergencyStorage, houseHoldStorage, industrialStorage, lighting, production, robotics, other''. Target application of the Device regarding the storage. A combination of the enumeration.'    
      items:    
        enum:    
          - electricMobility    
          - energyStorage    
          - emergencyStorage    
          - houseHoldStorage    
          - industrialStorage    
          - lighting    
          - production    
          - robotics    
          - other    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    averageLife:    
      description: 'average life under normal battery usage conditions at reference temperatures. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **ANN** represents Year'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: year    
    batteryAssessmentMethods:    
      description: 'Enum:''ampereHourMeter, dischargeTest, electrolyteDensity, highFrequencyImpedance, lowFrequencyImpedance, mathematicalModel, operatingVoltageWithClosedCircuit, quiescentVoltageWithOpenCircuit''.  '    
      enum:    
        - ampereHourMeter    
        - dischargeTest    
        - electrolyteDensity    
        - highFrequencyImpedance    
        - lowFrequencyImpedance    
        - mathematicalModel    
        - operatingVoltageWithClosedCircuit    
        - quiescentVoltageWithOpenCircuit    
      minItems: 0    
      type: string    
      uniqueItems: true    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    batteryType:    
      description: 'Enum:''alkaline, gel, lead, lead-AGM, Li-Ion, Li-Po, Li-Po4, LMP, Li-Air, Na-NiCl2(Zebra), Ni-Cd, Ni-MH, Ni-Zn, other''. Type of battery used.'    
      enum:    
        - alkaline    
        - gel    
        - lead    
        - lead-AGM    
        - Li-Ion    
        - Li-Po    
        - Li-Po4    
        - LMP    
        - Li-Air    
        - Na-NiCl2(Zebra)    
        - Ni-Cd    
        - Ni-MH    
        - Ni-Zn    
        - other    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    brandName:    
      description: 'Brand Name of the item.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    capacityCnnn:    
      description: 'Remaining energy as a function of the discharge time for 6 keys according the temperature of reference. Each Key is a structured value with the format {`Cnnn`:[`value1`,`value2`]} describing the different measurement of [CapacityCnnn].'    
      properties:    
        C001:    
          items:    
            type: number    
          type: array    
        C005:    
          items:    
            type: number    
          type: array    
        C010:    
          items:    
            type: number    
          type: array    
        C020:    
          items:    
            type: number    
          type: array    
        C050:    
          items:    
            type: number    
          type: array    
        C100:    
          items:    
            type: number    
          type: array    
      type: object    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    chargeDischargeReactivity:    
      description: ' Charge and Discharge Reactivity which characterizes the reactive behavior of the system. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **SEC** represents Second'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: seconds    
    chargeEfficiency:    
      description: 'Charge Efficiency *(code PV-BAT)*. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **P1** represents Percent.'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    chargePower:    
      description: 'Load Power. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **VLT** represents Volt'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: volts    
    chargingModeAllowed:    
      description: ' Charging mode permitted to avoid damage to the battery. enum:''fast, normal, quick'''    
      items:    
        enum:    
          - normal    
          - quick    
          - fast    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    communication:    
      description: 'List of communication protocol with others device depending manufacturers. Enum:''CAN 2.0 B, dryContactTerminal, maintenanceInterface, RS485, RS485BMS, RS485Inverter, other'''    
      items:    
        enum:    
          - 'CAN 2.0 B'    
          - dryContactTerminal    
          - maintenanceInterface    
          - RS485    
          - RS485BMS    
          - RS485Inverter    
          - other    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/    
        type: Property    
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
    dateLastReported:    
      description: 'A timestamp which denotes the last time when the device successfully reported data. Date and time in an ISO8601 UTCformat. '    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    dimension:    
      description: 'External dimension of a Panel. The format is structured by a sub-property of 3 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **CMT** represents Centimeter'    
      properties:    
        depth:    
          minimum: 0    
          type: number    
        height:    
          minimum: 0    
          type: number    
        width:    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
        units: Centimeters    
    dischargeEfficiency:    
      description: 'Discharge Efficiency *(code PV-OND)*. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **P1** represents Percent.'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    dischargePower:    
      description: 'Discharge Power. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **VLT** represents Volt'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: volts    
    documentation:    
      description: 'Technical Documentation (Installation / maintenance / use).'    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    durationPeakPower:    
      description: 'Reference Time recorded for the attribute [peakPower]. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **SEC** represents Second'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: seconds    
    id:    
      anyOf: &storagebatterydevice_-_properties_-_owner_-_items_-_anyof    
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
    installationCondition:    
      description: 'Enum:''desert, dust, extremeClimate, extremeCold, extremeHeat, extremeHumidity, marine, saline, sand, seismic, other''. Condition and possibility of use in the following environments.'    
      items:    
        enum:    
          - desert    
          - dust    
          - extremeClimate    
          - extremeCold    
          - extremeHeat    
          - extremeHumidity    
          - marine    
          - saline    
          - sand    
          - seismic    
          - other    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    installationMode:    
      description: 'Enum:''aerial, ground, pole, roofing, underGround, wall, other''. Positioning of the device in relation to a ground reference system.'    
      enum:    
        - aerial    
        - ground    
        - pole    
        - roofing    
        - underGround    
        - wall    
        - other    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    lifeCycleNumber:    
      description: 'Number of admissible charge / discharge life cycles. The format is structured by a sub-property of 2 items.'    
      properties:    
        max:    
          minimum: 0    
          type: number    
        min:    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        model: https://schema.org/Number    
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
    manufacturerName:    
      description: 'Manufacturer Name of the item.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    massEnergyDensity:    
      description: 'Mass Energy density *(Code D)*. Ratio between the capacity of the battery to deliver a certain power for a certain time and its weight. The format is structured by a sub-property of 2 items. The unit code (text) of measurement is **Wh/Kg** WattHour per Kilogram'    
      properties:    
        max:    
          minimum: 0    
          type: number    
        min:    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'W hour / Kg'    
    maxOutputPower:    
      description: 'Maximum Power. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **KWT** represents Kilowatt'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Kw    
    maximumVoltageEOC:    
      description: 'Maximum authorized voltage after end of charge and Battery still connected to to a charge generator. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **VLT** represents Volt'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: volts    
    minimumVoltageEOD:    
      description: 'Minimum voltage after end of discharge and not connected to to a charge generator. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **VLT** represents Volt'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: volts    
    modelName:    
      description: 'Model Name of the item. '    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    nominalAmpere:    
      description: 'Nominal Amperage. *(Code I)*. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **AMP** represents Ampere'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: amperes    
    nominalCapacity:    
      description: 'Nominal Energy capacity. *(Code C)* to link with the attribute [CapacityCnnn] to measure the predefined levels parameters C / xx h of discharge regimes. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **AMH** represents Ampere Hour'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'Ampere Hour'    
    nominalFrequency:    
      description: 'Nominal Frequency. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **HTZ** represents Hertz'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: hertz    
    nominalVoltage:    
      description: 'Nominal battery voltage. *(Code U)* The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **VLT** represents Volt'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: volts.    
    operatingAltitude:    
      description: 'Operating altitude with minimum and maximum resistance to height and depth. The format is structured by a sub-property of 2 items with the keys [min] =<0 and [max] >=0. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **MTR** represents Meter'    
      properties:    
        max:    
          minimum: 0    
          type: number    
        min:    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: meters    
    operatingAmpere:    
      description: ' Minimum and Maximum Ampere allowed. The format is structured by a sub-property of 2 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **AMP** represents Ampere'    
      properties:    
        max:    
          minimum: 0    
          type: number    
        min:    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: amperes    
    operatingFrequency:    
      description: ' Minimum and Maximum frequency allowed. The format is structured by a sub-property of 2 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **HTZ** represents Hertz'    
      properties:    
        max:    
          minimum: 0    
          type: number    
        min:    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: hertz    
    operatingTemperature:    
      description: 'Ambient operating temperature range. This is the minimum and maximum resistance to cold and heat for an [event]. The format is structured by a sub-property of 3 items with the format  {`event`:[`min`,`max`]}. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **CEL** represents Degree Celsius'    
      properties:    
        charge:    
          description: 'Property. Model:''https://schema.org/Number''. Charge of the item'    
          items:    
            type: number    
          type: array    
        discharge:    
          description: 'Property. Model:''https://schema.org/Number''. Discharge of the item '    
          items:    
            type: number    
          type: array    
        storage:    
          description: 'Property. Model:''https://schema.org/Number''. Storage of the item'    
          items:    
            type: number    
          type: array    
      type: object    
      x-ngsi:    
        type: Property    
        units: 'degrees Celsius'    
    operatingVoltage:    
      description: 'Minimum and Maximum voltage allowed. The format is structured by a sub-property of 2 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **VLT** represents Volt'    
      properties:    
        max:    
          minimum: 0    
          type: number    
        min:    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: volt    
    overloadAccepted:    
      description: 'Overload is permitted after exceeding the threshold.(`true` for yes)'    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
        type: Property    
    overloadAcceptedTime:    
      description: 'Accepted overcharge time without damage to the battery.'    
      format: time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *storagebatterydevice_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    peakPower:    
      description: ' Maximum intensity extractable over a short period. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **KWT** represents Kilowatt'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Kw    
    possibilityOfUse:    
      description: 'Possibility of use. A unique value. Enum:''mobile, mixed, stationary, other''.  '    
      enum:    
        - mobile    
        - mixed    
        - stationary    
        - other    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    protectionIK:    
      description: 'IK ''Mecanic Protection'' level relating to numeric classification for the degrees of protection provided by enclosures for electrical equipment against external mechanical impacts, according to International Electro technical Commission standard (EN 62-262). - IK varies from 0 (minimum resistance) to 10 (maximum resistance) which represents an Impact Energy (Unit Joule)'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number.    
        type: Property    
    protectionIP:    
      description: 'IP *Ingress Protection* for the Junction Box. This is the level classifies and rates the degree of protection provided by mechanical casings and electrical enclosures against intrusion, dust, accidental contact, and water according to International Electrotechnical Commission standard (EN 60-529). - First digit: Solid particle protection (Single numeral: 0–6 or ''X''). - Second digit: Liquid ingress protection (Single numeral: 0–9 or ''X''). - Third digit: Personal Protection  against access to dangerous parts (optional additional letter). - Fourth digit: Other protections (optional additional letter)'    
      type: string    
      x-ngsi:    
        model: https://en.wikipedia.org/wiki/IP_Code.    
        type: Property    
    rechargeEnergySource:    
      description: 'Enum:''electric, hydraulic, windTurbine, other''. Recharge Energy Source. A unique value of the list '    
      enum:    
        - electric    
        - hydraulic    
        - windTurbine    
        - other    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    refDevice:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to the Main Entity [Device](https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md) if used as second link.'    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
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
      description: 'Reference to a [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) linked with the observation.'    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    roundTripEfficiency:    
      description: 'Round-Trip Efficiency. Efficiency, defined as the ratio between stored energy and returned energy. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **P1** represents Percent.'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
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
    selfDischargeRate:    
      description: 'Battery discharge rate without any use on a baseline of 1 month according the [temperature of reference]. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **P1** represents Percentage.'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    serialNumber:    
      description: 'Serial numbers of the item.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    storableEnergy:    
      description: 'Total Storage Energy = [nominalVoltage] * [nominalCapacity]. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **KWH** represents Kilowatt Hour'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'Kw Hour'    
    toolBMS:    
      description: 'Use of a Battery Management System tool to protect, guarantee and optimize battery life. (`true` for yes)'    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
        type: Property    
    type:    
      description: 'It has to be StorageBatteryDevice'    
      enum:    
        - StorageBatteryDevice    
      type: string    
      x-ngsi:    
        model: 'https://schema.org/Text '    
        type: Property    
    typeEnergySource:    
      description: 'Enum:''dam, fall, generator, network, photovoltaic, river, sea, waterTurbine, wind, other''. Type of Energy Source regarding `RechargeEnergySource` attribute.'    
      items:    
        enum:    
          - dam    
          - fall    
          - generator    
          - network    
          - photovoltaic    
          - river    
          - sea    
          - waterTurbine    
          - wind    
          - other    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    typeOfUse:    
      description: 'Accepted use regarding its positioning in an indoor / outdoor environment. Enum:'' indoor, mixed, outdoor, other'''    
      enum:    
        - indoor    
        - mixed    
        - outdoor    
        - other    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    usableEnergy:    
      description: 'Usable Energy. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **KWH** represents Kilowatt Hour'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'Kw Hour'    
    volEnergyDensity:    
      description: 'Volume Energy density *(Code D)*. The format is structured by a sub-property of 2 items. The unit code (text) of measurement is **Wh/L** WattHour per Liter'    
      properties:    
        max:    
          minimum: 0    
          type: number    
        min:    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Wh/L    
    weight:    
      description: 'Weight. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **KGM** represents KiloGramme'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/weight    
        type: Property    
        units: Kilograms    
  required:    
    - id    
    - type    
    - location    
    - dateLastReported    
    - batteryType    
    - rechargeEnergySource    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Battery/blob/master/StorageBatteryDevice/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/data-models.Energy/StorageBatteryDevice/schema.json    
  x-model-tags: ""    
  x-version: 0.0.2    
```  
</details>    
## ペイロードの例  
#### StorageBatteryDevice NGSI-v2 key-valuesの例。  
JSON-LD形式でStorageBatteryDeviceをkey-valuesとして表現した例です。これは、`options=keyValues`を使用した場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### StorageBatteryDevice NGSI-v2 正規化された例。  
ここでは、正規化されたJSON-LD形式のStorageBatteryDeviceの例を示します。これは、オプションを使用しない場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### StorageBatteryDevice NGSI-LDのキーバリューの例。  
JSON-LD形式でStorageBatteryDeviceをkey-valuesとして表現した例です。これは、`options=keyValues`を使用した場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
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
    "value": "AirPort \u2013 global Observation"  
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
        43.66481,  
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
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### StorageBatteryDevice NGSI-LD 正規化された例。  
ここでは、正規化されたJSON-LD形式のStorageBatteryDeviceの例を示します。これは、オプションを使用しない場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "urn:ngsi-ld:StorageBatteryDevice:StorageBatteryDevice:MNCA-SBD-T1-G0-027",  
  "type": "StorageBatteryDevice",  
  "name": "SBD-T1-G0-027",  
  "alternateName": "AirPort \u2013 global Observation",  
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
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
