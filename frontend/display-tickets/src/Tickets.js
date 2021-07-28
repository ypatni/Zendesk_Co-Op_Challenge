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
      isFirstPage: true,
      hasMore: true,
      error: null,
      isLoaded: false,
      items: [],
      after_cursor: '',
      before_cursor: '',
      after_link: '',
      before_link: '',
    };
  }
  componentDidMount() {
    const requestOptions = {
      method: "POST",
      body: JSON.stringify({ cursor: this.state.after_link }),
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
            isFirstPage: false,
            items: result.tickets,
            after_cursor: result.meta.after_cursor,
            before_cursor: result.meta.before_cursor,
            after_link: result.links.next,
            before_link: result.links.prev,
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
  requestPost = () => {
    const requestOptions = {
      method: "POST",
      body: JSON.stringify({ cursor: this.state.after_link  }),
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
            isFirstPage: false,
            hasMore:  result.meta.has_more,
            isLoaded: true,
            after_cursor: result.meta.after_cursor,
            before_cursor: result.meta.before_cursor,
            items: result.tickets,
            after_link: result.links.next,
            before_link: result.links.prev,
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
  };
  requestPreviousPost = () => {
    const requestOptions = {
      method: "POST",
      body: JSON.stringify({ cursor: this.state.before_link  }),
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
            isFirstPage: true,
            hasMore:  result.meta.has_more,
            isLoaded: true,
            after_cursor: result.meta.after_cursor,
            before_cursor: result.meta.before_cursor,
            items: result.tickets,
            after_link: result.links.next,
            before_link: result.links.prev,
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
  };

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
          <h3>{this.state.before_link}</h3>
          <h3>{this.state.after_cursor}</h3>
          { !this.state.isFirstPage &&
          <button onClick={this.requestPreviousPost}> Back</button>}

          {this.state.hasMore &&
          <button onClick={this.requestPost}> Next</button>}

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
