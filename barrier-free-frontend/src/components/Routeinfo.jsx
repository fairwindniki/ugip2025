import PropTypes from 'prop-types';

const RouteInfo = ({ routeData }) => {
    if (!routeData || !routeData.routes || routeData.routes.length === 0) {
      return null;
    }
    const route = routeData.routes[0];
    return (
      <div className="route-info">
        <h2>ルート情報</h2>
        <p>距離: {route.legs[0].distance.text}</p>
        <p>所要時間: {route.legs[0].duration.text}</p>
      </div>
      );
  };
  
  RouteInfo.propTypes = {
      routeData: PropTypes.shape({
          routes: PropTypes.arrayOf(
              PropTypes.shape({
                  legs: PropTypes.arrayOf(
                      PropTypes.shape({
                          distance: PropTypes.shape({
                              text: PropTypes.string.isRequired,
                          }).isRequired,
                          duration: PropTypes.shape({
                              text: PropTypes.string.isRequired,
                          }).isRequired,
                      }).isRequired
                  ).isRequired,
              }).isRequired
          ).isRequired,
      }).isRequired,
  };
  
  export default RouteInfo;
