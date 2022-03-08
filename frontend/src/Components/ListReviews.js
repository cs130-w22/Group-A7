import React, { Component } from "react";
import { Row, Col, Container, Form, Button, FormGroup } from "react-bootstrap";
import { NavLink } from "react-router-dom";
import axios from "axios";
import Cookies from "js-cookie";

import ReviewTile from "./ReviewTile";
export default class ListReviews extends Component {
  state = {
    reviews: ["review1", "review2"],
  };
  componentDidMount() {
    axios({
      method: "post",
      url: "http://localhost:8000/myReviews/",
      headers: {
        "Content-Type": "text/plain",
        "X-CSRFToken": Cookies.get("XSRF-TOKEN"),
      },
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
  }
  render() {
    console.log(this.state.reviews);
    // return <ReviewTile review={this.state.reviews} />;
    // remove this once multiple reviews are suported
    const listItems = Object.entries(this.state.reviews).map(
      (r) => <ReviewTile key={r} review={r}/>
    );
    return <Container>{listItems}</Container>;
  }
}
