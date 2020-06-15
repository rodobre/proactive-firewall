import React from "react";
import Chart from "react-apexcharts";

// Wrapper for Apex Charts - Donut Chart
class DonutChartWrapper extends React.Component {
    constructor(props) {
        super(props);

        this.series = this.props.series;
        this.categories = this.props.categories;
        this.id = this.props.id;
        this.total_descr = this.props.total_descr;
        this.size = (this.props.size === undefined) ? "60%" : this.props.size;

        this.state = {
            options: {},
            series: this.series,
            labels: this.categories,
            dataLabels: {
                enabled: true
            },
            chart: {
                fontFamily: 'Oxanium',
                foreColor: '#eaeaea',
                offsetX: 0,
                offsetY: 20
            },
            colors: ['#581f79'],
            plotOptions : {
                radialBar: {
                    startAngle: -135,
                    endAngle: 135,
                    hollow: {
                        margin: 0,
                        size: '60%',
                        background: '#eabaea22',
                    },
                    dataLabels: {
                        name: {
                            fontSize: '22px',
                        },
                        value: {
                            fontSize: '16px',
                        },
                        total: {
                            show: true,
                            label: this.total_descr,
                            formatter: function (w) {
                                return w.config.series.reduce((i, j) => i + j) + '%';
                              }
                        }
                    }
                }
            },
            stroke: {
                curve: 'straight',
                lineCap: 'square',
            }
        }
    }

    render() {
        return (
            <Chart
                    options={this.state}
                    series={this.props.series}
                    categories={this.categories}
                    type="radialBar"
                    width={this.size}
            />
        );
    }
}

export default DonutChartWrapper;
