var getDirections = function (map, fromPoint) {
    $.getJSON("/api/v1/washington-dc/nearest/?lat="+fromPoint.lat()+"&lon="+fromPoint.lng(), function (data) {
        var directions = new google.maps.DirectionsService();
        directions.route({
            origin: fromPoint,
            destination: new google.maps.LatLng(data.coordinates[0],
                data.coordinates[1]),
            travelMode: google.maps.TravelMode.WALKING,
        }, function (result, status) {
            new google.maps.DirectionsRenderer({
                map: map,
                directions: result
            });
        })
    });
};

function initialize() {
    var mapOptions = {
        center: new google.maps.LatLng(38.8951, -77.0367),
        zoom: 15,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    var map = new google.maps.Map(document.getElementById("map-canvas"),
            mapOptions);

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (position) {
            var initialLocation = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
            map.setCenter(initialLocation);
            getDirections(map, initialLocation);
        });
    }
    var openWindow = null

        $.getJSON("/api/v1/washington-dc/", function(data) {
            for (var index in data) {
                var marker = new google.maps.Marker({
                    map: map,
                    position: new google.maps.LatLng(data[index].coordinates[0],
                        data[index].coordinates[1])
                });

                (function (marker, index) {
                    google.maps.event.addListener(marker, 'click', function () {
                        if (openWindow) {
                            openWindow.close();
                        }
                        openWindow = new google.maps.InfoWindow({
                            content: "<ul>" +
                            "<li>Bikes: " + data[index].bikes + "</li>" +
                            "<li>Empty Docks: " + data[index].empty_docks + "</li>" +
                            "</ul>"
                        });
                        openWindow.open(map, marker);
                    });
                })(marker, index);
            }
        });

    google.maps.event.addListener(map, 'dblclick', function(e) {
        getDirections(map, e.latLng);
    });
};
google.maps.event.addDomListener(window, 'load', initialize);

