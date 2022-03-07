import React, { Component } from "react";
import { Row, Col, Container, Form, Button, FormGroup } from "react-bootstrap";
import { NavLink } from "react-router-dom";
import axios from "axios";
import Cookies from "js-cookie";
export default class ReviewPage extends Component {
  state = {
    restaurantName: "",
    rating: "",
    longReview: "",
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

  onSubmit = () => {
    var data = JSON.stringify({
      restaurant: this.state.restaurantName,
      rating: this.state.rating,
      content: this.state.longReview,
    });
    axios({
      method: "post",
      url: "http://localhost:8000/addReview/",
      headers: {
        "Content-Type": "text/plain",
        "X-CSRFToken": Cookies.get("XSRF-TOKEN"),
      },
      data: data,
      withCredentials: "false",
    })
      .then((response) => {
        console.log(response.status);
        window.location.href = "/home";
      })
      .catch(function (error) {
        console.log(error);
      });
  };

  render() {
    return (
      <Container>
        <h1>Review Page</h1>
        <Form>
          <Form.Group controlId="name">
            <Form.Label>Enter the restaurant name</Form.Label>
            <Form.Control
              type="text"
              placeholder="Enter restaurant"
              value={this.state.restaurantName}
              onChange={(e) =>
                this.setState({ restaurantName: e.target.value })
              }
            />
          </Form.Group>
          <Form.Group controlId="rating">
            <Form.Label>Rating</Form.Label>
            <Form.Control
              as="select"
              custom="true"
              onChange={(e) => this.setState({ rating: e.target.value })}
            >
              <option value="">Choose...</option>
              {["1", "2", "3", "4", "5"].map((o) => {
                const stars = o;
                return <option key={stars}>{stars}</option>;
              })}
            </Form.Control>
          </Form.Group>
          <Form.Group controlId="details">
            <Form.Label>Enter your review here</Form.Label>
            <Form.Control
              type="text"
              placeholder="Enter details"
              value={this.state.longReview}
              onChange={(e) => this.setState({ longReview: e.target.value })}
              as="textarea"
              rows={3}
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
