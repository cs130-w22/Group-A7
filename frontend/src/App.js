import "./App.css";
import { HashRouter, Route, Routes } from "react-router-dom";
import { Nav, Navbar, Container } from "react-bootstrap";
import React, { Component } from "react";
import axios from "axios";
import Cookies from "js-cookie";

import HomePage from "./Pages/HomePage";
import LandingPage from "./Pages/LandingPage";
import LoginPage from "./Pages/LoginPage";
import SignupPage from "./Pages/SignupPage";
import BrowsePage from "./Pages/BrowsePage";
import ReviewPage from "./Pages/ReviewPage";
import ProfilePage from "./Pages/ProfilePage";
import RestaurantPage from "./Pages/RestaurantPage";

class App extends Component {
  state = {
    user: "",
    dummy: 0,
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
        this.setState({ user: response.data });
      })
      .catch(function (error) {
        console.log(error);
      });
  }

  onSubmit = () => {
    axios({
      method: "post",
      url: "http://localhost:8000/logout/",
      headers: {
        "Content-Type": "text/plain",
        "X-CSRFToken": Cookies.get("XSRF-TOKEN"),
      },
      withCredentials: true,
    })
      .then((response) => {
        console.log(response.status);
        this.setState({ user: "" });
      })
      .catch(function (error) {
        console.log(error);
      });
  };

  render() {
    function TryUsername(props) {
      const user = props.user;

      if (user !== "") {
        return (
          <div>
            {/* <Navbar.Text>Signed in as: {user} .</Navbar.Text> */}
            <Nav.Link href="#/profile">
              <h4 className="linkText">Signed in as: {user}</h4>
            </Nav.Link>
          </div>
        );
      } else {
        return <div></div>;
      }
    }
    return (
      <Container>
        <Navbar bg="primary" variant="dark">
          <Navbar.Brand href="#/">DineSmart</Navbar.Brand>
          <Nav className="mr-auto">
            <Nav.Link href="#/home">Home</Nav.Link>
            <Nav.Link href="#/login">Login</Nav.Link>
            <Nav.Link href="#/browse">Browse</Nav.Link>
            <Nav.Link href="#/restaurant">Restaurant</Nav.Link>
            <Nav.Link href="#/review">Review</Nav.Link>
          </Nav>
          <Navbar.Collapse className="justify-content-end">
            <TryUsername user={this.state.user}></TryUsername>
            <Navbar.Text onClick={this.onSubmit}>
              <a href="#login">Logout</a>
            </Navbar.Text>
          </Navbar.Collapse>
        </Navbar>
        <HashRouter>
          <div className="App">
            <Routes>
              <Route exact path="/" element={<LandingPage />} />
              <Route path="/home" element={<HomePage />} />
              <Route path="/login" element={<LoginPage />} />
              <Route path="/signup" element={<SignupPage />} />
              <Route path="/browse" element={<BrowsePage />} />
              <Route path="/restaurant/" element={<RestaurantPage />} />
              <Route path="/review/" element={<ReviewPage />} />
              <Route path="/profile/" element={<ProfilePage />} />
            </Routes>
          </div>
        </HashRouter>
      </Container>
    );
  }
}

export default App;
