import { useAuth } from "../context/Auth";
import { useNavigate } from "react-router-dom";
const Home = () => {
  const auth = useAuth();
  const navigate = useNavigate();
  const handleLogout = () => {
    auth.logout();
    navigate("/login");
  };
  return (
    <>
      <div className="bg-gray-50 cs-font">
        <div id="wrapper" className="grid grid-cols-1 xl:grid-cols-2">
          <div id="col-2" className="px-3 md:px-20 xl:py-64 xl:px-12">
            <div
              id="cards"
              className="rounded-lg flex border py-5 px-6 md:py-8 md:px-16 -mt-6 bg-white xl:-ml-24 xl:pl-8 xl:rounded-xl"
            >
              <div
                id="circle"
                className="w-8 h-8 bg-blue-500 md:w-16 md:h-16 rounded-full"
              ></div>
              <p className="pl-4 md:pl-12 text-base pt-1 font-semibold md:text-2xl md:pt-4">
                Hello {auth.user.name}
              </p>
            </div>

            <div
              id="cards"
              className="rounded-lg flex border py-5 px-6 md:py-8 md:px-16 mt-6 md:mt-12 bg-white xl:pl-8 xl:rounded-xl"
            >
              <div
                id="circle"
                className="w-8 h-8 bg-blue-500 md:w-16 md:h-16 rounded-full"
              ></div>
              <p className="pl-4 md:pl-12 text-base pt-1 font-semibold md:text-2xl md:pt-4">
                {auth.user.role == "Staff"
                  ? "You can check for new certicate approval reques at certificate tab"
                  : "you can check for certicate approval status at certificate tab "}
              </p>
            </div>
          </div>
        </div>
        <div>
          <button
            className="w-[20] px-4 py-2 text-lg font-semibold text-white transition-colors duration-300 bg-blue-500 rounded-md shadow hover:bg-blue-600 focus:outline-none focus:ring-blue-200 focus:ring-4"
            onClick={handleLogout}
          >
            Log Out
          </button>
        </div>
      </div>
    </>
  );
};

export default Home;
