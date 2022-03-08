import { render, screen } from "@testing-library/react";
import AccountDetails from "../Components/AccountDetails";
import { BrowserRouter, Routes, Route } from "react-router-dom";

test("acct details name shows", () => {
  const account = {
    name: "name",
    location: "LA",
    num_bookings: "0",
    member_since: "2022"
  };
  render(
    <BrowserRouter>
      <Routes>
        <Route
          path="*"
          element={<AccountDetails account={account} />}
        ></Route>
      </Routes>
    </BrowserRouter>
  );
  const name = screen.getByText("Welcome name");
  expect(name).toBeInTheDocument();
});

test("acct details location shows", () => {
    const account = {
      name: "name",
      location: "LA",
      num_bookings: "0",
      member_since: "2022"
    };
    render(
      <BrowserRouter>
        <Routes>
          <Route
            path="*"
            element={<AccountDetails account={account} />}
          ></Route>
        </Routes>
      </BrowserRouter>
    );
    const name = screen.getByText("You are based in LA");
    expect(name).toBeInTheDocument();
  });

  test("acct details nbooking shows", () => {
    const account = {
      name: "name",
      location: "LA",
      num_bookings: "0",
      member_since: "2022"
    };
    render(
      <BrowserRouter>
        <Routes>
          <Route
            path="*"
            element={<AccountDetails account={account} />}
          ></Route>
        </Routes>
      </BrowserRouter>
    );
    const name = screen.getByText("You have made 0 bookings");
    expect(name).toBeInTheDocument();
  });

  test("acct details membersince shows", () => {
    const account = {
      name: "name",
      location: "LA",
      num_bookings: "0",
      member_since: "2022"
    };
    render(
      <BrowserRouter>
        <Routes>
          <Route
            path="*"
            element={<AccountDetails account={account} />}
          ></Route>
        </Routes>
      </BrowserRouter>
    );
    const name = screen.getByText("Member since 2022");
    expect(name).toBeInTheDocument();
  });