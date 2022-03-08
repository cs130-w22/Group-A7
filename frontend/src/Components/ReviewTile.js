import React, { Component } from "react";
import { Row, Col, Container, Form, Button, FormGroup } from "react-bootstrap";
import { NavLink } from "react-router-dom";
import axios from "axios";
import Cookies from "js-cookie";
export default class ReviewTile extends Component {
  state = {
    restaurant_name: ""
  }
  componentDidMount() {
    var data = JSON.stringify({restaurant_id: this.state.restaurant_id})
    axios({
      method: "post",
      url: "http://localhost:8000/getRestaurantById/",
      headers: {
        "Content-Type": "text/plain",
        "X-CSRFToken": Cookies.get("XSRF-TOKEN"),
      },
      data: data,
      withCredentials: "false",
    })
      .then((response) => {
        if (response.data !== "") {
          this.setState({ restaurant_name: response.data });
        }
      })
      .catch(function (error) {
        console.log(error);
      });
  }
  render() {
    return (
      <Container>
        <h2>Restaurant id: {this.state.restaurant_name}</h2>
        <h2>Written by: {this.props.review[1].user_id} on {this.props.review[1].timestamp}</h2>
        <h2>Stars: {this.props.review[1].rating}</h2>
        <h2>Review: {this.props.review[1].content}</h2>
      </Container>
    );
  }
}
