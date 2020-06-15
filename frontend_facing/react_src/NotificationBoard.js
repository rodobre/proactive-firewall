import React from 'react';


// Notification board, used to aggregate notification logs in the dashboard
class NotificationBoard extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        let message_components = [];
        for (let i = 0; i < this.props.messages.length; ++i) {
            message_components.push(
                <div key={i} className="notification">
                    <p>{this.props.messages[i].date} {this.props.messages[i].content}</p>
                </div>
            );
        }

        return (
            <div className="grid-one-column-nogap chatbox-container">
                <div className="messages-container">
                    {message_components}
                </div>
            </div>
        );
    }
}

export default NotificationBoard;