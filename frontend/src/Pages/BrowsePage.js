import React, { Component } from "react";
import { Row, Col, Container, Form, Button, FormGroup } from "react-bootstrap";
import { NavLink } from "react-router-dom";

export default class BrowsePage extends Component {
  state = {
    possible_dates: [],
    possible_times: [],
    possible_sizes: [],
    possible_neighborhoods: [],
    selected_date: "",
    selected_time: "",
    selected_size: "",
    selected_neighborhood: "",
    restaurants: [],
    selected_restaurant_id: "",
    loggedIn: false,
  };
  componentDidMount() {
    // some logic to verify logged in
    this.loggedIn = true;

    // replace with API calls
    this.setState({
      possible_dates: ["Saturday", "Sunday"],
      possible_times: ["12", "1", "2"],
      possible_sizes: ["2", "4", "6"],
      possible_neighborhoods: ["Westwood", "Santa Monica", "Sawtelle", "DTLA"],
    });
  }
  render() {
    return (
      <Container>
        <h1>Browse Page</h1>
        <Form>
          <Form.Group controlId="neighborhood">
            <Form.Label>Neighborhood</Form.Label>
            <Form.Control
              as="select"
              custom="true"
              onChange={(e) =>
                this.setState({ selected_neighborhood: e.target.value })
              }
            >
              <option value="">Choose...</option>
              {this.state.possible_neighborhoods.map((o) => {
                const neighborhood = o;
                return <option key={neighborhood}>{neighborhood}</option>;
              })}
            </Form.Control>
          </Form.Group>
          <Form.Group controlId="date">
            <Form.Label>Date</Form.Label>
            <Form.Control
              as="select"
              custom="true"
              onChange={(e) => this.setState({ selected_date: e.target.value })}
            >
              <option value="">Choose...</option>
              {this.state.possible_dates.map((o) => {
                const date = o;
                return <option key={date}>{date}</option>;
              })}
            </Form.Control>
          </Form.Group>
          <Form.Group controlId="time">
            <Form.Label>Time</Form.Label>
            <Form.Control
              as="select"
              custom="true"
              onChange={(e) => this.setState({ selected_time: e.target.value })}
            >
              <option value="">Choose...</option>
              {this.state.possible_times.map((o) => {
                const time = o;
                return <option key={time}>{time}</option>;
              })}
            </Form.Control>
          </Form.Group>
          <Form.Group controlId="location">
            <Form.Label>Size</Form.Label>
            <Form.Control
              as="select"
              custom="true"
              onChange={(e) => this.setState({ selected_size: e.target.value })}
            >
              <option value="">Choose...</option>
              {this.state.possible_sizes.map((o) => {
                const size = o;
                return <option key={size}>{size}</option>;
              })}
            </Form.Control>
          </Form.Group>
        </Form>

        <p>Select from the following restaurants:</p>
        <NavLink
          to={`/reserve/${this.state.selected_restaurant_id}/${this.state.selected_date}/${this.state.selected_time}/${this.state.selected_size}`}
          onClick={this.makeBooking}
        >
          Make a booking
        </NavLink>
      </Container>
    );
  }
}
