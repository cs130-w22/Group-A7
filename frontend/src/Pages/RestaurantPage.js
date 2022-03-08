import React, { Component } from "react";
import { Row, Col, Container, Form, Button, FormGroup } from "react-bootstrap";
import {  NavLink } from "react-router-dom";
import axios from "axios";
import Cookies from "js-cookie";
export default class RestaurantPage extends Component {
  state = {
    restaurantName: "",
    loggedIn: false,
  };

  componentDidMount() {
    axios({
      method: "post",
      url: "http://localhost:8000/getCurrentUser/",
      headers: {
        "Content-Type": "text/plain",
        "X-CSRFToken": Cookies.get("XSRF-TOKEN"),
      },
      withCredentials: "false",
    })
      .then((response) => {
        if (response.data !== "") {
          this.setState({ loggedIn: true });
        }
      })
      .catch(function (error) {
        console.log(error);
      });
  }

  render() {
    return (
      <Container>
        <h1>Restaurant Page</h1>
        <Form>
          <Form.Group>
            <Form.Label>Enter the restaurant name</Form.Label>
            <Form.Control
              type="text"
              placeholder="Enter restaurant"
              value={this.state.restauarantName}
              onChange={(e) =>
                this.setState({ restauarantName: e.target.value })
              }
            />
          </Form.Group>
          <Form.Group>
            <Form.Label>Enter the restaurant details</Form.Label>
            <Form.Control
              type="text"
              placeholder="Enter details"
              value={this.state.reservationDetails}
              onChange={(e) =>
                this.setState({ reservationDetails: e.target.value })
              }
            />
          </Form.Group>
        </Form>
        <NavLink to="/home/" onClick={this.onSubmit}>
          Submit
        </NavLink>
      </Container>
    );
  }
}
