<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティStorageBatteryDevice  
==========================<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.Battery/blob/master/StorageBatteryDevice/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述：**蓄電池機器データモデルは、蓄電池の技術特性やエネルギーの充放電条件を記述することを目的としている。  
バージョン: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティのリスト  

<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国。例えば、スペイン  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 番地がある地域と、その地域に含まれる地域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: その地域がある地域、またその国がある地域  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 地区とは行政区画の一種で、国によっては地方自治体によって管理されている。    
	- `postOfficeBoxNumber[string]`: 私書箱の住所のための私書箱番号。例：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 郵便番号。例：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 番地  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: この項目の別名  - `application[array]`: Enum:'electricMobility, energyStorage, emergencyStorage, houseHoldStorage, industrialStorage, lighting, production, robotics, other'.ストレージに関するデバイスのターゲットアプリケーション。列挙の組み合わせ  . Model: [https://schema.org/Text](https://schema.org/Text)- `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `averageLife[number]`: 基準温度における通常の電池使用条件下での平均寿命。単位コード（テキスト）は、[UN/CEFACT 共通コード](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) を使用しています。例えば、**ANN**はYearを表します。  . Model: [https://schema.org/Number](https://schema.org/Number)- `batteryAssessmentMethods[string]`: Enum:'ampereHourMeter, dischargeTest, electrolyteDensity, highFrequencyImpedance, lowFrequencyImpedance, mathematicalModel, operatingVoltageWithClosedCircuit, quiescentVoltageWithOpenCircuit'.    . Model: [https://schema.org/Text](https://schema.org/Text)- `batteryType[string]`: Enum:'alkaline, gel, lead, lead-AGM, Li-Ion, Li-Po, Li-Po4, LMP, Li-Air, Na-NiCl2(Zebra), Ni-Cd, Ni-MH, Ni-Zn, other'.使用電池の種類  . Model: [https://schema.org/Text](https://schema.org/Text)- `brandName[string]`: 商品のブランド名  . Model: [https://schema.org/Text](https://schema.org/Text)- `capacityCnnn[object]`: 基準温度に応じた6つのキーの放電時間の関数としての残存エネルギー。各キーは{`Cnnn`:[`value1`,`value2`]}のフォーマットで構造化された値であり、[CapacityCnnn]の異なる測定値を記述する。  . Model: [https://schema.org/Number](https://schema.org/Number)	- `C001`:     
	- `C005`:     
	- `C010`:     
	- `C020`:     
	- `C050`:     
- `chargeDischargeReactivity[number]`: システムの反応挙動を特徴付ける充放電反応性。単位コード（テキスト）は、[UN/CEFACT 共通コード](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) を用いて与えられる。例えば、**SEC**はSecondを表します。  . Model: [https://schema.org/Number](https://schema.org/Number)- `chargeEfficiency[number]`: 充電効率 *(コード PV-BAT)*。単位コード(テキスト)は、[UN/CEFACT 共通コード](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて与えられる。例えば、**P1** はパーセントを表す。  . Model: [https://schema.org/Number](https://schema.org/Number)- `chargePower[number]`: 負荷電力。単位コード（テキスト）は、[UN/CEFACT 共通コード](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて示される。例えば、**VLT** はボルトを表す。  . Model: [https://schema.org/Number](https://schema.org/Number)- `chargingModeAllowed[array]`: enum:'fast, normal, quick' バッテリーへのダメージを避けるために許される充電モード。  . Model: [https://schema.org/Text](https://schema.org/Text)- `communication[array]`: 通信プロトコルの一覧です。Enum:'CAN 2.0 B, dryContactTerminal, maintenanceInterface, RS485, RS485BMS, RS485Inverter, other'.  . Model: [https://schema.org/](https://schema.org/)- `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateLastReported[date-time]`: デバイスが正常にデータを報告した最後の時刻を示すタイムスタンプ。ISO8601 UTCフォーマットの日付と時刻。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `dimension[object]`: パネルの外部寸法。フォーマットは 3 項目のサブプロパティで構成される。単位コード（テキスト）は、[UN/CEFACT 共通コード](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) を使用して指定する。例えば、**CMT** はセンチメートルを表す。  	- `depth`:     
	- `height`:     
- `dischargeEfficiency[number]`: 放電効率 *(コード PV-OND)*。単位コード（テキスト）は、[UN/CEFACT 共通コード](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) を用いて与えられる。例えば、**P1** は Percent を表す。  . Model: [https://schema.org/Number](https://schema.org/Number)- `dischargePower[number]`: 放電電力。単位コード（テキスト）は、[UN/CEFACT 共通コード](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) を用いて与えられる。例えば、**VLT** はボルトを表す。  . Model: [https://schema.org/Number](https://schema.org/Number)- `documentation[string]`: 技術文書（設置／メンテナンス／使用方法）  . Model: [https://schema.org/URL](https://schema.org/URL)- `durationPeakPower[number]`: 属性[peakPower]に記録された基準時間。単位コード（テキスト）は、[UN/CEFACT 共通コード](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) を使用して指定します。例えば、**SEC** は Second を表す。  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: エンティティの一意識別子  - `installationCondition[array]`: Enum:'desert, dust, extremeClimate, extremeCold, extremeHeat, extremeHumidity, marine, saline, sand, seismic, other'.以下の環境での使用条件と可能性  . Model: [https://schema.org/Text](https://schema.org/Text)- `installationMode[string]`: Enum:'aerial, ground, pole, roofing, underGround, wall, other'.地上基準システムに対するデバイスの位置決め  . Model: [https://schema.org/Text](https://schema.org/Text)- `lifeCycleNumber[object]`: 許容される充放電ライフサイクル数。このフォーマットは、2つの項目のサブプロパティによって構成されています。  . Model: [https://schema.org/Number](https://schema.org/Number)	- `max`:     
- `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `manufacturerName[string]`: メーカー名  . Model: [https://schema.org/Text](https://schema.org/Text)- `massEnergyDensity[object]`: 質量エネルギー密度*（コードD）*。一定の電力を一定時間供給する電池の容量と重量の比。フォーマットは2項目のサブプロパティで構成される。測定単位コード（テキスト）は、**Wh/Kg** WattHour per Kilogram です。  . Model: [https://schema.org/Number](https://schema.org/Number)	- `max`:     
- `maxOutputPower[number]`: 最大出力。単位コード（テキスト）は、[UN/CEFACT 共通コード](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) を用いて示される。例えば、**KWT** はキロワットを表す。  . Model: [https://schema.org/Number](https://schema.org/Number)- `maximumVoltageEOC[number]`: 充電が終了し、バッテリーがまだ充電ジェネレーターに接続されている状態での最大認可電圧。単位コード（テキスト）は、[UN/CEFACT 共通コード](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) を使用して示される。例えば、**VLT**はVolt（ボルト）を表します。  . Model: [https://schema.org/Number](https://schema.org/Number)- `minimumVoltageEOD[number]`: 放電終了後の最低電圧で、充電発電機に接続されていない状態。単位コード（テキスト）は、[UN/CEFACT 共通コード](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) を用いて与えられる。例えば、**VLT**はVolt（ボルト）を表す。  . Model: [https://schema.org/Number](https://schema.org/Number)- `modelName[string]`: アイテムのモデル名  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: このアイテムの名前  - `nominalAmpere[number]`: 公称アンペア数。*(コード I)*。単位コード（テキスト）は、[UN/CEFACT 共通コード](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) を使用して示される。例えば、**AMP**はアンペアを表す。  . Model: [https://schema.org/Number](https://schema.org/Number)- `nominalCapacity[number]`: 公称エネルギー容量。*(コード C)*は、属性[CapacityCnnn]とリンクし、放電レジームの定義済みレベルパラメータC / xx hを測定する。単位コード（テキスト）は、[UN/CEFACT 共通コード](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) を用いて与えられる。例えば、**AMH** はアンペアアワーを表す。  . Model: [https://schema.org/Number](https://schema.org/Number)- `nominalFrequency[number]`: 公称周波数。単位コード（テキスト）は、[UN/CEFACT 共通コード](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) を使用して指定する。例えば、**HTZ** はヘルツを表す。  . Model: [https://schema.org/Number](https://schema.org/Number)- `nominalVoltage[number]`: 公称バッテリー電圧。*単位コード（テキスト）は、[UN/CEFACT 共通コード](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) を使用します。例えば、**VLT**はVolt(ボルト)を表します。  . Model: [https://schema.org/Number](https://schema.org/Number)- `operatingAltitude[object]`: 高さと深さに対する最小と最大の抵抗を持つ動作高度。フォーマットは、[min] =<0、[max] >=0 をキーとする 2 項目のサブプロパティで構成される。単位コード（テキスト）は、[UN/CEFACT 共通コード](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) を用いて与えられる。例えば、**MTR** は Meter を表す。  . Model: [https://schema.org/Number](https://schema.org/Number)	- `max`:     
- `operatingAmpere[object]`: 許容最小アンペアと最大アンペア。フォーマットは 2 項目のサブプロパティで構成される。単位コード（テキスト）は、[UN/CEFACT 共通コード](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) を使用して指定します。例えば、**AMP** はアンペアを表します。  . Model: [https://schema.org/Number](https://schema.org/Number)	- `max`:     
- `operatingFrequency[object]`: 許容される最小頻度と最大頻度。フォーマットは 2 項目のサブプロパティで構成される。単位コード（テキスト）は、[UN/CEFACT 共通コード](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) を用いて与えられる。例えば、**HTZ** はヘルツを表す。  . Model: [https://schema.org/Number](https://schema.org/Number)	- `max`:     
- `operatingTemperature[object]`: 周囲動作温度範囲。これは[event]の寒さと熱に対する最小値と最大値である。このフォーマットは {`event`:[`min`,`max`]} というフォーマットで 3 項目のサブプロパティによって構成される。単位コード（テキスト）は、[UN/CEFACT 共通コード](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) を用いて与えられる。例えば、**CEL**は摂氏を表します。  	- `charge[array]`: 商品代金  . Model: [https://schema.org/Number](https://schema.org/Number)  
	- `discharge[array]`: 排出物  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `operatingVoltage[object]`: 許容される最小電圧と最大電圧。フォーマットは 2 項目のサブプロパティで構成される。単位コード（テキスト）は、[UN/CEFACT 共通コード](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) を使用して指定します。例えば、**VLT** は Volt を表します。  . Model: [https://schema.org/Number](https://schema.org/Number)	- `max`:     
- `overloadAccepted[boolean]`: 閾値を超えると過負荷を許可する(yesの場合は`true`)  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `overloadAcceptedTime[time]`: バッテリーに損傷を与えることなく過充電時間を許容する。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `peakPower[number]`: 短時間で抽出可能な最大強度。単位コード（テキスト）は、[UN/CEFACT 共通コード](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) を用いて与えられる。例えば、**KWT**はキロワットを表す。  . Model: [https://schema.org/Number](https://schema.org/Number)- `possibilityOfUse[string]`: 使用の可能性。ユニークな値。Enum:'mobile, mixed, stationary, other'.    . Model: [https://schema.org/Text](https://schema.org/Text)- `protectionIK[number]`: IK「機械的保護」レベルは、国際電気技術委員会規格（EN 62-262）に基づき、外部からの機械的衝撃に対して電気機器用エンクロージャが提供する保護の程度を数値で分類したもの。- IKは0（最小抵抗）から10（最大抵抗）まであり、衝撃エネルギー（単位ジュール）を表します。  . Model: [https://schema.org/Number](https://schema.org/Number)- `protectionIP[string]`: ジャンクションボックスのIP *Ingress Protection*。これは、国際電気標準会議規格（EN 60-529）に従い、侵入、ほこり、偶発的な接触、および水に対する機械的なケーシングと電気的なエンクロージャが提供する保護の程度を分類し、評価するレベルです。- 一桁目1桁目：固体粒子に対する保護等級（1桁の数字：0～6または'X'）。- 2桁目2桁目：液体浸入保護（1桁の数字：0～9または「X」）。- 3桁目危険な部品へのアクセスに対する個人保護（オプションの追加文字）。- 4桁目その他の保護（オプションの追加文字）  . Model: [https://en.wikipedia.org/wiki/IP_Code](https://en.wikipedia.org/wiki/IP_Code)- `rechargeEnergySource[string]`: Enum:'electric, hydraulic, windTurbine, other'.充電エネルギー源。リストの一意な値  . Model: [https://schema.org/Text](https://schema.org/Text)- `refDevice[*]`: セカンドリンクとして使用される場合、メインエンティティ[デバイス](https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md)への参照  . Model: [https://schema.org/URL](https://schema.org/URL)- `refPointOfInterest[*]`: 観測とリンクしている[PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md)への参照。  . Model: [https://schema.org/URL](https://schema.org/URL)- `roundTripEfficiency[number]`: 往復効率。蓄積エネルギーと帰還エネルギーの比として定義される効率。単位コード（テキスト）は、[UN/CEFACT 共通コード](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) を用いて与えられる。例えば、**P1** は Percent を表す。  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `selfDischargeRate[number]`: 基準温度]に従い、1ヶ月間使用しない場合の電池放電率。単位コード（テキスト）は、[UN/CEFACT 共通コード](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) を用いて与えられる。例えば、**P1** は Percentage（パーセント）を表す。  . Model: [https://schema.org/Number](https://schema.org/Number)- `serialNumber[string]`: 商品のシリアル番号  . Model: [https://schema.org/Text](https://schema.org/Text)- `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `storableEnergy[number]`: 総蓄電エネルギー = [公称電圧] * [公称容量]。単位コード（テキスト）は、[UN/CEFACT 共通コード](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) を用いて与えられる。例えば、**KWH**はキロワット時を表す。  . Model: [https://schema.org/Number](https://schema.org/Number)- `toolBMS[boolean]`: バッテリー寿命の保護、保証、最適化のためのバッテリー管理システムツールの使用。(はいなら`true`）。  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `type[string]`: StorageBatteryDeviceでなければならない。  . Model: [https://schema.org/Text ](https://schema.org/Text )- `typeEnergySource[array]`: Enum:'dam, fall, generator, network, photovoltaic, river, sea, waterTurbine, wind, other'.RechargeEnergySource`属性に関するエネルギー源の種類  . Model: [https://schema.org/Text](https://schema.org/Text)- `typeOfUse[string]`: 屋内／屋外環境での位置づけに関する使用を認める。列挙：' 屋内, 混合, 屋外, その他'  . Model: [https://schema.org/Text](https://schema.org/Text)- `usableEnergy[number]`: 使用可能エネルギー。単位コード（テキスト）は、[UN/CEFACT 共通コード](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) を用いて与えられる。例えば、**KWH**はキロワット時を表す。  . Model: [https://schema.org/Number](https://schema.org/Number)- `volEnergyDensity[object]`: 体積エネルギー密度 *(コード D)*。フォーマットは2項目のサブプロパティで構成される。測定単位コード（テキスト）は、**Wh/L** WattHour per Liter です。  . Model: [https://schema.org/Number](https://schema.org/Number)	- `max`:     
- `weight[number]`: 重量。単位コード（テキスト）は、[UN/CEFACT 共通コード](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) を用いて与えられる。例えば、**KGM**はキログラムを表す。  . Model: [https://schema.org/weight](https://schema.org/weight)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必須プロパティ  
- `batteryType`  - `dateLastReported`  - `id`  - `location`  - `rechargeEnergySource`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
充電機能は、「車載システム、ソーラーパネル、風力タービン、発電機、電源」を使用できる電源から適用される。油圧源はこのバージョンには含まれていません。放電機能は、蓄電池からのエネルギー消費を必要とするすべてのタイプのシステムに適用される。*このデータモデルは、*Battery Storage* というデバイスを記述するメインエンティティとして直接使用することも、*refDevice* 属性による参照を使用して、*DEVICE* というデータモデルのサブエンティティとして使用することもできる。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順（クリックで詳細表示）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
StorageBatteryDevice:    
  description: The storage battery device data model is intended to describe the technical characteristics of the battery and the charging and discharging conditions of the energy.    
  properties:    
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
    application:    
      description: 'Enum:''electricMobility, energyStorage, emergencyStorage, houseHoldStorage, industrialStorage, lighting, production, robotics, other''. Target application of the Device regarding the storage. A combination of the enumeration'    
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
      description: The geographic area where a service or offered item is provided    
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
      description: 'Enum:''alkaline, gel, lead, lead-AGM, Li-Ion, Li-Po, Li-Po4, LMP, Li-Air, Na-NiCl2(Zebra), Ni-Cd, Ni-MH, Ni-Zn, other''. Type of battery used'    
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
      description: Brand Name of the item    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    capacityCnnn:    
      description: 'Remaining energy as a function of the discharge time for 6 keys according the temperature of reference. Each Key is a structured value with the format {`Cnnn`:[`value1`,`value2`]} describing the different measurement of [CapacityCnnn]'    
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
      description: 'Charge Efficiency *(code PV-BAT)*. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **P1** represents Percent'    
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
          - CAN 2.0 B    
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
    dateLastReported:    
      description: 'A timestamp which denotes the last time when the device successfully reported data. Date and time in an ISO8601 UTCformat. '    
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
    description:    
      description: A description of this item    
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
      description: 'Discharge Efficiency *(code PV-OND)*. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **P1** represents Percent'    
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
      description: Technical Documentation (Installation / maintenance / use)    
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
    installationCondition:    
      description: 'Enum:''desert, dust, extremeClimate, extremeCold, extremeHeat, extremeHumidity, marine, saline, sand, seismic, other''. Condition and possibility of use in the following environments'    
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
      description: 'Enum:''aerial, ground, pole, roofing, underGround, wall, other''. Positioning of the device in relation to a ground reference system'    
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
      description: Number of admissible charge / discharge life cycles. The format is structured by a sub-property of 2 items    
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
    manufacturerName:    
      description: Manufacturer Name of the item    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    massEnergyDensity:    
      description: Mass Energy density *(Code D)*. Ratio between the capacity of the battery to deliver a certain power for a certain time and its weight. The format is structured by a sub-property of 2 items. The unit code (text) of measurement is **Wh/Kg** WattHour per Kilogram    
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
        units: W hour / Kg    
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
      description: The name of this item    
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
        units: Ampere Hour    
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
        units: volts    
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
          description: Charge of the item    
          items:    
            type: number    
          type: array    
          x-ngsi:    
            model: https://schema.org/Number    
            type: Property    
        discharge:    
          description: 'Discharge of the item '    
          items:    
            type: number    
          type: array    
          x-ngsi:    
            model: https://schema.org/Number    
            type: Property    
        storage:    
          description: Storage of the item    
          items:    
            type: number    
          type: array    
          x-ngsi:    
            model: https://schema.org/Number    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
        units: degrees Celsius    
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
      description: Overload is permitted after exceeding the threshold.(`true` for yes)    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
        type: Property    
    overloadAcceptedTime:    
      description: Accepted overcharge time without damage to the battery    
      format: time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
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
        model: https://schema.org/Number    
        type: Property    
    protectionIP:    
      description: 'IP *Ingress Protection* for the Junction Box. This is the level classifies and rates the degree of protection provided by mechanical casings and electrical enclosures against intrusion, dust, accidental contact, and water according to International Electrotechnical Commission standard (EN 60-529). - First digit: Solid particle protection (Single numeral: 0–6 or ''X''). - Second digit: Liquid ingress protection (Single numeral: 0–9 or ''X''). - Third digit: Personal Protection  against access to dangerous parts (optional additional letter). - Fourth digit: Other protections (optional additional letter)'    
      type: string    
      x-ngsi:    
        model: https://en.wikipedia.org/wiki/IP_Code    
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
      description: 'Reference to the Main Entity [Device](https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md) if used as second link'    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
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
      description: 'Reference to a [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) linked with the observation'    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    roundTripEfficiency:    
      description: 'Round-Trip Efficiency. Efficiency, defined as the ratio between stored energy and returned energy. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **P1** represents Percent'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
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
    selfDischargeRate:    
      description: 'Battery discharge rate without any use on a baseline of 1 month according the [temperature of reference]. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **P1** represents Percentage'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    serialNumber:    
      description: Serial numbers of the item    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    storableEnergy:    
      description: 'Total Storage Energy = [nominalVoltage] * [nominalCapacity]. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **KWH** represents Kilowatt Hour'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Kw Hour    
    toolBMS:    
      description: 'Use of a Battery Management System tool to protect, guarantee and optimize battery life. (`true` for yes)'    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
        type: Property    
    type:    
      description: It has to be StorageBatteryDevice    
      enum:    
        - StorageBatteryDevice    
      type: string    
      x-ngsi:    
        model: 'https://schema.org/Text '    
        type: Property    
    typeEnergySource:    
      description: 'Enum:''dam, fall, generator, network, photovoltaic, river, sea, waterTurbine, wind, other''. Type of Energy Source regarding `RechargeEnergySource` attribute'    
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
        units: Kw Hour    
    volEnergyDensity:    
      description: Volume Energy density *(Code D)*. The format is structured by a sub-property of 2 items. The unit code (text) of measurement is **Wh/L** WattHour per Liter    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Battery/blob/master/StorageBatteryDevice/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/data-models.Energy/StorageBatteryDevice/schema.json    
  x-model-tags: ""    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### StorageBatteryDevice NGSI-v2 キー値の例  
以下はStorageBatteryDeviceをJSON-LD形式でkey-valuesとした例です。これは NGSI-v2 と互換性があり、`options=keyValues` を使用すると、個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### StorageBatteryDevice NGSI-v2 正規化例  
以下は、正規化された JSON-LD フォーマットの StorageBatteryDevice の例です。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキスト・データを返します。  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### StorageBatteryDevice NGSI-LD キー値の例  
以下は、StorageBatteryDevice を JSON-LD フォーマットの key-values で表した例です。これは NGSI-LD と互換性があり、`options=keyValues` を使うと個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:StorageBatteryDevice:StorageBatteryDevice:MNCA-SBD-T1-G0-027",  
  "type": "StorageBatteryDevice",  
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
  "application": {  
    "type": "Property",  
    "value": [  
      "energyStorage",  
      "emergencyStorage"  
    ]  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Nice Aeroport"  
  },  
  "averageLife": {  
    "type": "Property",  
    "value": 15  
  },  
  "batteryType": {  
    "type": "Property",  
    "value": "Li-Ion"  
  },  
  "brandName": {  
    "type": "Property",  
    "value": "LG ELEC"  
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
  "chargeDischargeReactivity": {  
    "type": "Property",  
    "value": 0.4  
  },  
  "chargeEfficiency": {  
    "type": "Property",  
    "value": 98  
  },  
  "chargePower": {  
    "type": "Property",  
    "value": 123  
  },  
  "chargingModeAllowed": {  
    "type": "Property",  
    "value": [  
      "normal"  
    ]  
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
  "dateLastReported": {  
    "type": "Property",  
    "value": {  
      "type": "DateTime",  
      "value": "2020-03-17T08:45:00Z"  
    }  
  },  
  "description": {  
    "type": "Property",  
    "value": "Description of the Solar Storage Battery Device"  
  },  
  "dimension": {  
    "type": "Property",  
    "value": {  
      "width": 74.4,  
      "height": 90.7,  
      "depth": 20.6  
    }  
  },  
  "dischargeEfficiency": {  
    "type": "Property",  
    "value": 95  
  },  
  "dischargePower": {  
    "type": "Property",  
    "value": 96.8  
  },  
  "documentation": {  
    "type": "Property",  
    "value": "https://www.myStoragebattery.fr"  
  },  
  "durationPeakPower": {  
    "type": "Property",  
    "value": 10  
  },  
  "installationCondition": {  
    "type": "Property",  
    "value": [  
      "extremeClimate"  
    ]  
  },  
  "installationMode": {  
    "type": "Property",  
    "value": "ground"  
  },  
  "lifeCycleNumber": {  
    "type": "Property",  
    "value": {  
      "min": 600,  
      "max": 2400  
    }  
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
  "manufacturerName": {  
    "type": "Property",  
    "value": "OSCPOWER"  
  },  
  "massEnergyDensity": {  
    "type": "Property",  
    "value": {  
      "min": 30,  
      "max": 50  
    }  
  },  
  "maxOutputPower": {  
    "type": "Property",  
    "value": 12.8  
  },  
  "maximumVoltageEOC": {  
    "type": "Property",  
    "value": 48.6  
  },  
  "minimumVoltageEOD": {  
    "type": "Property",  
    "value": 47.3  
  },  
  "modelName": {  
    "type": "Property",  
    "value": "SBRESU10H"  
  },  
  "name": {  
    "type": "Property",  
    "value": "SBD-T1-G0-027"  
  },  
  "nominalAmpere": {  
    "type": "Property",  
    "value": 20  
  },  
  "nominalCapacity": {  
    "type": "Property",  
    "value": 63  
  },  
  "nominalFrequency": {  
    "type": "Property",  
    "value": 60  
  },  
  "nominalVoltage": {  
    "type": "Property",  
    "value": 48  
  },  
  "operatingAltitude": {  
    "type": "Property",  
    "value": {  
      "min": 0,  
      "max": 500  
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
  "operatingVoltage": {  
    "type": "Property",  
    "value": {  
      "min": 38.5,  
      "max": 55.0  
    }  
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
  "owners": {  
    "type": "Property",  
    "value": [  
      "Airport-Division Maintenance"  
    ]  
  },  
  "peakPower": {  
    "type": "Property",  
    "value": 5.0  
  },  
  "possibilityOfUse": {  
    "type": "Property",  
    "value": "stationary"  
  },  
  "protectionIK": {  
    "type": "Property",  
    "value": 10  
  },  
  "protectionIP": {  
    "type": "Property",  
    "value": "55"  
  },  
  "rechargeEnergySource": {  
    "type": "Property",  
    "value": "electric"  
  },  
  "roundTripEfficiency": {  
    "type": "Property",  
    "value": 96.8  
  },  
  "selfDischargeRate": {  
    "type": "Property",  
    "value": 2  
  },  
  "serialNumber": {  
    "type": "Property",  
    "value": "BSSMA10267841259"  
  },  
  "storableEnergy": {  
    "type": "Property",  
    "value": 3.025  
  },  
  "temperature": {  
    "type": "Property",  
    "value": 25  
  },  
  "toolBMS": {  
    "type": "Property",  
    "value": true  
  },  
  "typeEnergySource": {  
    "type": "Property",  
    "value": [  
      "network",  
      "photovoltaic"  
    ]  
  },  
  "typeOfUse": {  
    "type": "Property",  
    "value": "mixed"  
  },  
  "usableEnergy": {  
    "type": "Property",  
    "value": 3.012  
  },  
  "volEnergyDensity": {  
    "type": "Property",  
    "value": {  
      "min": 75,  
      "max": 120  
    }  
  },  
  "weight": {  
    "type": "Property",  
    "value": 175  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Battery/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### StorageBatteryDevice NGSI-LD 正規化例  
以下は、正規化された JSON-LD フォーマットの StorageBatteryDevice の例です。これは、オプションを使用しない場合はNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:StorageBatteryDevice:StorageBatteryDevice:MNCA-SBD-T1-G0-027",  
  "type": "StorageBatteryDevice",  
  "address": {  
    "addressCountry": "FR",  
    "addressLocality": "Nice",  
    "streetAddress": "Airport - Terminal 1 - Ground 0 - Local  27"  
  },  
  "alternateName": "AirPort \u2013 global Observation",  
  "application": [  
    "energyStorage",  
    "emergencyStorage"  
  ],  
  "areaServed": "Nice Aeroport",  
  "averageLife": 15,  
  "batteryType": "Li-Ion",  
  "brandName": "LG ELEC",  
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
  "chargeDischargeReactivity": 0.4,  
  "chargeEfficiency": 0.98,  
  "chargePower": 123,  
  "chargingModeAllowed": [  
    "normal"  
  ],  
  "communication": [  
    "CAN 2.0 B",  
    "RS485Inverter",  
    "RS485BMS",  
    "dryContactTerminal",  
    "maintenanceInterface"  
  ],  
  "dateLastReported": "2020-03-17T08:45:00Z",  
  "description": "Description of the Solar Storage Battery Device",  
  "dimension": {  
    "width": 74.4,  
    "height": 90.7,  
    "depth": 20.6  
  },  
  "dischargeEfficiency": 0.95,  
  "dischargePower": 96.8,  
  "documentation": "https://www.myStoragebattery.fr",  
  "durationPeakPower": 10,  
  "installationCondition": [  
    "extremeClimate"  
  ],  
  "installationMode": "ground",  
  "lifeCycleNumber": {  
    "min": 600,  
    "max": 2400  
  },  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      43.66481,  
      7.196545  
    ]  
  },  
  "manufacturerName": "OSCPOWER",  
  "massEnergyDensity": {  
    "min": 30,  
    "max": 50  
  },  
  "maxOutputPower": 12.8,  
  "maximumVoltageEOC": 48.6,  
  "minimumVoltageEOD": 47.3,  
  "modelName": "SBRESU10H",  
  "name": "SBD-T1-G0-027",  
  "nominalAmpere": 20,  
  "nominalCapacity": 63,  
  "nominalFrequency": 60,  
  "nominalVoltage": 48,  
  "operatingAltitude": {  
    "min": 0,  
    "max": 500  
  },  
  "operatingAmpere": {  
    "min": 1.0,  
    "max": 1.5  
  },  
  "operatingFrequency": {  
    "min": 57,  
    "max": 63  
  },  
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
  "operatingVoltage": {  
    "min": 38.5,  
    "max": 55.0  
  },  
  "overloadAccepted": true,  
  "overloadAcceptedTime": "00:00:03",  
  "owners": [  
    "Airport-Division Maintenance"  
  ],  
  "peakPower": 5.0,  
  "possibilityOfUse": "stationary",  
  "protectionIK": 10,  
  "protectionIP": "55",  
  "rechargeEnergySource": "electric",  
  "roundTripEfficiency": 0.968,  
  "selfDischargeRate": 0.02,  
  "serialNumber": "BSSMA10267841259",  
  "storableEnergy": 3.025,  
  "temperature": 25,  
  "toolBMS": true,  
  "typeEnergySource": [  
    "network",  
    "photovoltaic"  
  ],  
  "typeOfUse": "mixed",  
  "usableEnergy": 3.012,  
  "volEnergyDensity": {  
    "min": 75,  
    "max": 120  
  },  
  "weight": 175,  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Battery/master/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
