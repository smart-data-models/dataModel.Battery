<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: StorageBatteryMeasurement  
=================================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.Battery/blob/master/StorageBatteryMeasurement/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Il modello di dati osservati della batteria di stoccaggio è destinato a misurare la capacità energetica rimanente in una batteria, che può essere ridistribuita sotto forma di energia elettrica. Queste funzioni si applicano da una fonte che dipende dal tipo di batteria (riferimento all'attributo 'batteryType' del modello di dati `StorageBatteryDevice`)**.  
versione: 0.0.4  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `activePower[number]`: Potenza attiva, dove "phi" è lo sfasamento della corrente rispetto alla tensione. Il codice dell'unità di misura (testo) è indicato utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Ad esempio, **KWT** rappresenta il Kilowatt  . Model: [https://schema.org/Number](https://schema.org/Number)- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Il paese. Ad esempio, la Spagna  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La località in cui si trova l'indirizzo civico e che si trova nella regione  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel paese  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni Paesi, è gestita dal governo locale.    
	- `postOfficeBoxNumber[string]`: Il numero di casella postale per gli indirizzi di casella postale. Ad esempio, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: L'indirizzo stradale  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Numero che identifica una proprietà specifica su una strada pubblica    
- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `batteryAssessmentMethods[string]`: Metodi di valutazione e di calcolo per le misure che valutano le condizioni della batteria. Enum:'ampereOraMetria, prova di scarica, densità dell'elettrolito, impedenza ad alta frequenza, impedenza a bassa frequenza, modello matematico, tensione di esercizio con circuito chiuso, tensione di riposo con circuito aperto'.  - `batteryLevel[*]`: Livello della batteria del dispositivo. Un valore univoco del seguente valore 0.0=batteria vuota, 1.0=batteria piena, -1.0=Tranquillamente non determinato  . Model: [https://schema.org/Number](https://schema.org/Number)- `batteryStatus[string]`: Stato della batteria durante la misurazione (che fornisce o meno energia). Enum:'consumareEnergia, dareEnergia, standby'.  - `current[number]`: Corrente. Il codice dell'unità (testo) è indicato utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Ad esempio, **AMP** rappresenta gli Ampere.  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateEnergyMeteringStarted[date-time]`: La data di inizio della misurazione dell'energia in formato ISO8601 UTC.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateObserved[date-time]`: Data dell'entità osservata definita dall'utente  - `dateObservedFrom[date-time]`: Periodo di osservazione: Data e ora di inizio in formato ISO8601 UTC. Questo attributo può essere utilizzato in aggiunta all'attributo "dataOsservata" quando corrisponde a un intervallo di tempo da evidenziare.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateObservedTo[date-time]`: Periodo di osservazione: Data e ora finale in formato ISO8601 UTC. Questo attributo può essere utilizzato in aggiunta all'attributo "dataOsservata" quando corrisponde a un intervallo di tempo da evidenziare.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `deepOfDischarge[number]`: La profondità di scarica (codice DoD) espressa in % è il rapporto tra la capacità già scaricata e la capacità nominale dell'accumulatore. Vale a dire l'energia consumata nella batteria. Regola [DOD] = 100 % - [SOC]. Il codice dell'unità (testo) è indicato utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Ad esempio, **P1** rappresenta Percentuale  . Model: [https://schema.org/Number](https://schema.org/Number)- `description[string]`: Descrizione dell'articolo  - `id[*]`: Identificatore univoco dell'entità  - `inverterStatus[array]`: Stato dell'inverter. Una combinazione di valori. Enum:'00-Onsettore, 01-Mancanza di alimentazione/sulla batteria, 02-Perdita di comunicazione, 03-Anomalia della batteria, 04-Spegnimento del sistema, 05-Scadimento di tensione, 06-Sovratensione, 07-Scadimento di tensione, 08-Aumento di tensione, 09-Rumore di linea, 10-Variazione di frequenza, 11-Distorsione transitiva, 12-Distorsione armonica'.  - `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `name[string]`: Il nome di questo elemento  - `openCircuitVoltage[number]`: La tensione a vuoto (codice OCV) espressa in Volt è la differenza di potenziale elettrico tra due terminali di un dispositivo quando è scollegato da un qualsiasi circuito. Non c'è nessun carico esterno collegato e nessuna corrente elettrica esterna scorre tra i terminali. Il codice dell'unità di misura (testo) viene fornito utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Ad esempio, **VLT** rappresenta il Volt  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `reactivePower[number]`: Potenza reattiva utilizzata dai circuiti. Il codice dell'unità di misura (testo) è fornito utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Per esempio, **K5** rappresenta il kilovolt-ampere reattivo  . Model: [https://schema.org/Number](https://schema.org/Number)- `refPointOfInterest[*]`: Riferimento a un [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) collegato con il Repository  - `refStorageBatteryDevice[*]`: Riferimento a un [Storage Battery Device](https://github.com/FIWARE/data-models/blob/master/specs/Energy/StorageBatteryDevice/doc/spec.md) che ha catturato questa osservazione, se l'entità è usata  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `stateOfCharge[number]`: Lo stato di carica (codice SoC) espresso in % è definito come il rapporto tra la capacità residua e quella corrente. La capacità corrente è la capacità massima che può essere prelevata dalla batteria completamente carica in determinate condizioni di scarica. Regola [SOC] + [DOD] = 100 %. Il codice dell'unità (testo) è indicato utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Ad esempio, **P1** rappresenta la Percentuale  . Model: [https://schema.org/Number](https://schema.org/Number)- `stateOfHealth[number]`: Lo stato di salute (codice SoH) espresso in % è definito come il rapporto tra la quantità massima di carica che una batteria completamente carica può fornire nel suo regime di scarica nominale e la sua capacità nominale. Il codice dell'unità (testo) è indicato utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Ad esempio, **P1** rappresenta la Percentuale  . Model: [https://schema.org/Number](https://schema.org/Number)- `temperature[number]`: Temperatura principale registrata al momento dell'osservazione rispetto alla temperatura nominale di riferimento del dispositivo. Il codice dell'unità di misura (testo) è indicato utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Ad esempio, **CEL** rappresenta il grado Celsius.  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: Tipo di entità NGSI. Deve essere StorageBatteryMeasurement.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `dateObserved`  - `id`  - `location`  - `stateOfCharge`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
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
    dateObserved:    
      description: Date of the observed entity defined by the user    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Battery/blob/master/StorageBatteryMeasurement/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/data-models.Energy/StorageBatteryMeasurement/schema.json    
  x-model-tags: ""    
  x-version: 0.0.4    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload  
#### StorageBatteryMeasurement Valori chiave NGSI-v2 Esempio  
Ecco un esempio di StorageBatteryMeasurement in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:StorageBatteryMeasurement:StorageBatteryMeasurement:MNCA-SBM-T1-G0-027",  
  "type": "StorageBatteryMeasurement",  
  "name": "SBM-T1-G0-027",  
  "alternateName": "AirPort \u2013 global Observation",  
  "description": "Measurement of the level of Solar Storage Battery",  
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
  "dateObserved": "2020-03-17T08:45:00Z",  
  "refStorageBatteryDevice": "urn:ngsi-ld:StorageBatteryDevice:SBD-T1-G0-027",  
  "batteryLevel": -1,  
  "batteryStatus": "standby",  
  "batteryAssessmentMethods": "dischargeTest",  
  "dateEnergyMeteringStarted": "2020-03-16T10:30:00Z",  
  "stateOfCharge": 0.7,  
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
#### StorageBatteryMeasurement NGSI-v2 normalizzato Esempio  
Ecco un esempio di StorageBatteryMeasurement in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:StorageBatteryMeasurement:StorageBatteryMeasurement:MNCA-SBM-T1-G0-027",  
  "type": "StorageBatteryMeasurement",  
  "name": {  
    "type": "Text",  
    "value": "SBM-T1-G0-027"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "AirPort \u2013 global Observation"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Measurement of the level of Solar Storage Battery"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        43.66481,  
        7.196545  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "addressCountry": "FR",  
      "addressLocality": "Nice",  
      "streetAddress": "Airport - Terminal 1 - Ground 0 - Local  27"  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Nice Aeroport"  
  },  
  "dateObserved": {  
    "type": "DateTime",  
    "value": "2020-03-17T08:45:00Z"  
  },  
  "refStorageBatteryDevice": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:StorageBatteryDevice:SBD-T1-G0-027"  
  },  
  "batteryLevel": {  
    "type": "Number",  
    "value": -1  
  },  
  "batteryStatus": {  
    "type": "Text",  
    "value": "standby"  
  },  
  "batteryAssessmentMethods": {  
    "type": "Text",  
    "value": "dischargeTest"  
  },  
  "dateEnergyMeteringStarted": {  
    "type": "DateTime",  
    "value": "2020-03-16T10:30:00Z"  
  },  
  "stateOfCharge": {  
    "type": "Number",  
    "value": 0.7  
  },  
  "measurementInterval": {  
    "type": "Boolean",  
    "value": true  
  },  
  "temperature": {  
    "type": "Number",  
    "value": 25.2  
  },  
  "deepOfDischarge": {  
    "type": "Number",  
    "value": 0.286  
  },  
  "stateOfHealth": {  
    "type": "Number",  
    "value": 0.8235  
  },  
  "openCircuitVoltage": {  
    "type": "Number",  
    "value": 47.3  
  },  
  "inverterStatus": {  
    "type": "StructuredValue",  
    "value": [  
      "00-OnSector",  
      "06-OverVoltage"  
    ]  
  }  
}  
```  
</details>  
#### StorageBatteryMeasurement Valori chiave NGSI-LD Esempio  
Ecco un esempio di StorageBatteryMeasurement in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### StoccaggioBatteriaMisura NGSI-LD normalizzata Esempio  
Ecco un esempio di StorageBatteryMeasurement in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
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
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
