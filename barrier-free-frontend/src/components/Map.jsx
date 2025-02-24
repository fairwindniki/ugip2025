import React from "react";
import PropTypes from "prop-types";
import { GoogleMap, LoadScript, Marker, DirectionsRenderer } from "@react-google-maps/api";
import { getBarrierFreeRoute } from "../api/directionsApi";

const API_KEY = import.meta.env.VITE_GOOGLE_MAPS_API_KEY;

const containerStyle = {
  width: "100%",
  height: "500px",
};

const center = { lat: 35.6895, lng: 139.6917 };

const Map = ({ start, end }) => {
  const [directions, setDirections] = React.useState(null);
  const directionsPanelRef = React.useRef(null);

  React.useEffect(() => {
    if (start && end) {
      getBarrierFreeRoute(start, end).then((data) => {
        if (data && data.routes.length > 0) {
          setDirections(data);
        } else {
          console.error("⚠️ ルート情報なし");
        }
      });
    }
  }, [start, end]);

  return (
    <div style={{ display: "flex" }}>
      <LoadScript googleMapsApiKey={API_KEY}>
        <GoogleMap mapContainerStyle={containerStyle} center={center} zoom={13}>
          {start?.lat && start?.lng && <Marker position={{ lat: start.lat, lng: start.lng }} label="出発" />}
          {end?.lat && end?.lng && <Marker position={{ lat: end.lat, lng: end.lng }} label="目的地" />}
          {directions && <DirectionsRenderer directions={directions} panel={directionsPanelRef.current} />}
        </GoogleMap>
      </LoadScript>

      <div ref={directionsPanelRef} style={{ width: "300px", padding: "10px", backgroundColor: "#fff" }}>
        <h3>経路案内</h3>
      </div>
    </div>
  );
};


Map.propTypes = {
  start: PropTypes.shape({
    lat: PropTypes.number.isRequired,
    lng: PropTypes.number.isRequired,
  }),
  end: PropTypes.shape({
    lat: PropTypes.number.isRequired,
    lng: PropTypes.number.isRequired,
  }),
};

export default Map;
