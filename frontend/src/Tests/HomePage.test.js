import { render, screen } from "@testing-library/react";
import HomePage from "../Pages/HomePage";
import { BrowserRouter, Routes, Route } from "react-router-dom";

test("homepage renders", () => {
  render(
    <BrowserRouter>
      <Routes>
        <Route path="*" element={<HomePage />}></Route>
      </Routes>
    </BrowserRouter>
  );
  const title = screen.getByText("Your reservations");
  expect(title).toBeInTheDocument();
});

test("homepage shows reservations", () => {
  render(
    <BrowserRouter>
      <Routes>
        <Route path="*" element={<HomePage />}></Route>
      </Routes>
    </BrowserRouter>
  );
  const reservations = screen.getByText("Here are your reservations:");
  expect(reservations).toBeInTheDocument();
});

test("homepage has link to browse", () => {
  render(
    <BrowserRouter>
      <Routes>
        <Route path="*" element={<HomePage />}></Route>
      </Routes>
    </BrowserRouter>
  );
  const browse = screen.getByText("Browse local restaurants");
  expect(browse).toBeInTheDocument();
});

test("homepage has link to booking", () => {
  render(
    <BrowserRouter>
      <Routes>
        <Route path="*" element={<HomePage />}></Route>
      </Routes>
    </BrowserRouter>
  );
  const booking = screen.getByText("Know what you want? Make a booking");
  expect(booking).toBeInTheDocument();
});
