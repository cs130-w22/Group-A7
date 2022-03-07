import React, { Component } from "react";
import { Row, Col, Container, Form, Button, FormGroup } from "react-bootstrap";
import { NavLink } from "react-router-dom";

export default class AccountDetails extends Component {
  render() {
    return (
      <Container>
        <p>Here are the account details</p>
        <h1>Welcome {this.props.account.name}</h1>
        <h2>You are based in {this.props.account.location}</h2>
        <h2>You have made {this.props.account.nbookings} bookings</h2>
        <h2>Member since {this.props.account.year}</h2>
      </Container>
    );
  }
}
