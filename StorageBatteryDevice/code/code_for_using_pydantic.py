from __future__ import annotations

from datetime import time
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


class ApplicationEnum(Enum):
    electricMobility = 'electricMobility'
    energyStorage = 'energyStorage'
    emergencyStorage = 'emergencyStorage'
    houseHoldStorage = 'houseHoldStorage'
    industrialStorage = 'industrialStorage'
    lighting = 'lighting'
    production = 'production'
    robotics = 'robotics'
    other = 'other'


class BatteryAssessmentMethods(Enum):
    ampereHourMeter = 'ampereHourMeter'
    dischargeTest = 'dischargeTest'
    electrolyteDensity = 'electrolyteDensity'
    highFrequencyImpedance = 'highFrequencyImpedance'
    lowFrequencyImpedance = 'lowFrequencyImpedance'
    mathematicalModel = 'mathematicalModel'
    operatingVoltageWithClosedCircuit = 'operatingVoltageWithClosedCircuit'
    quiescentVoltageWithOpenCircuit = 'quiescentVoltageWithOpenCircuit'


class BatteryType(Enum):
    alkaline = 'alkaline'
    gel = 'gel'
    lead = 'lead'
    lead_AGM = 'lead-AGM'
    Li_Ion = 'Li-Ion'
    Li_Po = 'Li-Po'
    Li_Po4 = 'Li-Po4'
    LMP = 'LMP'
    Li_Air = 'Li-Air'
    Na_NiCl2_Zebra_ = 'Na-NiCl2(Zebra)'
    Ni_Cd = 'Ni-Cd'
    Ni_MH = 'Ni-MH'
    Ni_Zn = 'Ni-Zn'
    other = 'other'


class CapacityCnnn(BaseModel):
    C001: Optional[List[float]] = None
    C005: Optional[List[float]] = None
    C010: Optional[List[float]] = None
    C020: Optional[List[float]] = None
    C050: Optional[List[float]] = None
    C100: Optional[List[float]] = None


class ChargingModeAllowedEnum(Enum):
    normal = 'normal'
    quick = 'quick'
    fast = 'fast'


class CommunicationEnum(Enum):
    CAN_2_0_B = 'CAN 2.0 B'
    dryContactTerminal = 'dryContactTerminal'
    maintenanceInterface = 'maintenanceInterface'
    RS485 = 'RS485'
    RS485BMS = 'RS485BMS'
    RS485Inverter = 'RS485Inverter'
    other = 'other'


class Dimension(BaseModel):
    depth: Optional[confloat(ge=0.0)] = None
    height: Optional[confloat(ge=0.0)] = None
    width: Optional[confloat(ge=0.0)] = None


class InstallationConditionEnum(Enum):
    desert = 'desert'
    dust = 'dust'
    extremeClimate = 'extremeClimate'
    extremeCold = 'extremeCold'
    extremeHeat = 'extremeHeat'
    extremeHumidity = 'extremeHumidity'
    marine = 'marine'
    saline = 'saline'
    sand = 'sand'
    seismic = 'seismic'
    other = 'other'


class InstallationMode(Enum):
    aerial = 'aerial'
    ground = 'ground'
    pole = 'pole'
    roofing = 'roofing'
    underGround = 'underGround'
    wall = 'wall'
    other = 'other'


class LifeCycleNumber(BaseModel):
    max: Optional[confloat(ge=0.0)] = None
    min: Optional[confloat(ge=0.0)] = None


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


class MassEnergyDensity(BaseModel):
    max: Optional[confloat(ge=0.0)] = None
    min: Optional[confloat(ge=0.0)] = None


class OperatingAltitude(BaseModel):
    max: Optional[confloat(ge=0.0)] = None
    min: Optional[confloat(ge=0.0)] = None


class OperatingAmpere(BaseModel):
    max: Optional[confloat(ge=0.0)] = None
    min: Optional[confloat(ge=0.0)] = None


class OperatingFrequency(BaseModel):
    max: Optional[confloat(ge=0.0)] = None
    min: Optional[confloat(ge=0.0)] = None


