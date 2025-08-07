// src/routes/RedirectRoute.tsx
import { Navigate } from "react-router-dom";
import Cookies from "js-cookie";

const RedirectRoute = () => {
  const token = Cookies.get("jwt_token");

  if (token) {
    return <Navigate to="/dashboard" replace />;
  } else {
    return <Navigate to="/login" replace />;
  }
};

export default RedirectRoute;
