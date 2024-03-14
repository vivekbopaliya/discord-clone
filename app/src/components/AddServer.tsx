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
import React, { useContext } from "react";
import { Separator } from "../ui/Seperator";
import { useToast } from "../ui/use-toast";
import AuthContext from "../store/AuthContext";
import useAuth from "../hooks/useAuth";
import useAxiosPrivate from "../hooks/useAxiosPrivate";

const AddServer = () => {
  const { accessToken, csrftoken } = useAuth();
  const [server, setServer] = React.useState<string>("");
  const { toast } = useToast();
  const axiosPrivateInstance = useAxiosPrivate();

  console.log(accessToken, csrftoken);
  const handleSubmit = async () => {
    const res = await axiosPrivateInstance.post("server/create/", {
      name: server,
    });
    console.log(res.data);
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
              {/* @ts-ignore */}
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
