import React, { memo } from "react";
import {
  ComposableMap,
  Geographies,
  Geography
} from "react-simple-maps";
import { scaleLinear } from "d3-scale";

// Unused component, part of future versions

const geoUrl =
  "https://raw.githubusercontent.com/zcreativelabs/react-simple-maps/master/topojson-maps/world-110m.json";

const colorScale = scaleLinear()
  .domain([0.01, 1.00])
  .range(["#FAFA0D", "#ff0a0d"]);

const countryMap = {
  'ITA': 0.39,
  'RUS': 0.84,
  'USA': 0.65,
  'CHN': 0.77,
  'DEU': 0.41,
  'FRA': 0.31,
  'ROU': 0.35,
  'JPN': 0.21,
  'BRA': 0.41,
  'MEX': 0.21,
  'CAN': 0.33,
  'NED': 0.36,
  'POL': 0.12,
  'ESP': 0.22,
  'PRT': 0.23
};

function getColorFromMap(key, map) {
  if(key in map)
    return colorScale(map[key]);
  return '#0a0a0d';
}

const MapChart = ({ setTooltipContent }) => {
  return (
    <>
      <ComposableMap
            data-tip=""
            projectionConfig={{ scale: 100 }}
            height={350}
      >
        <Geographies geography={geoUrl}>
          {({ geographies }) =>
            geographies.map(geo => (
              <Geography
                key={geo.rsmKey}
                geography={geo}
                onMouseEnter={() => {
                  const { NAME, POP_EST } = geo.properties;
                  setTooltipContent(`${NAME} — ${POP_EST}`);
                }}
                onMouseLeave={() => {
                  setTooltipContent("");
                }}
                style={{
                  default: {
                    fill: getColorFromMap(geo.properties.ISO_A3, countryMap),
                    outline: "none",
                    stroke: "#4a4a4d",
                    strokeWidth: "0.5px",
                    strokeOpacity: "0.5"
                  },
                  hover: {
                    fill: "#eaeaea",
                    outline: "none"
                  }
                }}
              />
            ))
          }
        </Geographies>
      </ComposableMap>
    </>
  );
};
  
  export default memo(MapChart);