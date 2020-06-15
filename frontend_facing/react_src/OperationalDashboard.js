import React from "react";
import { Switch, Checkbox } from 'antd';


// Operational dashboard, functionality to be implemented

class LabeledCheckbox extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            label: this.props.label,
            enabled: (this.props.enabled === undefined) ? false : this.props.enabled
        }
    }

    onChange = () => {
        this.setState({
            enabled: !this.state.enabled
        });
    }

    render() {
        return (
            <p style={{display: 'flex', alignItems: 'center'}}>
                <Checkbox checked={this.state.enabled} onChange={this.onChange} style={{marginRight: '10px'}}/>
                {this.state.label}
            </p>
        );
    }
}

class OperationalDashboard extends React.Component {
    constructor(props) {
        super(props);
    }
    
    toggleChecked = (i) => {
        this.setState({ checked: !this.state.checkbox[i].checked })
    }

    render() { 
        return (
            <div className="grid-one-column" style={{marginLeft: "30px", marginRight: "30px"}} >
                <div style={{margin: "0px", paddingTop: "0px"}}>
                    <p style={{display: 'flex', alignItems: 'center', marginTop: "30px", marginBottom: "50px"}}>
                        <Switch defaultChecked={true} style={{marginRight: '20px'}}/>
                        System Status
                    </p>
                    <p>Monitored Endpoints</p>
                    <div className="grid-two-columns-nogap">
                        <LabeledCheckbox enabled={true} label='192.168.1.2' />
                        <LabeledCheckbox enabled={true} label='192.168.1.3' />
                        <LabeledCheckbox enabled={true} label='192.168.1.4' />
                        <LabeledCheckbox enabled={true} label='192.168.1.5' />
                        <LabeledCheckbox enabled={true} label='192.168.1.6' />
                        <LabeledCheckbox enabled={true} label='192.168.1.7' />
                        <LabeledCheckbox enabled={true} label='192.168.1.8' />
                        <LabeledCheckbox enabled={true} label='192.168.1.9' />
                    </div>
                </div>
            </div>
        );
    }
}

export default OperationalDashboard;