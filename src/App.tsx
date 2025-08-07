import Login from './pages/login'
import './App.css'
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Dashboard from "./pages/home.tsx";
import PrivateRoute from "./routes/privateRoute.tsx";
import RedirectRoute from "./routes/RedirectRoute.tsx";

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
              <Dashboard />
            </PrivateRoute>
          }
        />
      </Routes>
    </Router>
  );
}

export default App;


