import React from "react";
import ReactDOM from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router-dom";

import "./index.css";
import { Layout } from "@/components/Layout";
import { DashboardPage, CustomersPage } from "@/pages";
import { AddCustomerPage } from "./pages/AddCustomerPage";
import { Toaster } from "@/components/ui/toaster";
import { ActionsContextProvider } from "./store/actions-context";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout />,
    children: [
      {
        index: true,
        element: <DashboardPage />,
      },
      {
        path: "customers",
        element: <CustomersPage />,
      },
      {
        path: "add-customer",
        element: <AddCustomerPage />,
      },
    ],
  },
]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <ActionsContextProvider>
      <RouterProvider router={router} />
      <Toaster />
    </ActionsContextProvider>
  </React.StrictMode>
);
