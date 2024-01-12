import { Route, Routes } from "react-router-dom";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Certificate from "./pages/Certificate";
import NavBar from "./components/NavBar";
import { AuthProvider } from "./context/Auth";
import { RequireAuth } from "./components/RequireAuth";
function App() {
  return (
    <AuthProvider>
      <>
        <NavBar />
        <Routes>
          <Route
            path="/"
            element={
              <RequireAuth>
                <Home />
              </RequireAuth>
            }
          ></Route>
          <Route
            path="/certificates"
            element={
              <RequireAuth>
                <Certificate />
              </RequireAuth>
            }
          ></Route>
          <Route path="/login" element={<Login />}></Route>
        </Routes>
      </>
    </AuthProvider>
  );
}

export default App;
