import { useState, createContext, useContext } from "react";
import usersData from "../data/users.json";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import { useAtom } from "jotai";
import { errorMessage } from "../global_state/global_state";

const AuthContext = createContext(null);

export const AuthProvider = ({ children }) => {
  let [errorMsg, setErrorMsg] = useAtom(errorMessage);
  const [user, setUser] = useState(() => {
    const storedUser = localStorage.getItem("user");
    return storedUser ? JSON.parse(storedUser) : null;
  });
  const login = (username: string, password: string) => {
    try {
      const foundUser = usersData.users.find(
        (u) => u.username === username && u.password === password
      );
      if (foundUser !== undefined) {
        setUser(foundUser);
        localStorage.setItem("user", JSON.stringify(foundUser));
      } else {
        setErrorMsg("Invalid Username or password");
        toast.error("Invalid Username or password", {
          position: "top-right",
          autoClose: 5000,
          hideProgressBar: false,
          closeOnClick: true,
          pauseOnHover: true,
          draggable: true,
          progress: undefined,
          theme: "dark",
        });
      }
    } catch (error) {
      setErrorMsg("Error during login");
      toast.error("Error during login", {
        position: "top-right",
        autoClose: 5000,
        hideProgressBar: false,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
        progress: undefined,
        theme: "dark",
      });
    }
  };

  const logout = () => {
    setUser(null);
    localStorage.removeItem("user");
  };

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  return useContext(AuthContext);
};
