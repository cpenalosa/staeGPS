## Transit Vehicle Data Specification

The following provides the fields for the transit vehicle data types. All data needs to be in JSON with location data encoded in [GeoJSON](http://geojson.org/). 

### Transit Vehicle Data Type
The fields marked with an asterisk are already populated when you create the data source for your transit vehicle in Stae. 

| Field | Data type | Description | Validation | Example
| ---   | --- 		| ---         | ---		   | ---
|id*    | Text      | Represents a transit vehicle operated by the government. | Not empty | "Transit Vehicle"
|name* | Text 		| Descriptive name given to the vehicle by the operator. | Not empty | "M Train Tracker Pilot"
|notes* | Text 		| Description or further notes about the transit Vehicle. | Not empty | "Pilot GPS Deployment for M Train Routes"
|type | Text 		| Categorization of the vehicle. | Not empty | "New York City Subway Car"
|operators| Array 	| List of agencies of people responsible for the vehicle. | Not empty, max character length: 2048 | ["New York City Subway"]
|active | Boolean 	| True/false if the vehicle is currently in transit. | True/False | "True"
|heading | Number (degrees) 	| Direction the vehicle is pointing | Min: 0, Max: 360 | "175.45"
|speed 	| Number (KM/H) | Speed the UAS is currently going. | Min: 0, Max: 1000 | "5 KM/H"
|passengers | Number 		| Number of passengers currently in the vehicle. | Not empty, Min: 0, Max:1000 | "50"
|capacity | Number 		| Maximum number of passengers the vehicle can hold. | Not empty, Min: 0, Max:1000 | "202"
|routeId | Text 		| Unique ID for the current transit route the vehicle is operating on. | Not empty, max character length: 2048 | "Forest Hills – 71st Avenue"
|nextStationId | Text 		| Unique ID for the next station the vehicle will be servicing. | Not empty, max character length: 2048 | "5th Ave- 53rd Street"
|images | Array 	| List of images related to the transit vehicle | Not empty, max character length: 2048 | [https://stae.co/transit1.jpg, https://stae.co/transit2.jpg]
|location | Point 	| Location where the transit vehicle exists. | GEOJSON format | {"type": "Point", "coordinates": [-74.0429, 40.744]}