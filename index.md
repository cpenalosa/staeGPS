<h2> stae GPS </h2>

<p> Start submitting GPS data to your city's stae account in real-time. </p> <br>

The following scripts in this guide currently work on the Rapsberry Pi 3, Model B with a USB GPS receiver.<br>

To get started, create an account at <a href="https://municipal.systems" target="_blank"> Municipal Systems</a>. Once you're in, make a data source for your GPS vehicle and copy your secret API key. Once you have the key, you're ready to begin the tutorial!<br>

Happy building! <br>

<h3> Quick Links </h3>

<b> Hardware </b>
<ul>
<li>Raspberry Pi 3, Model B <a href="https://www.amazon.com/Raspberry-Pi-RASPBERRYPI3-MODB-1GB-Model-Motherboard/dp/B01CD5VC92" target="_blank"> (Amazon) </a> </li>
<li> 2.5A/5V DC USB power or car charger with a 2.5A/5B DC port <a href="https://www.amazon.com/Mediabridge-Charger-Devices-Samsung-Galaxy/dp/B007TV88F2" target="_blank"> (Amazon) </a> </li>	
<li>8GB micro SD card <a href="https://www.amazon.com/SanDisk-MicroSDHC-Standard-Packaging-SDSDQUAN-008G-G4A/dp/B00M55C0VU" target="_blank"> (Amazon) </a> </li>
<li> USB GPS Receiver BU-353 <a href="https://www.amazon.com/GlobalSat-BU-353-S4-USB-Receiver-Black/dp/B008200LHW" target="_blank"> (Amazon)</a> </li>
<li> USB Modem  <a href="https://www.amazon.com/Unlocked-Huawei-E397u-53-Worldwide-Required/dp/B01M0JY15V" target="_blank"> (Amazon)</a> </li>
<li> Twilio SIM Card <a href="https://www.twilio.com/wireless/pricing" target="_blank"> (Order on Twilio) </a> </li></ul> 

<b> Python Scripts </b>
<ul>
<li>Snow Plow/Service Vehicle <br> <a href="https://github.com/cpenalosa/staeGPS/blob/master/Service%20Vehicle%20Tracker/plow-POST-service-vehicle.py" target="_blank">(posts in real-time to stae) </a> , <a href="https://github.com/cpenalosa/staeGPS/blob/master/Service%20Vehicle%20Tracker/plow-local-service-vehicle.py" target="_blank">(writes to local disk)</a> </li>
<li>Transit Vehicle <br> <a href="https://github.com/cpenalosa/staeGPS/blob/master/Transit%20Vehicle%20Tracker/subway-POST-transit-vehicle.py" target="_blank">(posts in real-time to stae) </a> , <a href="https://github.com/cpenalosa/staeGPS/blob/master/Transit%20Vehicle%20Tracker/subway-local-transit-vehicle.py" target="_blank">(writes to local disk)</a></li>
<li>UAS/Delivery Drone <br> <a href="https://github.com/cpenalosa/staeGPS/blob/master/Drone%20Tracker/dDrone-POST-UAS.py" target="_blank">(posts in real-time to stae) </a> , <a href="https://github.com/cpenalosa/staeGPS/blob/master/Drone%20Tracker/dDrone-local-UAS.py" target="_blank">(writes to local disk)</a></li>
</ul>
