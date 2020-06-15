import React from "react";
import Chart from "react-apexcharts";

// Unused component, part of future versions
class HeatMapWrapper extends React.Component {
    constructor(props) {
        super(props);

        this.series = this.props.series;

        this.state = {
            series: [{
                name: 'Jan',
                data: this.series[0]['Data']
              },
              {
                name: 'Feb',
                data: this.series[1]['Data']
              },
              {
                name: 'Mar',
                data: this.series[2]['Data']
              },
              {
                name: 'Apr',
                data: this.series[3]['Data']
              },
              {
                name: 'May',
                data: this.series[4]['Data']
              },
              {
                name: 'Jun',
                data: this.series[5]['Data']
              },
              {
                name: 'Jul',
                data: this.series[6]['Data']
              },
              {
                name: 'Aug',
                data: this.series[7]['Data']
              },
              {
                name: 'Sep',
                data: this.series[8]['Data']
              },
              {
                name: 'Oct',
                data: this.series[9]['Data']
              },
              {
                name: 'Nov',
                data: this.series[10]['Data']
              },
              {
                name: 'Dec',
                data: this.series[11]['Data']
              }
            ],
            options: {
              chart: {
                height: 600,
                type: 'heatmap',
                fontFamily: 'Oxanium',
                foreColor: '#eaeaea'
              },
              legend: {
                  show: true
              },
              plotOptions: {
                heatmap: {
                  shadeIntensity: 0.5,
              
                  colorScale: {
                    ranges: [{
                        from: -10,
                        to: 25,
                        name: 'low',
                        color: '#00A100'
                      },
                      {
                        from: 25,
                        to: 50,
                        name: 'medium',
                        color: '#128FD9'
                      },
                      {
                        from: 50,
                        to: 75,
                        name: 'high',
                        color: '#FFB200'
                      },
                      {
                        from: 75,
                        to: 100,
                        name: 'extreme',
                        color: '#FF0000'
                      }
                    ]
                  }
                }
              },
              dataLabels: {
                enabled: true
              },
              title: {
                text: 'Endpoint Heatmap - Attacks per Month'
              },
              responsive: [{
                breakpoint: 1000,
                options: {
                  chart: {
                    width: 500,
                    fontSize: '10px'
                  },
                  legend: {
                    show: false,
                  }
                }
              }]
             },
        };
    }

    render() {
        return (
            <Chart
                options={this.state.options}
                series={this.state.series}
                width="1000"
                type="heatmap"
            >
            </Chart>
        );
    }
}

export default HeatMapWrapper;