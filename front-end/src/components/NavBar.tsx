import { Link } from "react-router-dom";
import { useAuth } from "../context/Auth";

const NavBar = () => {
  const auth = useAuth();
  return (
    <div className="relative border-b">
      <nav className="container mx-auto">
        <div className="max-w-4xl h-12 nd:h-16 mx-auto flex justify-between align-stretch px-4">
          <div id="logo" className="flex items-center text-blue-600 font-bold">
            <a></a>
          </div>
          <ul
            id="nav-links"
            className="hidden md:block absolute md:relative md:flex md:align-stretch md:justify-end right-0 top-0 mt-10 md:mt-0 py-2 md:py-0 w-48 md:w-auto h-auto z-10 bg-white shadow md:shadow-none"
          >
            <li>
              <div className="w-full h-full flex md:items-center pl-6 md:pl-4 pr-4 py-1 hover:bg-gray-100">
                <Link to="/">Home</Link>
              </div>
            </li>
            <li>
              <div className="w-full h-full flex md:items-center pl-6 md:pl-4 pr-4 py-1 hover:bg-gray-100">
                {" "}
                <Link to="/certificates">Certificate</Link>
              </div>
            </li>
            <li>
              <div className="w-full h-full flex md:items-center pl-6 md:pl-4 pr-4 py-1 hover:bg-gray-100">
                {!auth.user && <Link to="/login">Login</Link>}
              </div>
            </li>
          </ul>
        </div>
      </nav>
    </div>

    // <nav>

    //   {/* <Link to="/login"></Link> */}

    // </nav>
  );
};

export default NavBar;
