import React, { Component } from "react";
import "./Design.css";
class ViewDetails extends Component {
  constructor(props) {
    super(props);
    console.log(props);
    this.state = {
      isLoaded: true,
      error: null,
      itemID: "",
      itemDescription: "",
      assigneeID: "",
      requesterID: "",
      ticketFormID: "",
      location: props.match,
    };
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
      .then((result) => {
        console.log(result);
        console.log(result.links);
        if (result.error) {
          console.log(result.error.title);
        } else {
          this.setState({
            isLoaded: true,
            itemDescription: result.ticket.description,
            itemID: result.ticket.id,
            assigneeID: result.ticket.assignee_id,
            requesterID: result.ticket.requester_id,
            ticketFormID: result.ticket.ticket_form_id,
          });
        }
      });
  }
  render() {
    const { error, isLoaded } = this.state;
    if (error) {
      return <div>Error: {error}</div>;
    } else if (!isLoaded) {
      return <div>Loading...</div>;
    } else {
      return (
        <>
          <h1 className="item-center">Ticket Information</h1>
          <div
            className="item-center"
            style={{ fontSize: "1.1em", marginBottom: "2px" }}
          >
            <h3>
              {" "}
              <strong>I.D. : </strong> {this.state.itemID}
            </h3>
          </div>
          <div
            className="item-center"
            style={{ fontSize: "1.1em", marginBottom: "2px" }}
          >
            <h3>
              {" "}
              <strong>Requester ID : </strong> {this.state.requesterID}
            </h3>
          </div>
          <div
            className="item-center"
            style={{ fontSize: "1.1em", marginBottom: "2px" }}
          >
            <h3>
              {" "}
              <strong>Assignee ID : </strong> {this.state.assigneeID}
            </h3>
          </div>
          <div
            className="item-center"
            style={{ fontSize: "1.1em", marginBottom: "2px" }}
          >
            <h3>
              {" "}
              <strong>Ticket Form ID : </strong> {this.state.ticketFormID}
            </h3>
          </div>
          <div className="item-center description-padding">
            <h3 style={{ justifyContent: "center", fontWeight: 500 }}>
              <strong style={{ fontWeight: "800", fontSize: "1.3em" }}>
                Ticket Description:
              </strong>{" "}
              <p style={{ fontWeight: 350 }}>{this.state.itemDescription}</p>{" "}
            </h3>
          </div>
        </>
      );
    }
  }
}

export default ViewDetails;
