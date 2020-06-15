import React from "react";
import Chart from "react-apexcharts";

// Apex Charts - Shaded Line Chart wrapper
class LineChart extends React.Component {
    constructor(props) {
        super(props);
        this.title = this.props.title;
        this.name = this.props.name;
        this.axisname = this.props.axisname;
        this.height = (this.props.height === undefined) ? 350 : this.props.height;

        this.state = {
            series: [{
                name: this.name,
                data: this.props.data
            }],
            options: {
                chart: {
                    type: 'area',
                    stacked: false,
                    height: this.height,
                    fontFamily: 'Oxanium',
                    foreColor: '#eaeaea',
                    zoom: {
                        type: 'x',
                        enabled: true,
                        autoScaleYaxis: true
                    },
                    toolbar: {
                        show: false,
                        autoSelected: 'zoom'
                    }
                },
                colors: ['#581f79'],
                dataLabels: {
                    enabled: false
                },
                markers: {
                    size: 1,
                },
                title: {
                    text: this.title,
                    align: 'left'
                },
                grid: {
                    borderColor: '#222',
                    row: {
                      colors: ['transparent'], // takes an array which will be repeated on columns
                      opacity: 0.8
                    },
                },
                fill: {
                    type: 'gradient',
                    gradient: {
                        shadeIntensity: 1,
                        gradientToColors: ['#541b75'],
                        inverseColors: false,
                        opacityFrom: 0.65,
                        opacityTo: 0.4,
                        stops: [0, 40, 100]
                    },
                },
                yaxis: {
                    labels: {
                        formatter: function (val) {
                            return val.toFixed(0);
                        }
                    },
                    title: {
                        text: this.axisname
                    },
                },
                xaxis: {
                    type: 'datetime',
                },
                tooltip: {
                    shared: false,
                    y: {
                        formatter: function (val) {
                            return val.toFixed(0);
                        }
                    }
                }
            }
        };
    }

    render() {
        
        return (
            <div>
                <Chart options={this.state.options} series={[{name: this.props.name, data: this.props.data}]} type="area" height={this.height} />
            </div>
        );
    }
}

export default LineChart;