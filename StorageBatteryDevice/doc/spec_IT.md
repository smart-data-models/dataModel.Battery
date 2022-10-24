<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: StorageBatteryDevice  
============================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.Battery/blob/master/StorageBatteryDevice/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Il modello di dati della batteria di accumulo ha lo scopo di descrivere le caratteristiche tecniche della batteria e le condizioni di carica e scarica dell'energia **.  
versione: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nome alternativo per questa voce  - `application[array]`: Enum:'electricMobility, energyStorage, emergencyStorage, houseHoldStorage, industrialStorage, lighting, production, robotics, other'. Applicazione target del dispositivo per quanto riguarda l'accumulo. Una combinazione dell'enumerazione.  . Model: [https://schema.org/Text](https://schema.org/Text)- `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `averageLife[number]`: durata media in condizioni normali di utilizzo della batteria a temperature di riferimento. Il codice dell'unità (testo) è indicato utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Ad esempio, **ANN** rappresenta l'anno  . Model: [https://schema.org/Number](https://schema.org/Number)- `batteryAssessmentMethods[string]`: Enum:'amperometro, prova di scarica, densità dell'elettrolito, impedenza ad alta frequenza, impedenza a bassa frequenza, modello matematico, tensione di esercizio con circuito chiuso, tensione di riposo con circuito aperto'.    . Model: [https://schema.org/Text](https://schema.org/Text)- `batteryType[string]`: Enum:'alcalina, al gel, al piombo, al piombo-AGM, Li-Ion, Li-Po, Li-Po4, LMP, Li-Air, Na-NiCl2(Zebra), Ni-Cd, Ni-MH, Ni-Zn, altro'. Tipo di batteria utilizzata.  . Model: [https://schema.org/Text](https://schema.org/Text)- `brandName[string]`: Marchio dell'articolo.  . Model: [https://schema.org/Text](https://schema.org/Text)- `capacityCnnn[object]`: Energia residua in funzione del tempo di scarica per 6 chiavi alla temperatura di riferimento. Ogni chiave è un valore strutturato con il formato {`Cnnn`:[`valore1`,`valore2`]} che descrive le diverse misure di [CapacityCnnn].  . Model: [https://schema.org/Number](https://schema.org/Number)- `chargeDischargeReactivity[number]`:  Reattività di carica e scarica che caratterizza il comportamento reattivo del sistema. Il codice dell'unità (testo) viene fornito utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Ad esempio, **SEC** rappresenta i secondi  . Model: [https://schema.org/Number](https://schema.org/Number)- `chargeEfficiency[number]`: Efficienza di carica *(codice PV-BAT)*. Il codice dell'unità (testo) è indicato utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Ad esempio, **P1** rappresenta la percentuale.  . Model: [https://schema.org/Number](https://schema.org/Number)- `chargePower[number]`: Potenza di carico. Il codice dell'unità (testo) viene fornito utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Ad esempio, **VLT** rappresenta il Volt  . Model: [https://schema.org/Number](https://schema.org/Number)- `chargingModeAllowed[array]`:  Modalità di carica consentita per evitare danni alla batteria. enum:'fast, normal, quick'  . Model: [https://schema.org/Text](https://schema.org/Text)- `communication[array]`: Elenco dei protocolli di comunicazione con altri dispositivi a seconda dei produttori. Enum:'CAN 2.0 B, dryContactTerminal, maintenanceInterface, RS485, RS485BMS, RS485Inverter, altro'.  . Model: [https://schema.org/](https://schema.org/)- `dataProvider[string]`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated[string]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `dateLastReported[string]`: Un timestamp che indica l'ultima volta in cui il dispositivo ha riportato dati con successo. Data e ora in formato ISO8601 UTC.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[string]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `description[string]`: Descrizione dell'articolo  - `dimension[object]`: Dimensione esterna di un pannello. Il formato è strutturato da una sottoproprietà di 3 elementi. Il codice dell'unità di misura (testo) è fornito utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Ad esempio, **CMT** rappresenta il centimetro.  - `dischargeEfficiency[number]`: Efficienza di scarico *(codice PV-OND)*. Il codice dell'unità (testo) è indicato utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Ad esempio, **P1** rappresenta la percentuale.  . Model: [https://schema.org/Number](https://schema.org/Number)- `dischargePower[number]`: Potenza di scarica. Il codice dell'unità (testo) è indicato utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Ad esempio, **VLT** rappresenta il Volt  . Model: [https://schema.org/Number](https://schema.org/Number)- `documentation[string]`: Documentazione tecnica (installazione / manutenzione / utilizzo).  . Model: [https://schema.org/URL](https://schema.org/URL)- `durationPeakPower[number]`: Tempo di riferimento registrato per l'attributo [peakPower]. Il codice dell'unità di misura (testo) è fornito utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Ad esempio, **SEC** rappresenta i secondi  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Identificatore univoco dell'entità  - `installationCondition[array]`: Enum:'deserto, polvere, clima estremo, freddo estremo, caldo estremo, umidità estrema, marino, salino, sabbia, sismico, altro'. Condizione e possibilità di utilizzo nei seguenti ambienti.  . Model: [https://schema.org/Text](https://schema.org/Text)- `installationMode[string]`: Enum:'aerial, ground, pole, roofing, underGround, wall, other'. Posizionamento del dispositivo rispetto a un sistema di riferimento a terra.  . Model: [https://schema.org/Text](https://schema.org/Text)- `lifeCycleNumber[object]`: Numero di cicli di vita di carica/scarica ammissibili. Il formato è strutturato da una sottoproprietà di 2 voci.  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `manufacturerName[string]`: Produttore Nome dell'articolo.  . Model: [https://schema.org/Text](https://schema.org/Text)- `massEnergyDensity[object]`: Densità di energia di massa *(Codice D)*. Rapporto tra la capacità della batteria di erogare una certa potenza per un certo tempo e il suo peso. Il formato è strutturato da una sotto-proprietà di 2 elementi. Il codice dell'unità (testo) di misura è **Wh/Kg** Wattora per chilogrammo  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxOutputPower[number]`: Potenza massima. Il codice dell'unità di misura (testo) è indicato utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Ad esempio, **KWT** rappresenta il chilowatt.  . Model: [https://schema.org/Number](https://schema.org/Number)- `maximumVoltageEOC[number]`: Tensione massima autorizzata dopo la fine della carica e batteria ancora collegata a un generatore di carica. Il codice dell'unità (testo) viene fornito utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Per esempio, **VLT** rappresenta il Volt  . Model: [https://schema.org/Number](https://schema.org/Number)- `minimumVoltageEOD[number]`: Tensione minima dopo la fine della scarica e non collegata a un generatore di carica. Il codice dell'unità di misura (testo) è indicato utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Ad esempio, **VLT** rappresenta il Volt  . Model: [https://schema.org/Number](https://schema.org/Number)- `modelName[string]`: Nome del modello dell'articolo.  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: Il nome di questo elemento.  - `nominalAmpere[number]`: Amperaggio nominale. *(Codice I)*. Il codice dell'unità (testo) è indicato utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Ad esempio, **AMP** rappresenta gli Ampere  . Model: [https://schema.org/Number](https://schema.org/Number)- `nominalCapacity[number]`: Capacità energetica nominale. *(Codice C)* da collegare all'attributo [CapacityCnnn] per misurare i livelli predefiniti parametri C / xx h dei regimi di scarico. Il codice dell'unità di misura (testo) è fornito utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Ad esempio, **AMH** rappresenta l'Ampereora.  . Model: [https://schema.org/Number](https://schema.org/Number)- `nominalFrequency[number]`: Frequenza nominale. Il codice dell'unità (testo) è indicato utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Ad esempio, **HTZ** rappresenta gli Hertz.  . Model: [https://schema.org/Number](https://schema.org/Number)- `nominalVoltage[number]`: Tensione nominale della batteria. *(Codice U)* Il codice dell'unità di misura (testo) è indicato utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Ad esempio, **VLT** rappresenta il Volt  . Model: [https://schema.org/Number](https://schema.org/Number)- `operatingAltitude[object]`: Altitudine operativa con resistenza minima e massima all'altezza e alla profondità. Il formato è strutturato da una sottoproprietà di 2 elementi con le chiavi [min] =<0 e [max] >=0. Il codice dell'unità di misura (testo) è fornito utilizzando i [Codici comuni UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Ad esempio, **MTR** rappresenta il Metro  . Model: [https://schema.org/Number](https://schema.org/Number)- `operatingAmpere[object]`:  Ampere minimo e massimo consentito. Il formato è strutturato da una sottoproprietà di 2 elementi. Il codice dell'unità (testo) è fornito utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Ad esempio, **AMP** rappresenta l'Ampere  . Model: [https://schema.org/Number](https://schema.org/Number)- `operatingFrequency[object]`:  Frequenza minima e massima consentita. Il formato è strutturato da una sottoproprietà di 2 elementi. Il codice dell'unità (testo) è fornito utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Ad esempio, **HTZ** rappresenta gli Hertz.  . Model: [https://schema.org/Number](https://schema.org/Number)- `operatingTemperature[object]`: Intervallo della temperatura di funzionamento ambientale. Si tratta della resistenza minima e massima al freddo e al caldo per un [evento]. Il formato è strutturato da una sotto-proprietà di 3 elementi con il formato {`evento`:[`min`,`max`]}. Il codice dell'unità (testo) è fornito utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Ad esempio, **CEL** rappresenta il grado Celsius.  - `operatingVoltage[object]`: Tensione minima e massima consentita. Il formato è strutturato da una sottoproprietà di 2 elementi. Il codice dell'unità (testo) è fornito utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Ad esempio, **VLT** rappresenta Volt  . Model: [https://schema.org/Number](https://schema.org/Number)- `overloadAccepted[boolean]`: Il sovraccarico è consentito dopo il superamento della soglia (`true` per sì).  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `overloadAcceptedTime[string]`: Tempo di sovraccarico accettato senza danni alla batteria.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `peakPower[number]`:  Intensità massima estraibile in un breve periodo. Il codice dell'unità (testo) è indicato utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Per esempio, **KWT** rappresenta il Kilowatt  . Model: [https://schema.org/Number](https://schema.org/Number)- `possibilityOfUse[string]`: Possibilità di utilizzo. Un valore unico. Enum:'mobile, misto, fisso, altro'.    . Model: [https://schema.org/Text](https://schema.org/Text)- `protectionIK[number]`: Livello IK "Protezione mecanica" relativo alla classificazione numerica dei gradi di protezione forniti dalle custodie per apparecchiature elettriche contro gli impatti meccanici esterni, secondo lo standard della Commissione Elettrotecnica Internazionale (EN 62-262). - L'IK varia da 0 (resistenza minima) a 10 (resistenza massima) e rappresenta un'energia d'impatto (unità di misura Joule).  . Model: [https://schema.org/Number.](https://schema.org/Number.)- `protectionIP[string]`: Protezione IP *Ingresso* per la scatola di giunzione. Questo livello classifica e valuta il grado di protezione fornito dagli involucri meccanici e dalle custodie elettriche contro le intrusioni, la polvere, i contatti accidentali e l'acqua secondo lo standard della Commissione Elettrotecnica Internazionale (EN 60-529). - Prima cifra: Protezione da particelle solide (numero singolo: 0-6 o "X"). - Seconda cifra: Protezione dall'ingresso di liquidi (numero singolo: 0-9 o "X"). - Terza cifra: Protezione personale contro l'accesso a parti pericolose (lettera aggiuntiva opzionale). - Quarta cifra: Altre protezioni (lettera aggiuntiva opzionale)  . Model: [https://en.wikipedia.org/wiki/IP_Code.](https://en.wikipedia.org/wiki/IP_Code.)- `rechargeEnergySource[string]`: Enum:'elettrico, idraulico, eolico, altro'. Fonte di energia di ricarica. Un valore unico dell'elenco  . Model: [https://schema.org/Text](https://schema.org/Text)- `refDevice[*]`: Riferimento all'Entità principale [Dispositivo](https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md) se usato come secondo collegamento.  . Model: [https://schema.org/URL](https://schema.org/URL)- `refPointOfInterest[*]`: Riferimento a un [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) collegato all'osservazione.  . Model: [https://schema.org/URL](https://schema.org/URL)- `roundTripEfficiency[number]`: Efficienza di andata e ritorno. Efficienza, definita come il rapporto tra l'energia immagazzinata e l'energia restituita. Il codice dell'unità (testo) è indicato utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Ad esempio, **P1** rappresenta la percentuale.  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `selfDischargeRate[number]`: Tasso di scarica della batteria senza alcun utilizzo su una base di 1 mese in base alla [temperatura di riferimento]. Il codice dell'unità (testo) è indicato utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Ad esempio, **P1** rappresenta la percentuale.  . Model: [https://schema.org/Number](https://schema.org/Number)- `serialNumber[string]`: Numeri di serie dell'articolo.  . Model: [https://schema.org/Text](https://schema.org/Text)- `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `storableEnergy[number]`: Energia di accumulo totale = [tensione nominale] * [capacità nominale]. Il codice dell'unità di misura (testo) è fornito utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Ad esempio, **KWH** rappresenta il Kilowattora.  . Model: [https://schema.org/Number](https://schema.org/Number)- `toolBMS[boolean]`: Utilizzo di un sistema di gestione della batteria per proteggere, garantire e ottimizzare la durata della batteria. (`true` per sì)  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `type[string]`: Deve essere StorageBatteryDevice (dispositivo di archiviazione)  . Model: [https://schema.org/Text ](https://schema.org/Text )- `typeEnergySource[array]`: Enum:'diga, caduta, generatore, rete, fotovoltaico, fiume, mare, turbina ad acqua, vento, altro'. Tipo di fonte di energia per quanto riguarda l'attributo `RechargeEnergySource`.  . Model: [https://schema.org/Text](https://schema.org/Text)- `typeOfUse[string]`: Uso accettato per quanto riguarda il posizionamento in un ambiente interno/esterno. Enum:" interno, misto, esterno, altro".  . Model: [https://schema.org/Text](https://schema.org/Text)- `usableEnergy[number]`: Energia utilizzabile. Il codice dell'unità (testo) è indicato utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Ad esempio, **KWH** rappresenta il Kilowattora.  . Model: [https://schema.org/Number](https://schema.org/Number)- `volEnergyDensity[object]`: Volume Densità energetica *(Codice D)*. Il formato è strutturato da una sottoproprietà di 2 elementi. Il codice dell'unità di misura (testo) è **Wh/L** Wattora per litro  . Model: [https://schema.org/Number](https://schema.org/Number)- `weight[number]`: Peso. Il codice dell'unità (testo) è indicato utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Ad esempio, **KGM** rappresenta il chilo-grammo.  . Model: [https://schema.org/weight](https://schema.org/weight)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `batteryType`  - `dateLastReported`  - `id`  - `location`  - `rechargeEnergySource`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Le funzionalità di ricarica si applicano da una fonte di alimentazione che può essere un "sistema di bordo, un pannello solare, una turbina eolica, un generatore, un alimentatore". Le fonti idrauliche non sono incluse in questa versione. Le funzioni di scarica si applicano a tutti i tipi di sistemi che richiedono il consumo di energia da una batteria di accumulo. *Questo modello di dati può essere utilizzato direttamente come entità principale per descrivere il dispositivo *Batteria di accumulo* o come sotto-entità del modello di dati *DEVICE* utilizzando un riferimento tramite l'attributo *refDevice*.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
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
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload  
#### StorageBatteryDevice Valori chiave NGSI-v2 Esempio  
Ecco un esempio di StorageBatteryDevice in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### StorageBatteryDevice NGSI-v2 normalizzato Esempio  
Ecco un esempio di StorageBatteryDevice in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
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
#### StorageBatteryDevice Valori chiave NGSI-LD Esempio  
Ecco un esempio di StorageBatteryDevice in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### StorageBatteryDevice NGSI-LD normalizzato Esempio  
Ecco un esempio di StorageBatteryDevice in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
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
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
