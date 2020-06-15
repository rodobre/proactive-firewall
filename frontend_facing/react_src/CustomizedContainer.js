import React from 'react';

// Shaded container, used for stylizing
class CustomizedContainer extends React.Component {
    constructor(props) {
        super(props);
        this.props = props;
        this.title = (this.props.title === undefined) ? undefined : this.props.title;
        this.icon = (this.props.icon === undefined) ? undefined : this.props.icon;
        this.sz = (this.props.sz === undefined) ? undefined : this.props.sz;
        this.id = this.props.id;
    }

    render() { 
        return (
            <div id={this.id} className="grid-container-sub" style={{gridColumn: this.sz, height: "100%"}}>
                <p style={{textAlign: "left", marginLeft: "50px"}}>{this.title}</p>
                <div className="filled-container" style={{height: "100%"}}>
                    {this.props.children}
                </div>
            </div>
        );
    }
}

export default CustomizedContainer;