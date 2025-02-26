import { useEffect, useRef } from "react";
import PropTypes from 'prop-types';

const Map = ({ routeData }) => {
  const mapRef = useRef(null);
  const mapInstance = useRef(null);
  const directionsRenderer = useRef(null);

  useEffect(() => {
    if (!mapInstance.current) {
      const tokyo = { lat: 35.6895, lng: 139.6917 };
      if (window.google) {
        mapInstance.current = new window.google.maps.Map(mapRef.current, {
          center: tokyo,
          zoom: 13,
        });
        directionsRenderer.current = new window.google.maps.DirectionsRenderer({
          suppressMarkers: false,
        });
        directionsRenderer.current.setMap(mapInstance.current);
      }
    }
  }, []);

  useEffect(() => {
    if (routeData && directionsRenderer.current) {
      directionsRenderer.current.setDirections(routeData);
    }
  }, [routeData]);

  return (
    <div
      ref={mapRef}
      className="map-container"
    ></div>
  );
};
Map.propTypes = {
  routeData: PropTypes.object,
};

export default Map;