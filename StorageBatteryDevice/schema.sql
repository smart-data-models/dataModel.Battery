/* (Beta) Export of data model StorageBatteryDevice of the subject dataModel.Battery for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE batteryAssessmentMethods_type AS ENUM ('ampereHourMeter','dischargeTest','electrolyteDensity','highFrequencyImpedance','lowFrequencyImpedance','mathematicalModel','operatingVoltageWithClosedCircuit','quiescentVoltageWithOpenCircuit');CREATE TYPE batteryType_type AS ENUM ('alkaline','gel','lead','lead-AGM','Li-Ion','Li-Po','Li-Po4','LMP','Li-Air','Na-NiCl2(Zebra)','Ni-Cd','Ni-MH','Ni-Zn','other');CREATE TYPE installationMode_type AS ENUM ('aerial','ground','pole','roofing','underGround','wall','other');CREATE TYPE possibilityOfUse_type AS ENUM ('mobile','mixed','stationary','other');CREATE TYPE rechargeEnergySource_type AS ENUM ('electric','hydraulic','windTurbine','other');CREATE TYPE StorageBatteryDevice_type AS ENUM ('StorageBatteryDevice');CREATE TYPE typeOfUse_type AS ENUM ('indoor','mixed','outdoor','other');
CREATE TABLE StorageBatteryDevice (address JSON, alternateName TEXT, application JSON, areaServed TEXT, averageLife NUMERIC, batteryAssessmentMethods batteryAssessmentMethods_type, batteryType batteryType_type, brandName TEXT, capacityCnnn JSON, chargeDischargeReactivity NUMERIC, chargeEfficiency NUMERIC, chargePower NUMERIC, chargingModeAllowed JSON, communication JSON, dataProvider TEXT, dateCreated TIMESTAMP, dateLastReported TIMESTAMP, dateModified TIMESTAMP, description TEXT, dimension JSON, dischargeEfficiency NUMERIC, dischargePower NUMERIC, documentation TEXT, durationPeakPower NUMERIC, id TEXT PRIMARY KEY, installationCondition JSON, installationMode installationMode_type, lifeCycleNumber JSON, location JSON, manufacturerName TEXT, massEnergyDensity JSON, maxOutputPower NUMERIC, maximumVoltageEOC NUMERIC, minimumVoltageEOD NUMERIC, modelName TEXT, name TEXT, nominalAmpere NUMERIC, nominalCapacity NUMERIC, nominalFrequency NUMERIC, nominalVoltage NUMERIC, operatingAltitude JSON, operatingAmpere JSON, operatingFrequency JSON, operatingTemperature JSON, operatingVoltage JSON, overloadAccepted BOOLEAN, overloadAcceptedTime TIME, owner JSON, peakPower NUMERIC, possibilityOfUse possibilityOfUse_type, protectionIK NUMERIC, protectionIP TEXT, rechargeEnergySource rechargeEnergySource_type, roundTripEfficiency NUMERIC, seeAlso JSON, selfDischargeRate NUMERIC, serialNumber TEXT, source TEXT, storableEnergy NUMERIC, toolBMS BOOLEAN, type StorageBatteryDevice_type, typeEnergySource JSON, typeOfUse typeOfUse_type, usableEnergy NUMERIC, volEnergyDensity JSON, weight NUMERIC);