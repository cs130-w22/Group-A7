import { render, screen } from "@testing-library/react";
import RestaurantPage from "../Pages/RestaurantPage";
import { BrowserRouter, Routes, Route } from "react-router-dom";

test("restaurant page renders", () => {
  render(
    <BrowserRouter>
      <Routes>
        <Route path="*" element={<RestaurantPage />}></Route>
      </Routes>
    </BrowserRouter>
  );
  const title = screen.getByText("Restaurant Review Page");
  expect(title).toBeInTheDocument();
});

test("restaurant page has restaurant name", () => {
  render(
    <BrowserRouter>
      <Routes>
        <Route path="*" element={<RestaurantPage />}></Route>
      </Routes>
    </BrowserRouter>
  );
  const name = screen.getByText("Enter the restaurant name");
  expect(name).toBeInTheDocument();
});

test("restaurant page has restaurant details", () => {
  render(
    <BrowserRouter>
      <Routes>
        <Route path="*" element={<RestaurantPage />}></Route>
      </Routes>
    </BrowserRouter>
  );
  const details = screen.getByText("Find Reviews");
  expect(details).toBeInTheDocument();
});
