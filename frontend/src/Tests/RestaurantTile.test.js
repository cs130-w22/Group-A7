import { render, screen } from "@testing-library/react";
import RestaurantTile from "../Components/RestaurantTile";
import { BrowserRouter, Routes, Route } from "react-router-dom";

test("restaurant tile name shows", () => {
  const dummyRestaurant = {
    name: "dummyName",
  };
  render(
    <BrowserRouter>
      <Routes>
        <Route
          path="*"
          element={<RestaurantTile restaurant={dummyRestaurant} />}
        ></Route>
      </Routes>
    </BrowserRouter>
  );
  const name = screen.getByText("dummyName");
  expect(name).toBeInTheDocument();
});

test("restaurant tile location shows", () => {
    const dummyRestaurant = {
      location: "dummyLocation",
    };
    render(
      <BrowserRouter>
        <Routes>
          <Route
            path="*"
            element={<RestaurantTile restaurant={dummyRestaurant} />}
          ></Route>
        </Routes>
      </BrowserRouter>
    );
    const location = screen.getByText("dummyLocation");
    expect(location).toBeInTheDocument();
  });

  test("restaurant tile price shows", () => {
    const dummyRestaurant = {
      price: "dummyPrice",
    };
    render(
      <BrowserRouter>
        <Routes>
          <Route
            path="*"
            element={<RestaurantTile restaurant={dummyRestaurant} />}
          ></Route>
        </Routes>
      </BrowserRouter>
    );
    const price = screen.getByText('Price: dummyPrice');
    expect(price).toBeInTheDocument();
  });