class OperatingTemperature(BaseModel):
    charge: Optional[List[float]] = Field(None, description='Charge of the item')
    discharge: Optional[List[float]] = Field(None, description='Discharge of the item ')
    storage: Optional[List[float]] = Field(None, description='Storage of the item')


class OperatingVoltage(BaseModel):
    max: Optional[confloat(ge=0.0)] = None
    min: Optional[confloat(ge=0.0)] = None


class PossibilityOfUse(Enum):
    mobile = 'mobile'
    mixed = 'mixed'
    stationary = 'stationary'
    other = 'other'


class RechargeEnergySource(Enum):
    electric = 'electric'
    hydraulic = 'hydraulic'
    windTurbine = 'windTurbine'
    other = 'other'


class Type6(Enum):
    StorageBatteryDevice = 'StorageBatteryDevice'


class TypeEnergySourceEnum(Enum):
    dam = 'dam'
    fall = 'fall'
    generator = 'generator'
    network = 'network'
    photovoltaic = 'photovoltaic'
    river = 'river'
    sea = 'sea'
    waterTurbine = 'waterTurbine'
    wind = 'wind'
    other = 'other'


class TypeOfUse(Enum):
    indoor = 'indoor'
    mixed = 'mixed'
    outdoor = 'outdoor'
    other = 'other'


class VolEnergyDensity(BaseModel):
    max: Optional[confloat(ge=0.0)] = None
    min: Optional[confloat(ge=0.0)] = None


