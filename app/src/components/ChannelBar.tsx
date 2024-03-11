import React from "react";
import { Separator } from "../ui/Seperator";
import { Hash, LockIcon, Search } from "lucide-react";
import { Input } from "../ui/Input";

const ChannelBar = () => {
  return (
    <div className="flex flex-col justify-center">
      <header className="py-3">Code with Antonio</header>

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

      <p>Members</p>
    </div>
  );
};

export default ChannelBar;
