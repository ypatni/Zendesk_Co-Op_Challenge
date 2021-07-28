import React from "react";
import Card from "react-bootstrap/Card";
import Button from "react-bootstrap/Button";
import './Parts.css'

function DetailsCard(props) {
  return (
    <Card className="project-card-view">
      <Card.Body>
        <Card.Title>{props.id}</Card.Title>
        <Card.Text style={{ textAlign: "justify" }}>
          {props.description}
        </Card.Text>
      </Card.Body>
    </Card>
  );
}
export default DetailsCard;