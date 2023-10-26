/* (Beta) Export of data model BatteryStatus of the subject dataModel.Battery for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE BatteryStatus_type AS ENUM ('BatteryStatus');
CREATE TABLE BatteryStatus (acPowerInput NUMERIC, acPowerOutput NUMERIC, address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, dcPowerInput NUMERIC, dcPowerOutput NUMERIC, description TEXT, id TEXT PRIMARY KEY, location JSON, name TEXT, owner JSON, refBattery JSON, seeAlso JSON, source TEXT, statusPercent NUMERIC, type BatteryStatus_type);