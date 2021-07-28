import React, { Component } from "react";
import Card from "./UI/Card";
import {
  BrowserRouter as Router,
  Link,
  Redirect,
  useLocation,
  withRouter,
  history as useHistory,
} from "react-router-dom";
import { GoPrimitiveDot } from "react-icons/go";

import {
  Container,
  Grid,
  Header,
  List,
  SearchResults,
} from "semantic-ui-react";

import contacts from "./file_name.json";
import "./Parts.css";
class Tickets extends Component {
  constructor(props) {
    super(props);
    this.state = {
      error: null,
      isLoaded: false,
      items: [],
      cursor: "",
      before_cursor: "",
    };
  }
  componentDidMount() {
    const requestOptions = {
      method: "POST",
      body: JSON.stringify({ cursor: this.state.cursor }),
    };

    fetch(
      "https://faq1slxbph.execute-api.us-east-1.amazonaws.com/dev/tickets",
      requestOptions
    )
      .then((res) => res.json())
      .then(
        (result) => {
          console.log(result.links);
          this.setState({
            isLoaded: true,
            items: result.tickets,
            cursor: result.links.next,
            before_cursor: result.meta.before_cursor,
          });
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
  }
  requestPost =() => {
    const requestOptions = {
      method: "POST",
      body: JSON.stringify({ cursor: this.state.cursor }),
    };

    fetch(
      "https://faq1slxbph.execute-api.us-east-1.amazonaws.com/dev/tickets",
      requestOptions
    )
      .then((res) => res.json())

  }

  render() {
    const { error, isLoaded, items } = this.state;
    if (error) {
      return <div>Error: {error.message}</div>;
    } else if (!isLoaded) {
      return <div>Loading...</div>;
    } else {
      //body.cursor = this.state.cursor
      return (
        <>
          <h1>{this.state.cursor}</h1>
          <button onClick={this.requestPost}> click</button>
          {/* <h1>{this.state.after_cursor}</h1> */}
          {items.map((item) => (
            <Card className="expense-item">
              <div className="expense-item__description">
                <Link
                  to={{
                    pathname: `/view-answer/${item.id}`,
                    state: { items: item },
                  }}
                  style={{ textDecoration: "none" }}
                >
                  <div style={{ color: "black" }}>
                    <GoPrimitiveDot /> {item.id} {item.subject}
                  </div>
                </Link>
              </div>
            </Card>
          ))}
        </>
      );
    }
  }
}

export default Tickets;