class StorageBatteryDevice(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    application: Optional[List[ApplicationEnum]] = Field(
        None,
        description="Enum:'electricMobility, energyStorage, emergencyStorage, houseHoldStorage, industrialStorage, lighting, production, robotics, other'. Target application of the Device regarding the storage. A combination of the enumeration",
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    averageLife: Optional[float] = Field(
        None,
        description='average life under normal battery usage conditions at reference temperatures. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **ANN** represents Year',
    )
    batteryAssessmentMethods: Optional[BatteryAssessmentMethods] = Field(
        None,
        description="Enum:'ampereHourMeter, dischargeTest, electrolyteDensity, highFrequencyImpedance, lowFrequencyImpedance, mathematicalModel, operatingVoltageWithClosedCircuit, quiescentVoltageWithOpenCircuit'.  ",
    )
    batteryType: Optional[BatteryType] = Field(
        None,
        description="Enum:'alkaline, gel, lead, lead-AGM, Li-Ion, Li-Po, Li-Po4, LMP, Li-Air, Na-NiCl2(Zebra), Ni-Cd, Ni-MH, Ni-Zn, other'. Type of battery used",
    )
    brandName: Optional[str] = Field(None, description='Brand Name of the item')
    capacityCnnn: Optional[CapacityCnnn] = Field(
        None,
        description='Remaining energy as a function of the discharge time for 6 keys according the temperature of reference. Each Key is a structured value with the format {`Cnnn`:[`value1`,`value2`]} describing the different measurement of [CapacityCnnn]',
    )
    chargeDischargeReactivity: Optional[float] = Field(
        None,
        description=' Charge and Discharge Reactivity which characterizes the reactive behavior of the system. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **SEC** represents Second',
    )
    chargeEfficiency: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None,
        description='Charge Efficiency *(code PV-BAT)*. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **P1** represents Percent',
    )
    chargePower: Optional[float] = Field(
        None,
        description='Load Power. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **VLT** represents Volt',
    )
    chargingModeAllowed: Optional[List[ChargingModeAllowedEnum]] = Field(
        None,
        description=" Charging mode permitted to avoid damage to the battery. enum:'fast, normal, quick'",
    )
    communication: Optional[List[CommunicationEnum]] = Field(
        None,
        description="List of communication protocol with others device depending manufacturers. Enum:'CAN 2.0 B, dryContactTerminal, maintenanceInterface, RS485, RS485BMS, RS485Inverter, other'",
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateLastReported: Optional[AwareDatetime] = Field(
        None,
        description='A timestamp which denotes the last time when the device successfully reported data. Date and time in an ISO8601 UTCformat. ',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    dimension: Optional[Dimension] = Field(
        None,
        description='External dimension of a Panel. The format is structured by a sub-property of 3 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **CMT** represents Centimeter',
    )
    dischargeEfficiency: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None,
        description='Discharge Efficiency *(code PV-OND)*. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **P1** represents Percent',
    )
    dischargePower: Optional[float] = Field(
        None,
        description='Discharge Power. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **VLT** represents Volt',
    )
    documentation: Optional[str] = Field(
        None, description='Technical Documentation (Installation / maintenance / use)'
    )
    durationPeakPower: Optional[float] = Field(
        None,
        description='Reference Time recorded for the attribute [peakPower]. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **SEC** represents Second',
    )
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
    installationCondition: Optional[List[InstallationConditionEnum]] = Field(
        None,
        description="Enum:'desert, dust, extremeClimate, extremeCold, extremeHeat, extremeHumidity, marine, saline, sand, seismic, other'. Condition and possibility of use in the following environments",
    )
    installationMode: Optional[InstallationMode] = Field(
        None,
        description="Enum:'aerial, ground, pole, roofing, underGround, wall, other'. Positioning of the device in relation to a ground reference system",
    )
    lifeCycleNumber: Optional[LifeCycleNumber] = Field(
        None,
        description='Number of admissible charge / discharge life cycles. The format is structured by a sub-property of 2 items',
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    manufacturerName: Optional[str] = Field(
        None, description='Manufacturer Name of the item'
    )
    massEnergyDensity: Optional[MassEnergyDensity] = Field(
        None,
        description='Mass Energy density *(Code D)*. Ratio between the capacity of the battery to deliver a certain power for a certain time and its weight. The format is structured by a sub-property of 2 items. The unit code (text) of measurement is **Wh/Kg** WattHour per Kilogram',
    )
    maxOutputPower: Optional[float] = Field(
        None,
        description='Maximum Power. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **KWT** represents Kilowatt',
    )
    maximumVoltageEOC: Optional[float] = Field(
        None,
        description='Maximum authorized voltage after end of charge and Battery still connected to to a charge generator. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **VLT** represents Volt',
    )
    minimumVoltageEOD: Optional[float] = Field(
        None,
        description='Minimum voltage after end of discharge and not connected to to a charge generator. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **VLT** represents Volt',
    )
    modelName: Optional[str] = Field(None, description='Model Name of the item. ')
    name: Optional[str] = Field(None, description='The name of this item')
    nominalAmpere: Optional[float] = Field(
        None,
        description='Nominal Amperage. *(Code I)*. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **AMP** represents Ampere',
    )
    nominalCapacity: Optional[float] = Field(
        None,
        description='Nominal Energy capacity. *(Code C)* to link with the attribute [CapacityCnnn] to measure the predefined levels parameters C / xx h of discharge regimes. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **AMH** represents Ampere Hour',
    )
    nominalFrequency: Optional[float] = Field(
        None,
        description='Nominal Frequency. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **HTZ** represents Hertz',
    )
    nominalVoltage: Optional[float] = Field(
        None,
        description='Nominal battery voltage. *(Code U)* The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **VLT** represents Volt',
    )
    operatingAltitude: Optional[OperatingAltitude] = Field(
        None,
        description='Operating altitude with minimum and maximum resistance to height and depth. The format is structured by a sub-property of 2 items with the keys [min] =<0 and [max] >=0. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **MTR** represents Meter',
    )
    operatingAmpere: Optional[OperatingAmpere] = Field(
        None,
        description=' Minimum and Maximum Ampere allowed. The format is structured by a sub-property of 2 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **AMP** represents Ampere',
    )
    operatingFrequency: Optional[OperatingFrequency] = Field(
        None,
        description=' Minimum and Maximum frequency allowed. The format is structured by a sub-property of 2 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **HTZ** represents Hertz',
    )
    operatingTemperature: Optional[OperatingTemperature] = Field(
        None,
        description='Ambient operating temperature range. This is the minimum and maximum resistance to cold and heat for an [event]. The format is structured by a sub-property of 3 items with the format  {`event`:[`min`,`max`]}. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **CEL** represents Degree Celsius',
    )
    operatingVoltage: Optional[OperatingVoltage] = Field(
        None,
        description='Minimum and Maximum voltage allowed. The format is structured by a sub-property of 2 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **VLT** represents Volt',
    )
    overloadAccepted: Optional[bool] = Field(
        None,
        description='Overload is permitted after exceeding the threshold.(`true` for yes)',
    )
    overloadAcceptedTime: Optional[time] = Field(
        None, description='Accepted overcharge time without damage to the battery'
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
    peakPower: Optional[float] = Field(
        None,
        description=' Maximum intensity extractable over a short period. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **KWT** represents Kilowatt',
    )
    possibilityOfUse: Optional[PossibilityOfUse] = Field(
        None,
        description="Possibility of use. A unique value. Enum:'mobile, mixed, stationary, other'.  ",
    )
    protectionIK: Optional[float] = Field(
        None,
        description="IK 'Mecanic Protection' level relating to numeric classification for the degrees of protection provided by enclosures for electrical equipment against external mechanical impacts, according to International Electro technical Commission standard (EN 62-262). - IK varies from 0 (minimum resistance) to 10 (maximum resistance) which represents an Impact Energy (Unit Joule)",
    )
    protectionIP: Optional[str] = Field(
        None,
        description="IP *Ingress Protection* for the Junction Box. This is the level classifies and rates the degree of protection provided by mechanical casings and electrical enclosures against intrusion, dust, accidental contact, and water according to International Electrotechnical Commission standard (EN 60-529). - First digit: Solid particle protection (Single numeral: 0–6 or 'X'). - Second digit: Liquid ingress protection (Single numeral: 0–9 or 'X'). - Third digit: Personal Protection  against access to dangerous parts (optional additional letter). - Fourth digit: Other protections (optional additional letter)",
    )
    rechargeEnergySource: Optional[RechargeEnergySource] = Field(
        None,
        description="Enum:'electric, hydraulic, windTurbine, other'. Recharge Energy Source. A unique value of the list ",
    )
    refDevice: Optional[
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
        description='Reference to the Main Entity [Device](https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md) if used as second link',
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
        description='Reference to a [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) linked with the observation',
    )
    roundTripEfficiency: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None,
        description='Round-Trip Efficiency. Efficiency, defined as the ratio between stored energy and returned energy. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **P1** represents Percent',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    selfDischargeRate: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None,
        description='Battery discharge rate without any use on a baseline of 1 month according the [temperature of reference]. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **P1** represents Percentage',
    )
    serialNumber: Optional[str] = Field(None, description='Serial numbers of the item')
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    storableEnergy: Optional[float] = Field(
        None,
        description='Total Storage Energy = [nominalVoltage] * [nominalCapacity]. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **KWH** represents Kilowatt Hour',
    )
    toolBMS: Optional[bool] = Field(
        None,
        description='Use of a Battery Management System tool to protect, guarantee and optimize battery life. (`true` for yes)',
    )
    type: Optional[Type6] = Field(None, description='It has to be StorageBatteryDevice')
    typeEnergySource: Optional[List[TypeEnergySourceEnum]] = Field(
        None,
        description="Enum:'dam, fall, generator, network, photovoltaic, river, sea, waterTurbine, wind, other'. Type of Energy Source regarding `RechargeEnergySource` attribute",
    )
    typeOfUse: Optional[TypeOfUse] = Field(
        None,
        description="Accepted use regarding its positioning in an indoor / outdoor environment. Enum:' indoor, mixed, outdoor, other'",
    )
    usableEnergy: Optional[float] = Field(
        None,
        description='Usable Energy. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **KWH** represents Kilowatt Hour',
    )
    volEnergyDensity: Optional[VolEnergyDensity] = Field(
        None,
        description='Volume Energy density *(Code D)*. The format is structured by a sub-property of 2 items. The unit code (text) of measurement is **Wh/L** WattHour per Liter',
    )
    weight: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Weight. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **KGM** represents KiloGramme',
    )
