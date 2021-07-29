import React, { Component } from "react";
import Card from "./UI/Card";
import {BrowserRouter as Router, Route, Switch } from "react-router-dom";
import { GoPrimitiveDot } from "react-icons/go";
import Tickets from "./Tickets";
import ViewDetails from "./ViewDetails";
import { Container, Grid, Header, List } from "semantic-ui-react";
import NotFound from './NotFound'
import contacts from "./file_name.json";
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
