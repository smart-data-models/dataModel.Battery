<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: StorageBatteryDevice  
=============================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Battery/blob/master/StorageBatteryDevice/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Das Datenmodell für Batteriespeicher dient der Beschreibung der technischen Merkmale der Batterie und der Lade- und Entladebedingungen der Energie**.  
Version: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, liegt das daran, dass es mehrere Typen oder unterschiedliche Formate/Muster haben kann</sub></sup>.  
- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `application[array]`: Enum:'electricMobility, energyStorage, emergencyStorage, houseHoldStorage, industrialStorage, lighting, production, robotics, other'. Zielanwendung des Geräts in Bezug auf die Speicherung. Eine Kombination aus der Aufzählung.  . Model: [https://schema.org/Text](https://schema.org/Text)- `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `averageLife[number]`: durchschnittliche Lebensdauer unter normalen Nutzungsbedingungen der Batterie bei Referenztemperaturen. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **ANN** für Jahr  . Model: [https://schema.org/Number](https://schema.org/Number)- `batteryAssessmentMethods[string]`: Enum:'ampereHourMeter, dischargeTest, electrolyteDensity, highFrequencyImpedance, lowFrequencyImpedance, mathematicalModel, operatingVoltageWithClosedCircuit, quiescentVoltageWithOpenCircuit'.    . Model: [https://schema.org/Text](https://schema.org/Text)- `batteryType[string]`: Enum:'Alkali, Gel, Blei, Blei-AGM, Li-Ion, Li-Po, Li-Po4, LMP, Li-Air, Na-NiCl2(Zebra), Ni-Cd, Ni-MH, Ni-Zn, andere'. Typ der verwendeten Batterie.  . Model: [https://schema.org/Text](https://schema.org/Text)- `brandName[string]`: Markenname des Artikels.  . Model: [https://schema.org/Text](https://schema.org/Text)- `capacityCnnn[object]`: Verbleibende Energie in Abhängigkeit von der Entladezeit für 6 Schlüssel entsprechend der Referenztemperatur. Jeder Schlüssel ist ein strukturierter Wert mit dem Format {`Cnnn`:[`Wert1`,`Wert2`]}, der die verschiedenen Messungen von [KapazitätCnnn] beschreibt.  . Model: [https://schema.org/Number](https://schema.org/Number)- `chargeDischargeReactivity[number]`:  Ladungs- und Entladungsreaktivität, die das reaktive Verhalten des Systems charakterisiert. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **SEC** für Second  . Model: [https://schema.org/Number](https://schema.org/Number)- `chargeEfficiency[number]`: Ladungswirkungsgrad *(Code PV-BAT)*. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **P1** für Prozent.  . Model: [https://schema.org/Number](https://schema.org/Number)- `chargePower[number]`: Leistung laden. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **VLT** für Volt  . Model: [https://schema.org/Number](https://schema.org/Number)- `chargingModeAllowed[array]`:  Zulässiger Lademodus, um Schäden an der Batterie zu vermeiden. enum:'fast, normal, quick'  . Model: [https://schema.org/Text](https://schema.org/Text)- `communication[array]`: Liste der Kommunikationsprotokolle mit anderen Geräten je nach Hersteller. Enum:'CAN 2.0 B, dryContactTerminal, maintenanceInterface, RS485, RS485BMS, RS485Inverter, other'  . Model: [https://schema.org/](https://schema.org/)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated[string]`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateLastReported[string]`: Ein Zeitstempel, der den letzten Zeitpunkt angibt, zu dem das Gerät erfolgreich Daten gemeldet hat. Datum und Uhrzeit im ISO8601 UTC-Format.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[string]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description[string]`: Eine Beschreibung dieses Artikels  - `dimension[object]`: Externe Dimension eines Panels. Das Format ist durch eine Untereigenschaft mit 3 Elementen strukturiert. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **CMT** für Zentimeter  - `dischargeEfficiency[number]`: Entladungswirkungsgrad *(Code PV-OND)*. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **P1** für Prozent.  . Model: [https://schema.org/Number](https://schema.org/Number)- `dischargePower[number]`: Entladungsleistung. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **VLT** für Volt  . Model: [https://schema.org/Number](https://schema.org/Number)- `documentation[string]`: Technische Dokumentation (Installation / Wartung / Nutzung).  . Model: [https://schema.org/URL](https://schema.org/URL)- `durationPeakPower[number]`: Referenzzeit, die für das Attribut [peakPower] aufgezeichnet wurde. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **SEC** für Sekunde  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Eindeutiger Bezeichner der Entität  - `installationCondition[array]`: Enum:'Wüste, Staub, extremesKlima, extremeKälte, extremeHitze, extremeFeuchtigkeit, Meer, Salz, Sand, seismisch, andere'. Bedingung und Möglichkeit der Verwendung in den folgenden Umgebungen.  . Model: [https://schema.org/Text](https://schema.org/Text)- `installationMode[string]`: Enum:'aerial, ground, pole, roofing, underGround, wall, other'. Positionierung des Geräts im Verhältnis zu einem Bodenbezugssystem.  . Model: [https://schema.org/Text](https://schema.org/Text)- `lifeCycleNumber[object]`: Anzahl der zulässigen Lade-/Entladelebenszyklen. Das Format ist durch eine Untereigenschaft von 2 Elementen strukturiert.  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `manufacturerName[string]`: Hersteller Name des Artikels.  . Model: [https://schema.org/Text](https://schema.org/Text)- `massEnergyDensity[object]`: Masse Energiedichte *(Code D)*. Verhältnis zwischen der Kapazität der Batterie, eine bestimmte Leistung für eine bestimmte Zeit zu liefern, und ihrem Gewicht. Das Format ist durch eine Untereigenschaft mit 2 Elementen strukturiert. Der Code der Maßeinheit (Text) ist **Wh/Kg** Wattstunde pro Kilogramm  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxOutputPower[number]`: Maximale Leistung. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **KWT** für Kilowatt  . Model: [https://schema.org/Number](https://schema.org/Number)- `maximumVoltageEOC[number]`: Maximal zulässige Spannung nach Beendigung des Ladevorgangs und wenn die Batterie noch an einen Ladegenerator angeschlossen ist. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **VLT** für Volt  . Model: [https://schema.org/Number](https://schema.org/Number)- `minimumVoltageEOD[number]`: Mindestspannung nach Ende der Entladung und ohne Anschluss an einen Aufladegenerator. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **VLT** für Volt  . Model: [https://schema.org/Number](https://schema.org/Number)- `modelName[string]`: Modell Name des Artikels.  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: Der Name dieses Artikels.  - `nominalAmpere[number]`: Nenn-Stromstärke. *(Code I)*. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **AMP** für Ampere  . Model: [https://schema.org/Number](https://schema.org/Number)- `nominalCapacity[number]`: Nominale Energiekapazität. *(Code C)* zur Verknüpfung mit dem Attribut [CapacityCnnn] zur Messung der vordefinierten Niveauparameter C / xx h des Entladungsregimes. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **AMH** für Ampere-Stunden  . Model: [https://schema.org/Number](https://schema.org/Number)- `nominalFrequency[number]`: Nennfrequenz. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **HTZ** für Hertz  . Model: [https://schema.org/Number](https://schema.org/Number)- `nominalVoltage[number]`: Nennspannung der Batterie. *(Code U)* Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **VLT** für Volt  . Model: [https://schema.org/Number](https://schema.org/Number)- `operatingAltitude[object]`: Betriebshöhe mit minimalem und maximalem Widerstand gegen Höhe und Tiefe. Das Format ist durch eine Untereigenschaft von 2 Elementen mit den Schlüsseln [min] =<0 und [max] >=0 strukturiert. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **MTR** für Meter  . Model: [https://schema.org/Number](https://schema.org/Number)- `operatingAmpere[object]`:  Zulässige Mindest- und Höchststromstärke. Das Format ist durch eine Untereigenschaft mit 2 Elementen strukturiert. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **AMP** für Ampere  . Model: [https://schema.org/Number](https://schema.org/Number)- `operatingFrequency[object]`:  Zulässige Mindest- und Höchsthäufigkeit. Das Format ist durch eine Untereigenschaft mit 2 Elementen strukturiert. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **HTZ** für Hertz  . Model: [https://schema.org/Number](https://schema.org/Number)- `operatingTemperature[object]`: Betriebstemperaturbereich der Umgebung. Dies ist der minimale und maximale Widerstand gegen Kälte und Hitze für ein [Ereignis]. Das Format ist durch eine Untereigenschaft von 3 Elementen im Format {`Ereignis`:[`min`,`max`]} strukturiert. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **CEL** für Grad Celsius  - `operatingVoltage[object]`: Zulässige Mindest- und Höchstspannung. Das Format ist durch eine Untereigenschaft mit 2 Elementen strukturiert. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **VLT** für Volt  . Model: [https://schema.org/Number](https://schema.org/Number)- `overloadAccepted[boolean]`: Überlastung ist nach Überschreiten des Schwellenwerts erlaubt (`true` für yes)  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `overloadAcceptedTime[string]`: Akzeptierte Überladezeit ohne Beschädigung des Akkus.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `peakPower[number]`:  Maximale Intensität, die über einen kurzen Zeitraum extrahiert werden kann. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **KWT** für Kilowatt  . Model: [https://schema.org/Number](https://schema.org/Number)- `possibilityOfUse[string]`: Die Möglichkeit der Nutzung. Ein eindeutiger Wert. Enum:'mobil, gemischt, stationär, andere'.    . Model: [https://schema.org/Text](https://schema.org/Text)- `protectionIK[number]`: IK 'Mecanic Protection' (mechanischer Schutz) ist eine numerische Klassifizierung für den Schutzgrad von Gehäusen für elektrische Geräte gegen äußere mechanische Einwirkungen gemäß der Norm der Internationalen Elektrotechnischen Kommission (EN 62-262). - IK reicht von 0 (minimaler Widerstand) bis 10 (maximaler Widerstand), was einer Schlagenergie (Einheit Joule) entspricht  . Model: [https://schema.org/Number.](https://schema.org/Number.)- `protectionIP[string]`: IP *Eindringschutz* für die Anschlussdose. Diese Stufe klassifiziert und bewertet den Grad des Schutzes, den mechanische und elektrische Gehäuse gegen Eindringen, Staub, zufällige Berührung und Wasser gemäß der Norm der Internationalen Elektrotechnischen Kommission (EN 60-529) bieten. - Erste Ziffer: Schutz gegen feste Partikel (einzelne Ziffer: 0-6 oder 'X'). - Zweite Ziffer: Schutz gegen Eindringen von Flüssigkeiten (Einzelne Ziffer: 0-9 oder 'X'). - Dritte Ziffer: Personenschutz gegen den Zugang zu gefährlichen Teilen (optionaler Zusatzbuchstabe). - Vierte Ziffer: Sonstige Schutzmaßnahmen (optionaler Zusatzbuchstabe)  . Model: [https://en.wikipedia.org/wiki/IP_Code.](https://en.wikipedia.org/wiki/IP_Code.)- `rechargeEnergySource[string]`: Enum:'elektrisch, hydraulisch, Windturbine, andere'. Energiequelle aufladen. Ein eindeutiger Wert aus der Liste  . Model: [https://schema.org/Text](https://schema.org/Text)- `refDevice[*]`: Verweis auf die Haupteinheit [Gerät] (https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md) bei Verwendung als zweite Verbindung.  . Model: [https://schema.org/URL](https://schema.org/URL)- `refPointOfInterest[*]`: Verweis auf einen [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md), der mit der Beobachtung verknüpft ist.  . Model: [https://schema.org/URL](https://schema.org/URL)- `roundTripEfficiency[number]`: Wirkungsgrad der Hin- und Rückfahrt. Wirkungsgrad, definiert als das Verhältnis zwischen gespeicherter Energie und zurückgegebener Energie. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **P1** für Prozent.  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `selfDischargeRate[number]`: Entladungsrate der Batterie ohne jegliche Nutzung bei einer Basislinie von 1 Monat gemäß der [Referenztemperatur]. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **P1** für den Prozentsatz.  . Model: [https://schema.org/Number](https://schema.org/Number)- `serialNumber[string]`: Seriennummern des Artikels.  . Model: [https://schema.org/Text](https://schema.org/Text)- `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Es wird empfohlen, den voll qualifizierten Domänennamen des Quellanbieters oder die URL des Quellobjekts zu verwenden.  - `storableEnergy[number]`: Gesamtspeichernergie = [NennSpannung] * [NennKapazität]. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **KWH** für Kilowattstunde  . Model: [https://schema.org/Number](https://schema.org/Number)- `toolBMS[boolean]`: Verwendung eines Batteriemanagementsystems zum Schutz, zur Gewährleistung und zur Optimierung der Batterielebensdauer. (`true` für ja)  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `type[string]`: Es muss StorageBatteryDevice sein  . Model: [https://schema.org/Text ](https://schema.org/Text )- `typeEnergySource[array]`: Enum:'Staudamm, Wasserfall, Generator, Netz, Photovoltaik, Fluss, Meer, Wasserturbine, Wind, andere'. Art der Energiequelle in Bezug auf das Attribut `RechargeEnergySource`.  . Model: [https://schema.org/Text](https://schema.org/Text)- `typeOfUse[string]`: Akzeptierte Verwendung hinsichtlich der Positionierung in einer Innen-/Außenumgebung. Enum:' innen, gemischt, außen, andere'  . Model: [https://schema.org/Text](https://schema.org/Text)- `usableEnergy[number]`: Nutzbare Energie. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **KWH** für Kilowattstunde  . Model: [https://schema.org/Number](https://schema.org/Number)- `volEnergyDensity[object]`: Volumen Energiedichte *(Code D)*. Das Format ist durch eine Untereigenschaft mit 2 Elementen strukturiert. Der Code der Maßeinheit (Text) ist **Wh/L** Wattstunde pro Liter  . Model: [https://schema.org/Number](https://schema.org/Number)- `weight[number]`: Gewicht. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **KGM** für KiloGramme  . Model: [https://schema.org/weight](https://schema.org/weight)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- `batteryType`  - `dateLastReported`  - `id`  - `location`  - `rechargeEnergySource`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Die Ladefunktionen gelten für eine Stromquelle, bei der es sich um ein "bordseitiges System, ein Solarpanel, eine Windturbine, einen Generator oder eine Stromversorgung" handeln kann. Hydraulische Quellen sind in dieser Version nicht enthalten. Die Entladefunktionen gelten für alle Arten von Systemen, die eine Energieentnahme aus einem Akkumulator erfordern. *Bemerkung* Dieses Datenmodell kann direkt als Hauptentität zur Beschreibung des Geräts *Batteriespeicher* oder als Unterentität des Datenmodells *DEVICE* unter Verwendung einer Referenz durch das Attribut *refDevice* verwendet werden.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
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
        - description: 'GeoProperty. Geojson reference to the item. Point'    
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
        - description: 'GeoProperty. Geojson reference to the item. LineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. Polygon'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiPoint'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        type: GeoProperty    
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
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
#### StorageBatteryDevice NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für ein StorageBatteryDevice im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
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
#### SpeicherBatterieGerät NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für ein StorageBatteryDevice im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
#### StorageBatteryDevice NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für ein StorageBatteryDevice im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
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
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Battery/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### SpeicherBatterieGerät NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für ein StorageBatteryDevice im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-LD kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
