import React, { Component } from "react";
import { BrowserRouter as Router, useLocation, Link } from "react-router-dom";
import { Form, Card, Container, Row, Col } from "react-bootstrap";
import Button from "react-bootstrap/Button";
import "./Design.css";
import PropTypes from "prop-types";

class ViewDetails extends Component {
  constructor(props) {
    super(props);
    console.log(props);
    this.state = {
      isLoaded: true,
      error: null,
      item_title: '',
      item_id: '',
      item_description: '',
      item_org_id: '',
      assignee_id: '',
      requester_id: '',
      location: props.match,
    };
    //console.log(this.state.location.state.items.id);
  }
  componentDidMount() {
    console.log("test");
    const requestOptions = {
      method: "GET",
    };

    fetch(
      `https://faq1slxbph.execute-api.us-east-1.amazonaws.com/dev/tickets/${this.state.location.params.id}`,
      requestOptions
    )
      .then((res) => res.json())
      .then(
        (result) => {
          console.log(result)
          console.log(result.links)
          if (result.error){
            console.log(result.error.title)

          }
          else{
            this.setState({
              isLoaded: true,
              item_description: result.ticket.description,
              item_id: result.ticket.id,
              assignee_id: result.ticket.assignee_id,
              requester_id: result.ticket.requester_id
            });
          }
        },
      );

  }
  render() {
    const { error, isLoaded} = this.state;
    if (error) {
      return <div>Error: {error}</div>;
    } else if (!isLoaded) {
      return <div>Loading...</div>;
    } else {
    return (
      <>
      <h1 className='item-center'>Ticket Information</h1>
        <div
          className=" item-center body-item__description"
        >
          <h2>
            {" "}
            <strong>I.D. : </strong> {this.state.item_id}
          </h2>
        </div>
        <div
          className="body-item__description item-center"
        >
          <h2>
            {" "}
            <strong>Requester ID : </strong> {this.state.requester_id}
          </h2>
        </div>
        <div
          className="body-item__description item-center"
        >
          <h2>
            {" "}
            <strong>Assignee ID : </strong> {this.state.assignee_id}
          </h2>
        </div>
        <div className = 'item-center description-padding' >
          <h3 style={{  justifyContent: 'center', fontWeight: 500 }}>
            <strong style={{fontWeight:'800', fontSize:'1.3em'}}>Ticket Description:</strong> <p style={{fontWeight:350}}>{this.state.item_description}</p>{" "}
          </h3>
        </div>
      </>
    );}
  }
}

export default ViewDetails;
