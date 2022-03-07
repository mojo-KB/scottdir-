/*
 * Coded by Rufat Hajizada for CS351
 * An example that allows to turn on and off markes and circles on the map
 * Also shows the poition of the point when you click on the map
 */
// Creates a new map 
var map = L.map('mapid').setView([51.508, -0.11], 11);

// Creates a streetview layer and inports layer image from OpenStreetMap
var streetView = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
});

// Adds StreetView layer to the map
streetView.addTo(map);

// Creates a circle for London and adds it to the map
var london = L.circle([51.505176, -0.125694], {
    color: 'red',
    fillColor: '#f03',
    fillOpacity: 0.5,
    radius: 1000
}).addTo(map).bindPopup('This is London');

// Creates a circle for Greenwich and adds it to the map
var greenwich = L.circle([51.480955, -0.005493], {
    color: 'green',
    fillColor: '#03f',
    fillOpacity: 0.5,
    radius: 1000
}).addTo(map).bindPopup('This is Greenwich');


var wimbledon = L.marker([51.425758, -0.218353]).bindPopup('This is Wimbledon').addTo(map); // Marker for Wimbledon
var stratford = L.marker([51.538648, 0.009613]).bindPopup('This is Stratford').addTo(map); // Marker for Stratfor

var circles = L.layerGroup([london, greenwich]); // Creates a Layer Group consisting of circles
var markers = L.layerGroup([wimbledon, stratford]); // Creates a Layer Group consisting of markers

// Creates visual element for titleLayer control
var baseMaps = {
    "Street view": streetView
};

// Creates an overlay for circles and markers layers
var overlayMaps = {
    "Circles": circles,
    "Markers": markers
};

L.control.layers(baseMaps, overlayMaps).addTo(map); // adds layer control elements on to the map

// Creates popups when clicking on the screen

var popup = L.popup();
function onMapClick(e) {
    popup
        .setLatLng(e.latlng)
        .setContent("You clicked the map at " + e.latlng)
        .openOn(map);
        // Uncomment following code if you want to create markers on click
    //var marker = L.marker(e.latlng).bindPopup(popup).addTo(map);
}

map.on('click', onMapClick);

