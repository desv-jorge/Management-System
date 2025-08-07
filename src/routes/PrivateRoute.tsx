// src/routes/PrivateRoute.tsx
import { Navigate } from "react-router-dom";
import Cookies from "js-cookie";
import type { JSX } from "react";

interface Props {
  children: JSX.Element;
}

const PrivateRoute = ({ children }: Props) => {
  const token = Cookies.get("jwt_token");

  if (!token) {
    return <Navigate to="/login" replace />;
  }

  return children;
};

export default PrivateRoute;
