import React from 'react';
import HeatMapWrapper from './HeatmapWrapper';
import Grid from '@material-ui/core/Grid';

// Unused component, part of future versions
function EndpointData() {
    const data_series = [
        {'Data':[21, 6, 42, 35, 12, 13, 30, 62]},
        {'Data':[31, 51, 22, 34, 15, 25, 19, 7]},
        {'Data':[1, 3, 6, 15, 27, 21, 14, 12]},
        {'Data':[14, 3, 8, 9, 22, 74, 1, 5]},
        {'Data':[81, 5, 60, 40, 5, 8, 24, 55]},
        {'Data':[67, 48, 43, 26, 45, 89, 53, 25]},
        {'Data':[22, 71, 79, 46, 21, 48, 45, 59]},
        {'Data':[95, 86, 44, 65, 96, 14, 95, 7]},
        {'Data':[47, 41, 67, 59, 67, 49, 44, 84]},
        {'Data':[59, 91, 60, 54, 64, 70, 10, 4]},
        {'Data':[47, 23, 6, 31, 39, 14, 31, 98]},
        {'Data':[14, 45, 54, 63, 77, 5, 79, 71]}
    ];

    return (
        <div className="bodyContainer">
            <h1 style={{textAlign: "center", marginTop: 20, marginBottom: 20 }}>Threat Hunter - Endpoint Data</h1>

            <Grid
                container
                spacing={0}
                direction="column"
                alignItems="center"
                justify="center"
                style={{marginTop: 100}}
            >
                <Grid item xs>
                    <HeatMapWrapper series={data_series} />
                </Grid>
            </Grid>
        </div>
    );
}

export default EndpointData;