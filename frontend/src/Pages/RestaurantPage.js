import React, { Component } from "react";
import { Row, Col, Container, Form, Button, FormGroup } from "react-bootstrap";
import { useSearchParams } from "react-router-dom";
import axios from "axios";
import Cookies from "js-cookie";

import ReviewTile from "../Components/ReviewTile.js";
export default class RestaurantPage extends Component {

  getName = () => {
    const urlSearchParams = new URLSearchParams(window.location.hash);
    const params = Object.fromEntries(urlSearchParams.entries());
    return params['#/restaurant?name']
  }
  state = {
    restaurantName: this.getName(), // this.props.match.params.name,
    reviews: [],
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

  findReviews = () => {
    var data = JSON.stringify({
      restaurant: this.state.restaurantName,
    });
    axios({
      method: "post",
      url: "http://localhost:8000/getRestaurantReviews/",
      headers: {
        "Content-Type": "text/plain",
        "X-CSRFToken": Cookies.get("XSRF-TOKEN"),
      },
      data: data,
      withCredentials: "false",
    })
      .then((response) => {
        if (response.data !== "") {
          this.setState({ reviews: response.data });
        }
      })
      .catch(function (error) {
        console.log(error);
      });
  };

  render() {
    const listItems = Object.entries(this.state.reviews).map((r) => (
      <ReviewTile key={r} review={r} />
    ));
    return (
      <Container>
        <h1>Restaurant Review Page</h1>
        <Form>
          <Form.Group>
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
        </Form>
        <Button onClick={this.findReviews}>Find Reviews</Button>
        {listItems}
      </Container>
    );
  }
}
