import { render, screen } from "@testing-library/react";
import RestaurantTile from "../Components/RestaurantTile";
import { BrowserRouter, Routes, Route } from "react-router-dom";

test("restaurant tile name shows", () => {
  const details = {
    tag: "tag",
    times: [],
    link: "link"
  };
  render(
    <BrowserRouter>
      <Routes>
        <Route
          path="*"
          element={<RestaurantTile name="abc" details={details} />}
        ></Route>
      </Routes>
    </BrowserRouter>
  );
  const name = screen.getByText("abc");
  expect(name).toBeInTheDocument();
});


test("restaurant tile tag shows", () => {
  const details = {
    tag: "tag",
    times: [],
    link: "link"
  };
  render(
    <BrowserRouter>
      <Routes>
        <Route
          path="*"
          element={<RestaurantTile name="abc" details={details} />}
        ></Route>
      </Routes>
    </BrowserRouter>
  );
  const tag = screen.getByText("tag");
  expect(tag).toBeInTheDocument();
});

test("restaurant tile times shows", () => {
  const details = {
    tag: "tag",
    times: [],
    link: "link"
  };
  render(
    <BrowserRouter>
      <Routes>
        <Route
          path="*"
          element={<RestaurantTile name="abc" details={details} />}
        ></Route>
      </Routes>
    </BrowserRouter>
  );
  const time = screen.getByText("Times:");
  expect(time).toBeInTheDocument();
});

test("restaurant tile times shows", () => {
  const details = {
    tag: "tag",
    times: [],
    link: "link"
  };
  render(
    <BrowserRouter>
      <Routes>
        <Route
          path="*"
          element={<RestaurantTile name="abc" details={details} />}
        ></Route>
      </Routes>
    </BrowserRouter>
  );
  const time = screen.getByText("Times:");
  expect(time).toBeInTheDocument();
});

test("restaurant tile reviews shows", () => {
  const details = {
    tag: "tag",
    times: [],
    link: "link"
  };
  render(
    <BrowserRouter>
      <Routes>
        <Route
          path="*"
          element={<RestaurantTile name="abc" details={details} />}
        ></Route>
      </Routes>
    </BrowserRouter>
  );
  const review = screen.getByText("See reviews");
  expect(review).toBeInTheDocument();
});

test("restaurant tile booking shows", () => {
  const details = {
    tag: "tag",
    times: [],
    link: "link"
  };
  render(
    <BrowserRouter>
      <Routes>
        <Route
          path="*"
          element={<RestaurantTile name="abc" details={details} />}
        ></Route>
      </Routes>
    </BrowserRouter>
  );
  const link = screen.getByText("Make booking here");
  expect(link).toBeInTheDocument();
});