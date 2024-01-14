import { useAuth } from "../context/Auth";
import { Ask_For_Certificate } from "../components/Ask_For_Certificate";
import { Approve_certificate } from "../components/Approve_certificate";
const Certificate = () => {
  const auth = useAuth();
  console.log(auth.user);
  return (
    <div>
      {auth.user.role == "Staff" ? (
        <Approve_certificate />
      ) : (
        <Ask_For_Certificate />
      )}
    </div>
  );
};

export default Certificate;
