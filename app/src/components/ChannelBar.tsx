import React from "react";
import { Separator } from "../ui/Seperator";
import { Hash, LockIcon, Search } from "lucide-react";
import { Input } from "../ui/Input";
import { useSelector } from "react-redux";
import { axiosInstance } from "../axios/axiosInstance";

const ChannelBar = () => {
  const serverName = useSelector((state: any) => state.server.currentServer);
  const user = useSelector((state: any) => state.auth.user);
  const [members, setMembers] = React.useState([]);
  // console.log(serverName.members);

  React.useEffect(() => {
    fetchMembers();
  }, [serverName]);

  const fetchMembers = async () => {
    try {
      const res = await axiosInstance.get(
        `members/getMembers/${serverName.id}/`
      );
      setMembers(res.data.members);
      console.log(res.data);
    } catch (error) {
      console.log(error);
    }
  };
  return (
    <div className="flex flex-col justify-center">
      <header className="py-3">
        {serverName ? serverName.name : "Click a server"}{" "}
      </header>

      <Separator className="my-1 px-2" />

      <Input placeholder="Search" />

      <Separator />

      <div className="flex justify-between hover:bg-gray-900 items-center px-3 py-3">
        <main className="gap-3 flex ">
          <Hash />
          <p>general</p>
        </main>
        <LockIcon size={20} />
      </div>

      {user !== null && (
        <div>
          {members.map((member: any) => {
            return (
              <div>
                <p>{member.username}</p>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
};

export default ChannelBar;
