import React from "react";
import { Avatar, AvatarFallback, AvatarImage } from "../ui/Avatar";
import { ThemeToggler } from "./ThemeToggler";
import AddServer from "./AddServer";

const ServerBar = () => {
  return (
    <div className="min-h-screen bg-black text-white flex flex-col justify-between">
      <div className="flex justify-center py-3 items-center">
        <AddServer />
      </div>

      <div className="flex flex-col py-3 items-center">
        <div className="py-3 px-2">
          <ThemeToggler />
        </div>
        <div className="mt-auto">
          <Avatar>
            <AvatarImage src="https://github.com/shadcn.png" />
            <AvatarFallback>Image</AvatarFallback>
          </Avatar>
        </div>
      </div>
    </div>
  );
};

export default ServerBar;
