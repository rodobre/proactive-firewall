import React from 'react';
import { Timeline } from 'antd';
import LiveClock from "./LiveClock.js";

// Uptime monitor component

class UptimeMonitor extends React.Component {
    constructor(props) {
        super(props);
    }

    render() { 
        let currentTimestamp = new Date().getTime();
        let updateTime = currentTimestamp - 7 * 60 * 60 * 24 * 1000;
        let update2Time = currentTimestamp - 13 * 60 * 60 * 24 * 1000;
        let update3Time = currentTimestamp - 20 * 60 * 60 * 24 * 1000;

        return (
            <div className="grid-one-column-nogap" >
                <Timeline style={{marginLeft: '10px'}}>
                    <Timeline.Item color='#581f79'>
                        <p>Running at <LiveClock /></p>
                    </Timeline.Item>
                    <Timeline.Item color='#581f79'>
                        <p>Updated at <LiveClock startdate={updateTime}/></p>
                    </Timeline.Item>
                    <Timeline.Item color='#581f79'>
                        <p>Updated at <LiveClock startdate={update2Time}/></p>
                    </Timeline.Item>
                    <Timeline.Item color='#581f79'>
                        <p>Deployed at <LiveClock startdate={update3Time}/></p>
                    </Timeline.Item>
                </Timeline>
            </div>
        );
    }
}

export default UptimeMonitor;