<h2> stae GPS </h2>

<p> Start submitting GPS data to your city's stae account in real-time. </p> <br>

The following scripts in this guide currently work on the Rapsberry Pi 3, Model B with a USB GPS receiver.<br>

To get started, create an account at <a href="https://municipal.systems" target="_blank"> Municipal Systems</a>. Once you're in, make a data source for your GPS vehicle and copy your secret API key. Once you have the key, you're ready to begin the tutorial!<br>

Happy building! 
<br>
<br>
<a href="https://docs.google.com/document/d/1RuPy-DXyvwP1_uuzpQx7pJ8gg4ft0RnslZ7wTNUNsGw/edit?usp=sharing" target="_blank"> Full Tutorial on Google Docs </a>
<br>
<a href="https://cpenalosa.github.io/staeGPS/" target="_blank"> Quick links to Scripts & Hardware </a>

## Service Vehicle Data Specification

The following provides the fields for the service vehicle data types. All data needs to be in JSON with location data encoded in [GeoJSON](http://geojson.org/). 

### Service Vehicle Data Type
The fields marked with an asterisk are already populated when you create the data source for your service vehicle in Stae. 

| Field | Data type | Description | Validation | Example
| ---   | --- 		| ---         | ---		   | ---
|id*    | Text      | Represents a service vehicle operated by the government. | Not empty | "Service Vehicle"
|name* | Text 		| Descriptive name given to the vehicle by the operator. | Not empty | "Snow Plow Trackers Pilot"
|notes* | Text 		| Description or further notes about the Service Vehicle. | Not empty | "Snow Plow Deployment for Downtown Routes"
|manufacturedAt  | Date      | Date/time the vehicle was manufactured. | Not empty | "2018-01-01"
|startedAt   | Date      | Date/time the vehicle was purchased. |  Not empty | "2018-02-01"
|endedAt   | Date      | Date/time the vehicle was sold or ended government service. |  Not empty | "2018-03-01"
|type | Text 		| Categorization of the vehicle. | Not empty | "Snow Plow"
|operators| Array 	| List of agencies of people responsible for the vehicle. | Not empty, max character length: 2048 | ["Public Works Deparment"]
|capacity | Text 		| Maximum number of passengers the vehicle can hold. | Not empty, Min: 0, Max:1000 | "5"
|manufacturer| Text | Make/manufacturer of the vehicle. | Not empty, max character length: 2048 | "Ford"
|model  | Text 		| Model of the vehicle. | Not empty, max character length: 2048 | "F-250"
|color  | Text 		| Color of the vehicle exterior. | Not empty, max character length: 2048 | "Shadow Black"
|fuel  | Text 		| Type of fuel the vehicle uses. | enumeration: gas, diesel, electric | "gas"
|transmission  | Text 		| Transmission of the vehicle, if applicable. | enumeration: manual, automatic | "automatic"
|cost | Number (USD) 	| Price of the vehicle when purchased. | Not empty, min: 0 | 35000
|value | Number (USD) 	| Current estimated value of the vehicle. | Not empty, min: 0 | 35000
|vin | Number 	| Unique legal identification number for the vehicle. | Not empty, max character length: 2048 | "1ABCD23EFGHI456789"
|registered | Text 	| Jurisdiction the vehicle is registered in. | Not empty, max character length: 2048 | "Jersey City, NJ"
|plate | Number 	| Registered license plate code for the vehicle. | Not empty, max character length: 2048 | "ABC1234"
|active | Boolean 	| True/false if the vehicle is currently in service. | True/False | "True"
|heading | Number (degrees) 	| Direction the vehicle is pointing | Min: 0, Max: 360 | "175.45"
|speed 	| Number (KM/H) | Speed the UAS is currently going. | Min: 0, Max: 1000 | "5 KM/H"
|tripId | Text 		| Unique ID for the current trip the vehicle is on. | Not empty, max character length: 2048 | "Trip 001"
|routeId | Text 		| Unique ID for the current service route the vehicle is operating on. | Not empty, max character length: 2048 | "CBD Emergency Vehicle Route"  
|stream | Text 		| URL of the live video feed for the camera. | Not empty, max character length: 2048, stream URL exists | https://stae.co/ServiceFeed
|images | Array 	| List of images related to the service vehicle | Not empty, max character length: 2048 | [https://stae.co/service1.jpg, https://stae.co/service2.jpg]
|location | Point 	| Location where the UAS exists. | GEOJSON format | {"type": "Point", "coordinates": [-74.0429, 40.744]}


