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

test("browsepage shows time option", () => {
  render(
    <BrowserRouter>
      <Routes>
        <Route path="*" element={<BrowsePage />}></Route>
      </Routes>
    </BrowserRouter>
  );
  const time = screen.getByText("Time");
  expect(time).toBeInTheDocument();
});

test("homepage shows size option", () => {
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
