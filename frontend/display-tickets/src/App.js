import React, { Component } from "react";
import Card from "./UI/Card";
import {BrowserRouter as Router, Route, Switch } from "react-router-dom";
import { GoPrimitiveDot } from "react-icons/go";

import { Container, Grid, Header, List } from "semantic-ui-react";

import contacts from "./file_name.json";

const App = () => {


  return (
    <>
      <div>
        <div style = {{marginBottom: 10}}></div>
        <Router>
        <Switch>

        </Switch>
        </Router>
      </div>
    </>
  );
};

export default App;
