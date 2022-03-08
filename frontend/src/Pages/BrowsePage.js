import React, { Component } from "react";
import { Row, Col, Container, Form, Button, FormGroup } from "react-bootstrap";
import { NavLink } from "react-router-dom";
import axios from "axios";
import Cookies from "js-cookie";
import ListRestaurants from "../Components/ListRestaurants";
export default class BrowsePage extends Component {
  state = {
    location: "",
    cuisine: "",
    date: "",
    size: "",
    restaurants: [],
    loggedIn: false,
  };
  componentDidMount() {
    // some logic to verify logged in
    this.loggedIn = true;
  }

  search = () => {
    var data = JSON.stringify({
      city: this.state.location,
      date: this.state.date,
      seats: this.state.size,
      cuisine: this.state.cuisine,
    });
    axios({
      method: "post",
      url: "http://localhost:8000/browseRestaurants/",
      headers: {
        "Content-Type": "text/plain",
        "X-CSRFToken": Cookies.get("XSRF-TOKEN"),
      },
      data: data,
      withCredentials: "false",
    })
      .then((response) => {
        if (response.data !== "") {
          this.setState({ restaurants: response.data });
        }
      })
      .catch(function (error) {
        console.log(error);
      });
  };
  render() {
    return (
      <Container>
        <h1>Browse Page</h1>
        <Form>
          <Form.Group controlId="neighborhood">
            <Form.Label>Neighborhood</Form.Label>
            <Form.Control
              type="text"
              placeholder="Enter location"
              value={this.state.location}
              onChange={(e) => this.setState({ location: e.target.value })}
            />
          </Form.Group>
          <Form.Group controlId="cuisine">
            <Form.Label>Cuisine</Form.Label>
            <Form.Control
              type="text"
              placeholder="Enter cuisine"
              value={this.state.cuisine}
              onChange={(e) => this.setState({ cuisine: e.target.value })}
            />
          </Form.Group>
          <Form.Group controlId="date">
            <Form.Label>Date</Form.Label>
            <Form.Control
              type="text"
              placeholder="YYYY-MM-DD"
              value={this.state.date}
              onChange={(e) => this.setState({ date: e.target.value })}
            />
          </Form.Group>
          <Form.Group controlId="size">
            <Form.Label>Size</Form.Label>
            <Form.Control
              type="text"
              placeholder="Enter party size"
              value={this.state.size}
              onChange={(e) => this.setState({ size: e.target.value })}
            />
          </Form.Group>
        </Form>
        <Button onClick={this.search}>Search</Button>
        <p>Select from the following restaurants:</p>
        <ListRestaurants restaurants={this.state.restaurants}/>
      </Container>
    );
  }
}
