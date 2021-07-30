import React from "react";
import {BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Tickets from "./Tickets";
import ViewDetails from "./ViewDetails";
import NotFound from './NotFound'
import "./Design.css"

const App = () => {


  return (
    <>

      {/* <NavBar /> */}

      <div>
        <div style = {{marginBottom: 10}}></div>
        <Router>
        <Switch>
          <Route exact path="/view-ticket/:id" component={ViewDetails} />
          <Route exact path="/" component={Tickets} />
          <Route component={NotFound} />
        </Switch>
        </Router>
      </div>
    </>
  );
};

export default App;
