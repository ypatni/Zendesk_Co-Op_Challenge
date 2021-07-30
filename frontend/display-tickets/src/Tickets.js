import React, { Component } from "react";
import "./Button.css";
import {
  Link
} from "react-router-dom";

import "./Design.css";
class Tickets extends Component {
  constructor(props) {
    super(props);
    this.state = {
      totalTickets: 0,
      ticketsOnCurrentPage: 0,
      isFirstPage: true,
      hasMore: true,
      error: null,
      isLoaded: false,
      items: [],
      afterCursor: "",
      beforeCursor: "",
      afterLink: "",
      beforeLink: "",
    };
  }
  componentDidMount() {
    const requestOptions = {
      method: "POST",
      body: JSON.stringify({ cursor: this.state.afterLink }),
    };

    fetch(
      "https://faq1slxbph.execute-api.us-east-1.amazonaws.com/dev/tickets",
      requestOptions
    )
      .then((res) => res.json())
      .then(
        (result) => {
          console.log('test0')
          console.log(typeof result);
          if (result.error) {
            this.setState({
              error: result.error,
            });
          } else {
            console.log("test1");

            this.setState({
              isLoaded: true,
              isFirstPage: false,
              items: result.tickets.tickets,
              afterCursor: result.tickets.meta.after_cursor,
              beforeCursor: result.tickets.meta.before_cursor,
              afterLink: result.tickets.links.next,
              beforeLink: result.tickets.links.prev,
              totalTickets: result.info.count.value,
              ticketsOnCurrentPage: result.tickets.tickets.length,
            });
          }
        },
        // Note: it's important to handle errors here
        // instead of a catch() block so that we don't swallow
        // exceptions from actual bugs in components.
        (error) => {
          console.log(error);
          this.setState({
            isLoaded: true,
            error,
          });
        }
      );
  }
  requestPost = () => {
    const requestOptions = {
      method: "POST",
      body: JSON.stringify({ cursor: this.state.afterLink }),
    };

    fetch(
      "https://faq1slxbph.execute-api.us-east-1.amazonaws.com/dev/tickets",
      requestOptions
    )
      .then((res) => res.json())
      .then(
        (result) => {
          console.log(result);
          if (result.error) {
            this.setState({
              error: result.error,
            });
          } else {
            console.log("test3");
            console.log(result);
            console.log(result.info);
            console.log("test2");
            this.setState({
              isFirstPage: false,
              hasMore: result.tickets.meta.has_more,
              isLoaded: true,
              items: result.tickets.tickets,
              afterCursor: result.tickets.meta.after_cursor,
              beforeCursor: result.tickets.meta.before_cursor,
              afterLink: result.tickets.links.next,
              beforeLink: result.tickets.links.prev,
              totalTickets: result.info.count.value,
              ticketsOnCurrentPage: result.tickets.tickets.length,
            });
          }
        },
        // Note: it's important to handle errors here
        // instead of a catch() block so that we don't swallow
        // exceptions from actual bugs in components.
        (error) => {
          this.setState({
            isLoaded: true,
            error,
          });
        }
      );
  };
  requestPreviousPost = () => {
    const requestOptions = {
      method: "POST",
      body: JSON.stringify({ cursor: this.state.beforeLink }),
    };

    fetch(
      "https://faq1slxbph.execute-api.us-east-1.amazonaws.com/dev/tickets",
      requestOptions
    )
      .then((res) => res.json())
      .then(
        (result) => {
          console.log(result.links);
          if (result.error) {
            this.setState({
              error: result.error,
            });
          } else {
            this.setState({
              isFirstPage: true,
              hasMore: result.tickets.meta.has_more,
              isLoaded: true,
              items: result.tickets.tickets,
              afterCursor: result.tickets.meta.after_cursor,
              beforeCursor: result.tickets.meta.before_cursor,
              afterLink: result.tickets.links.next,
              beforeLink: result.tickets.links.prev,
              totalTickets: result.info.count.value,
              ticketsOnCurrentPage: result.tickets.tickets.length,
            });
          }
        },
        // Note: it's important to handle errors here
        // instead of a catch() block so that we don't swallow
        // exceptions from actual bugs in components.
        (error) => {
          this.setState({
            isLoaded: true,
            error,
          });
        }
      );
  };

  render() {
    const { error, isLoaded, items } = this.state;
    if (error) {
      return (
        <>
          <div>
            <h1
              style={{
                textAlign: "center",
                fontWeight: "bolder",
                paddingBottom: "40px",
              }}
            >
              Ticket Information
            </h1>
          </div>

          <h4 style={{ textAlign: "center", fontWeight: "bolder" }}>
            Oh no! It looks like something went wrong! Here's the error message
            below:
          </h4>
          <h2
            style={{
              textAlign: "center",
              fontWeight: "bolder",
              fontFamily:
                "Lucida Sans Typewriter,Lucida Console,monaco,Bitstream Vera Sans Mono,monospace",
              color: "rgb(134, 129, 53)",
            }}
          >
            Error: {error}
          </h2>
        </>
      );
    } else if (!isLoaded) {
      return <div>Loading...</div>;
    } else {
      //body.cursor = this.state.cursor
      return (
        <>
          <h1
            className="h1"
            style={{ textAlign: "center", fontWeight: "bolder" }}
          >
            Ticket Manager{" "}
          </h1>

          <div
            style={{
              display: "flex",
              justifyContent: "center",
              alignItems: "center",
              paddingBottom: "30px",
            }}
          >
            <button
              className="btn-primary "
              style={{ marginRight: "50px" }}
              onClick={this.requestPreviousPost}
            >
              {" "}
              Back
            </button>

            {this.state.hasMore && (
              <button className="btn-primary " onClick={this.requestPost}>
                {" "}
                Next
              </button>
            )}
          </div>
          <div
            style={{
              marginTop: "10px",
              marginBottom: "1em",
              display: "flex",
              justifyContent: "center",
              alignItems: "center",
            }}
          >
            <p><b>{this.state.totalTickets}</b> {" "} total Tickets.{" "}
            <b>{this.state.ticketsOnCurrentPage}</b> tickets on this page.</p>
          </div>

          {/* <h1>{this.state.after_cursor}</h1> */}
          {items.map((item) => (
            <div className="body-item">
              <div className="body-item__description">
                <Link
                  to={{
                    pathname: `/view-ticket/${item.id}`,
                    state: { items: item },
                  }}
                  style={{ textDecoration: "none" }}
                >
                  <div style={{ color: "rgb(189, 217, 215)" }}>
                    Ticket {item.id} : {item.subject}
                  </div>
                </Link>
              </div>
            </div>
          ))}
                    <div
            style={{
              display: "flex",
              justifyContent: "center",
              alignItems: "center",
              paddingBottom: "50px",
              paddingTop: '30px'
            }}
          >
           { this.state.hasMore &&  (<button
              className="btn-primary "
              style={{ marginRight: "50px" }}
              onClick={this.requestPreviousPost}
            >
              {" "}
              Back
            </button>)}

            {this.state.hasMore && (
              <button className="btn-primary " onClick={this.requestPost}>
                {" "}
                Next
              </button>
            )}
          </div>
        </>
      );
    }
  }
}

export default Tickets;
