import { render, screen } from "@testing-library/react";
import BrowsePage from "../Pages/BrowsePage";
import { BrowserRouter, Routes, Route } from "react-router-dom";

test("browsepage renders", () => {
  render(
    <BrowserRouter>
      <Routes>
        <Route path="*" element={<BrowsePage />}></Route>
      </Routes>
    </BrowserRouter>
  );
  const title = screen.getByText("Browse Page");
  expect(title).toBeInTheDocument();
});

test("browsepage shows neighborhood option", () => {
  render(
    <BrowserRouter>
      <Routes>
        <Route path="*" element={<BrowsePage />}></Route>
      </Routes>
    </BrowserRouter>
  );
  const neighborhood = screen.getByText("Neighborhood");
  expect(neighborhood).toBeInTheDocument();
});

test("browsepage shows date option", () => {
  render(
    <BrowserRouter>
      <Routes>
        <Route path="*" element={<BrowsePage />}></Route>
      </Routes>
    </BrowserRouter>
  );
  const date = screen.getByText("Date");
  expect(date).toBeInTheDocument();
});

test("browsepage shows cuisine option", () => {
  render(
    <BrowserRouter>
      <Routes>
        <Route path="*" element={<BrowsePage />}></Route>
      </Routes>
    </BrowserRouter>
  );
  const cuisine = screen.getByText("Cuisine");
  expect(cuisine).toBeInTheDocument();
});

test("browsepage shows size option", () => {
  render(
    <BrowserRouter>
      <Routes>
        <Route path="*" element={<BrowsePage />}></Route>
      </Routes>
    </BrowserRouter>
  );
  const size = screen.getByText("Size");
  expect(size).toBeInTheDocument();
});

test("browsepage shows search", () => {
  render(
    <BrowserRouter>
      <Routes>
        <Route path="*" element={<BrowsePage />}></Route>
      </Routes>
    </BrowserRouter>
  );
  const search = screen.getByText("Search");
  expect(search).toBeInTheDocument();
});
