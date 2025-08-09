import Login from './pages/login'
import './App.css'
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./pages/home.tsx";
import PrivateRoute from "./routes/PrivateRoute.tsx";
import RedirectRoute from "./routes/RedirectRoute.tsx";
import ServiceRegister from './pages/Services/register.tsx';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<RedirectRoute />} />
        <Route path="/login" element={<Login />} />
        <Route
          path="/dashboard"
          element={
            <PrivateRoute>
              <Home />
            </PrivateRoute>
          }
        />
        <Route
          path="/service-register"
          element={
            <PrivateRoute>
              <ServiceRegister />
            </PrivateRoute>
          }
        />
      </Routes>
    </Router>
  );
}

export default App;


