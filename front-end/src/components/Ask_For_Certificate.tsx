import userData from "../data/users.json";
import { useAuth } from "../context/Auth";
export const Ask_For_Certificate = () => {
  const auth = useAuth();
  const foundUser = userData.users.find(
    (u) => u.id === auth.user.id && u.certificate_status_approval == ""
  );
  return (
    <div>
      {foundUser.certificate_status_approval === "" ? (
        <button className="w-[20] px-4 py-2 text-lg font-semibold text-white transition-colors duration-300 bg-blue-500 rounded-md shadow hover:bg-blue-600 focus:outline-none focus:ring-blue-200 focus:ring-4">
          Ask For Certificate
        </button>
      ) : foundUser.certificate_status_approval === "pending" ? (
        <p>Pending....</p>
      ) : (
        <a href="">See the certificate</a>
      )}
    </div>
  );
};
