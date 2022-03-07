import React, { Component } from "react";
import { Row, Col, Container, Form, Button, FormGroup } from "react-bootstrap";
import { NavLink } from "react-router-dom";

export default class ReviewPage extends Component {
  state = {
    restauarantName: "",
    rating: "",
    longReview: "",
    loggedIn: false,
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
              value={this.state.restauarantName}
              onChange={(e) =>
                this.setState({ restauarantName: e.target.value })
              }
            />
          </Form.Group>
          <Form.Group controlId="rating">
            <Form.Label>Rating</Form.Label>
            <Form.Control
              as="select"
              custom
              onChange={(e) => this.setState({ rating: e.target.value })}
            >
              <option value="">Choose...</option>
              {[1,2,3,4,5].map((o) => {
                const stars = o;
                return <option>{stars}</option>;
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
