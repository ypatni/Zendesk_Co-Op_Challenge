import React from "react";
import { BrowserRouter as Router, useLocation, Link } from "react-router-dom";
import { Form, Card, Container, Row, Col } from "react-bootstrap";
import './Parts.css'
import DetailsCard from "./DetailsCard";
const ViewDetails = (_) => {
  const { state } = useLocation();

  return (
    <>


      {/* <p style={{ color: "white" }}>
        Look out for this space because there's some big things coming up!
      </p>
      <p style={{ color: "white" }}>
        <h3>In the meantime check out my <a style={{textDecoration: "none"}} href='/resume'><strong className='purple'>Resume</strong></a></h3>

      </p> */}



        <div className="expense-item__description" style= {{paddingLeft: '40rem'}}>

          <h2> <strong>Id:</strong> {state.items.id}</h2>

        </div>
        <div>
        <h3 style= {{paddingLeft: '15rem', paddingRight: '15rem'}}><strong>Name:</strong> {state.items.description}{" "}</h3>
        </div>

    </>
  );
};

export default ViewDetails;
