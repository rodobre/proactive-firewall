import React from 'react';
import { Button } from "antd";
import { DownloadOutlined, ReloadOutlined, PoweroffOutlined } from '@ant-design/icons';

// The action dashboard implements the buttons for control
class ActionDashboard extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div className="grid-one-column-nogap" style={{marginTop: '100px'}}>
                <Button type="primary" icon={<DownloadOutlined />} style={{marginLeft: '30px', marginRight: '30px' }}>
                    Update firmware
                </Button>

                <Button type="primary" icon={<ReloadOutlined />} style={{marginLeft: '30px', marginRight: '30px'}}>
                    Restart
                </Button>

                <Button type="primary" icon={<PoweroffOutlined />} style={{marginLeft: '30px', marginRight: '30px'}}>
                    Power off
                </Button>
            </div>
        );
    }
}

export default ActionDashboard;