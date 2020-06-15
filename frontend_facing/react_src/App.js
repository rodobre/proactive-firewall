import React, { useState } from 'react';
import ReactTooltip from 'react-tooltip';
import MapChart from "./MapChart";
import StatisticsRender from "./ReactStatistics";
import EndpointData from "./EndpointData";
import { Navbar, Nav } from 'react-bootstrap';
import {
  BrowserRouter as Router,
  Switch,
  Route
} from 'react-router-dom';

// Main app, start with a Navbar and a Navigation Manager
// Render the principal components based on the route
function App() {
  const [content, setContent] = useState("");
  return (
     <Router>
      <Navbar collapseOnSelect expand="lg" className="navbar-global" variant="dark" sticky="top" >
        <Navbar.Brand href="/home">Threat Hunter</Navbar.Brand>
        <Navbar.Toggle aria-controls="responsive-navbar-nav" />
        <Navbar.Collapse id="responsive-navbar-nav">
          <Nav className="mr-auto">
            <Nav.Link href="/">Control Panel</Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Navbar>

      <Switch>
        <Route path="/">
          <StatisticsRender />
        </Route>
      </Switch>
    </Router>
  );
}

export default App;
