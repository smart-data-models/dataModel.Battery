/* (Beta) Export of data model StorageBatteryDevice of the subject dataModel.Battery for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE batteryAssessmentMethods_type AS ENUM ('ampereHourMeter', 'dischargeTest', 'electrolyteDensity', 'highFrequencyImpedance', 'lowFrequencyImpedance', 'mathematicalModel', 'operatingVoltageWithClosedCircuit', 'quiescentVoltageWithOpenCircuit');CREATE TYPE batteryType_type AS ENUM ('alkaline', 'gel', 'lead', 'lead-AGM', 'Li-Ion', 'Li-Po', 'Li-Po4', 'LMP', 'Li-Air', 'Na-NiCl2(Zebra)', 'Ni-Cd', 'Ni-MH', 'Ni-Zn', 'other');CREATE TYPE installationMode_type AS ENUM ('aerial', 'ground', 'pole', 'roofing', 'underGround', 'wall', 'other');CREATE TYPE possibilityOfUse_type AS ENUM ('mobile', 'mixed', 'stationary', 'other');CREATE TYPE rechargeEnergySource_type AS ENUM ('electric', 'hydraulic', 'windTurbine', 'other');CREATE TYPE StorageBatteryDevice_type AS ENUM ('StorageBatteryDevice');CREATE TYPE typeOfUse_type AS ENUM ('indoor', 'mixed', 'outdoor', 'other');
CREATE TABLE StorageBatteryDevice (address json, alternateName text, application json, areaServed text, averageLife text, batteryAssessmentMethods batteryAssessmentMethods_type, batteryType batteryType_type, brandName text, capacityCnnn json, chargeDischargeReactivity text, chargeEfficiency text, chargePower text, chargingModeAllowed json, communication json, dataProvider text, dateCreated timestamp, dateLastReported timestamp, dateModified timestamp, description text, dimension json, dischargeEfficiency text, dischargePower text, documentation text, durationPeakPower text, id text, installationCondition json, installationMode installationMode_type, lifeCycleNumber json, location json, manufacturerName text, massEnergyDensity json, maxOutputPower text, maximumVoltageEOC text, minimumVoltageEOD text, modelName text, name text, nominalAmpere text, nominalCapacity text, nominalFrequency text, nominalVoltage text, operatingAltitude json, operatingAmpere json, operatingFrequency json, operatingTemperature json, operatingVoltage json, overloadAccepted text, overloadAcceptedTime time, owner json, peakPower text, possibilityOfUse possibilityOfUse_type, protectionIK text, protectionIP text, rechargeEnergySource rechargeEnergySource_type, refDevice text, refPointOfInterest json, roundTripEfficiency text, seeAlso json, selfDischargeRate text, serialNumber text, source text, storableEnergy text, toolBMS text, type StorageBatteryDevice_type, typeEnergySource json, typeOfUse typeOfUse_type, usableEnergy text, volEnergyDensity json, weight text);