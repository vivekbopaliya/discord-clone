import React from "react";
import { Avatar, AvatarFallback, AvatarImage } from "../ui/Avatar";
import { ThemeToggler } from "./ThemeToggler";
import AddServer from "./AddServer";
import { Button } from "../ui/Button";
import UserAuthentication from "./UserAuthentication";
import ServerList from "./ServerList";
import { UseSelector, useSelector } from "react-redux";

const ServerBar = () => {
  const user = useSelector((state: any) => state.auth.user);

  console.log(user);
  return (
    <div className="min-h-screen bg-black text-white flex flex-col justify-between">
      <div className="flex justify-center py-3 items-center">
        <AddServer />
      </div>

      <div>
        <ServerList />
      </div>

      <div className="flex flex-col py-3 items-center">
        <div className="py-3 px-2">
          <ThemeToggler />
        </div>

        {/* {user ? (
          <p>{user.name}</p>
        ) : ( */}
        <div className="mt-auto">
          <UserAuthentication />
        </div>
        {/* )} */}
      </div>
    </div>
  );
};

export default ServerBar;
