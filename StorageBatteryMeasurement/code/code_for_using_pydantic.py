from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import (
    AnyUrl,
    AwareDatetime,
    BaseModel,
    Field,
    RootModel,
    confloat,
    constr,
)


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class BatteryAssessmentMethods(Enum):
    ampereHourMetry = 'ampereHourMetry'
    dischargeTest = 'dischargeTest'
    electrolyteDensity = 'electrolyteDensity'
    highFrequencyImpedance = 'highFrequencyImpedance'
    lowFrequencyImpedance = 'lowFrequencyImpedance'
    mathematicalModel = 'mathematicalModel'
    operatingVoltageWithClosedCircuit = 'operatingVoltageWithClosedCircuit'
    quiescentVoltageWithOpenCircuit = 'quiescentVoltageWithOpenCircuit'


class BatteryLevel(Enum):
    number__1 = -1


class BatteryStatus(Enum):
    consumingEnergy = 'consumingEnergy'
    givingEnergy = 'givingEnergy'
    standby = 'standby'


class InverterStatu(Enum):
    field_00_OnSector = '00-OnSector'
    field_01_PowerFailure_OnBattery = '01-PowerFailure/OnBattery'
    field_02_LossCommunication = '02-LossCommunication'
    field_03_BatteryFault = '03-BatteryFault'
    field_04_SystemShutDown = '04-SystemShutDown'
    field_05_TensionDip = '05-TensionDip'
    field_06_OverVoltage = '06-OverVoltage'
    field_07_VoltageDrop = '07-VoltageDrop'
    field_08_VoltageIncrease = '08-VoltageIncrease'
    field_09_LineNoise = '09-LineNoise'
    field_10_FrequencyVariation = '10-FrequencyVariation'
    field_11_TransientDistortion = '11-TransientDistortion'
    field_12_HarmonicDistortion = '12-HarmonicDistortion'


class Type(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


class Type6(Enum):
    StorageBatteryMeasurement = 'StorageBatteryMeasurement'


class StorageBatteryMeasurement(BaseModel):
    activePower: Optional[float] = Field(
        None,
        description="Active Power, where 'phi' is the phase shift of the current compared to the voltage. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **KWT** represents Kilowatt",
    )
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    batteryAssessmentMethods: Optional[BatteryAssessmentMethods] = Field(
        None,
        description="Assessment and calculation methods for measurements assessing the condition of the battery. Enum:'ampereHourMetry, dischargeTest, electrolyteDensity, highFrequencyImpedance, lowFrequencyImpedance, mathematicalModel, operatingVoltageWithClosedCircuit, quiescentVoltageWithOpenCircuit'",
    )
    batteryLevel: Optional[Union[confloat(ge=0.0, le=1.0), BatteryLevel]] = Field(
        None,
        description="Device's battery level. A unique value of the following value 0.0=battery empty, 1.0=Battery full, -1.0=Transiently not determined",
    )
    batteryStatus: Optional[BatteryStatus] = Field(
        None,
        description="Status of the battery during the measurement( giving or not energy). Enum:'consumingEnergy, givingEnergy, standby'",
    )
    current: Optional[float] = Field(
        None,
        description='Current. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **AMP** represents Ampere. ',
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateEnergyMeteringStarted: Optional[AwareDatetime] = Field(
        None,
        description='The starting date for metering energy in an ISO8601 UTC format',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    dateObserved: Optional[AwareDatetime] = Field(
        None, description='Date of the observed entity defined by the user'
    )
    dateObservedFrom: Optional[AwareDatetime] = Field(
        None,
        description="Observation period: Start date and time in an ISO8601 UTC format. The attribute can be used in addition to the 'dateObserved' attribute when it corresponds to a time interval to be highlighted",
    )
    dateObservedTo: Optional[AwareDatetime] = Field(
        None,
        description="Observation period: End date and time in an ISO8601 UTC format. The attribute can be used in addition to the 'dateObserved' attribute when it corresponds to a time interval to be highlighted",
    )
    deepOfDischarge: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None,
        description='The Deep of Discharge (Code DoD) expressed in % is the ratio between the capacity already discharged and the nominal capacity of the accumulator. That is to say the energy consumed in the battery. Rule  [DOD] = 100 % - [SOC]. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **P1** represents Percent',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    inverterStatus: Optional[List[InverterStatu]] = Field(
        None,
        description="Status of the inverter. A combination of values. Enum:'00-Onsector, 01-PowerFailure/OnBattery, 02-LossCommunication, 03-BatteryFault, 04-SystemShutDown, 05-TensionDip, 06-OverVoltage, 07-VoltageDrop, 08-VoltageIncrease, 09-LineNoise, 10-FrequencyVariation, 11-TransientDistortion, 12-HarmonicDistortion'",
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    openCircuitVoltage: Optional[float] = Field(
        None,
        description='The Open Circuit Voltage (Code OCV) expressed in Volt is the difference of electrical potential between two terminals of a device when disconnected from any circuit. There is no external load connected and No external electric current flows between the terminals. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **VLT** represents Volt',
    )
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    reactivePower: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Reactive Power used by circuits. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **K5** represents kilovolt-ampere-reactive',
    )
    refPointOfInterest: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None,
        description='Reference to a [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) linked with the Repository',
    )
    refStorageBatteryDevice: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None,
        description='Reference to a [Storage Battery Device](https://github.com/FIWARE/data-models/blob/master/specs/Energy/StorageBatteryDevice/doc/spec.md) which captured this observation, if the entity is used',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    stateOfCharge: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None,
        description='The State of Charge (Code SoC) expressed in % is defined as the ratio between the remaining and the current capacities. The current capacity is the maximum capacity that can be withdrawn from the fully charged battery under specific discharge conditions. Rule [SOC] + [DOD] = 100 %. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **P1** represents Percent',
    )
    stateOfHealth: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None,
        description='The State of Health  (Code SoH) expressed in % is defined as the ratio between the maximum amount of charge that a fully charged battery can provide under its nominal discharge regime, and its nominal capacity. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **P1** represents Percent',
    )
    temperature: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Main Temperature recorded at the time of Observation compared to the  nominal reference temperature of the device. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **CEL** represents Degree Celsius',
    )
    type: Optional[Type6] = Field(
        None, description='NGSI Entity type. It has to be StorageBatteryMeasurement'
    )
