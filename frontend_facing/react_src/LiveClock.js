import React from 'react';
import { format } from 'date-fns';

// State-managed live clock text
class LiveClock extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            startdate: (this.props.startdate === undefined) ? undefined : this.props.startdate,
            textdate: format(new Date((this.props.startdate === undefined) ? (new Date().getTime()) : this.props.startdate), "dd/MM/yyyy HH:mm:ss a")
        }
    }

    formatHour() {
        if (this.state.startdate === undefined)
            return format(new Date(), "dd/MM/yyyy HH:mm:ss a");

        return this.state.textdate;
    }

    componentDidMount() {
        if(this.state.startdate === undefined) {
            setInterval(
                () => {
                    this.setState({textdate: this.formatHour()});
                }, 1000
            );
        }
    }

    componentWillUnmount() {
        if(this.state.startdate === undefined) {
            clearInterval(this.state.startdate);
        }
    }

    render() {
        return (
            <span>
                {this.state.textdate}
            </span>
        );
    }
}

export default LiveClock;