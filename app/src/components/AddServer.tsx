import { Plus } from "lucide-react";
import { Button } from "../ui/Button";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "../ui/Dialog";
import { Input } from "../ui/Input";
import React from "react";
import axios from "axios";
import { Separator } from "../ui/Seperator";

const AddServer = () => {
  const [server, setServer] = React.useState<string>("");
  const handleSubmit = async () => {
    try {
      const data = await axios.post("/api/server/create/", server);
      console.log(data.status);
    } catch (error: any) {
      console.log(error);
      if (error.response.status === 401) {
        console.log("jdsfhkdsjfkdsf");
      }
    }
  };
  return (
    <div>
      <Dialog>
        <DialogTrigger>
          <Button className="hover:bg-green-600 bg-slate-800 rounded-full px-3 py-6">
            <Plus color="green" />
          </Button>

          <DialogContent color="white" className="max-w-lg min-h-64 ">
            <DialogHeader>
              <DialogTitle>Customize your server</DialogTitle>

              <DialogDescription>
                Give your server a personality with a name and an icon. You can
                always change it later.
              </DialogDescription>
            </DialogHeader>
            <div className="mt-2 gap-2 flex flex-col ">
              <p>SEVER NAME</p>
              <Input
                value={server}
                onChange={(e) => setServer(e.target.value)}
              />
            </div>

            <DialogFooter className="flex flex-col gap-2">
              <Button onClick={handleSubmit} className="bg-purple-500">
                Create{" "}
              </Button>
            </DialogFooter>
          </DialogContent>
        </DialogTrigger>
      </Dialog>
      <Separator className="my-3" />
    </div>
  );
};

export default AddServer;
