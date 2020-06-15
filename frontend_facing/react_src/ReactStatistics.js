import React, { useState, useEffect } from 'react';
import DonutChartWrapper from "./ApexChartsWrapper.js";
import CustomizedContainer from "./CustomizedContainer.js";
import LineChart from "./LineChartWrapper.js";
import OperationalDashboard from "./OperationalDashboard.js";
import NotificationBoard from "./NotificationBoard.js";
import UptimeMonitor from "./UptimeMonitor.js";
import ActionDashboard from "./ActionDashboard.js";
import { format } from "date-fns";
import 'bootstrap/dist/css/bootstrap.min.css';
import "antd/dist/antd.css";

// Statistics component, aggregating all the dashboard features 
const generate_plot_data = (size, multip) => {
    let current_timestamp = new Date().getTime();
    let day_decrease = 60 * 60 * 24 * 1000;
    let current_time = 0;
    let y_test = 0;
    let data = [];
    
    for(let i = size; i > 0; --i) {
        current_time = new Date(current_timestamp - (day_decrease * i)).getTime();
        y_test = Math.floor((Math.random() + 1) * multip);
        data.push({x: current_time, y: y_test});
    }

    return data;
}

class StatisticsRender extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      threats: [],
      messages: []
    }
  }

  componentDidMount() {
    fetch('http://icnc.go.ro:23231/api/threats?limit=200')
        .then(response => response.json())
        .then(data => {
          let threats_json = data['threats'];
          let messages_json = threats_json.map(x => {
            return {
              date: "[" + x[0] + "] ",
              content: "Recorded new attack on endpoint " + x[2].split(":")[0] + ". Type: " + x[1]
            }
          });

          this.setState({ threats: threats_json, messages: messages_json});
    });
  }

  render() {
    let date_set = {};
    let plot_data = this.state.threats.forEach(
      elem => {
        let date = elem[0].split(" ")[0];
        if(date_set[date] !== undefined) {
          date_set[date] += 1;
        } else {
          date_set[date] = 0;
        }
      }
    )

    console.log(date_set);

    let attack_graph = Object.entries(date_set).map(elem => {
      return {
        x: new Date(elem[0]),
        y: elem[1]
      }
    });

    attack_graph = attack_graph.reverse();
    let today_attacks = 0, mean = 0, freq = 0;
    
    if(attack_graph.length == 0 || attack_graph.length == 1) {
      today_attacks = 0;
      mean = 0;
    }
    else {
      today_attacks = attack_graph[attack_graph.length - 1].y;

      for(let i = 0; i < attack_graph.length - 1; ++i) {
        mean += attack_graph[i].y;
      }
    
      mean = mean / (attack_graph.length - 1);
      freq = (today_attacks / mean * 100.0).toFixed(2);
    }

    return (
      <div className="bodyContainer">
          <div className="grid-twelve-columns" style={{marginTop: 50}}>
              <CustomizedContainer id="operational-board" title="Operational Dashboard" sz="span 3">
                  <OperationalDashboard />
              </CustomizedContainer>


              <CustomizedContainer id="uptime-board" title="Uptime Monitor" sz="span 2">
                  <UptimeMonitor />
              </CustomizedContainer>

              <CustomizedContainer id="notification-board" title="Notification Log" sz="span 7">
                  <NotificationBoard messages={this.state.messages} />
              </CustomizedContainer>

          </div>

          <div className="grid-twelve-columns" style={{marginTop: 50}}>
              <CustomizedContainer title="Attack Frequency" sz="span 3">
                  <DonutChartWrapper categories={["Frequency"]} series={[freq]} total_descr={"Frequency"} size={"100%"} />
              </CustomizedContainer>

              <CustomizedContainer title="Latest attacks" sz="span 9">
                  <LineChart name="Attacks" data={attack_graph} height={280} />
              </CustomizedContainer>
          </div>
      </div>
    );
  }
}

export default StatisticsRender;