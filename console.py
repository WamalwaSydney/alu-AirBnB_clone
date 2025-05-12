#!/usr/bin/python3
"""Console entry point: implements HBNBCommand with cmd module."""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {
    'BaseModel': BaseModel,
    'User': User,
    'State': State,
    'City': City,
    'Amenity': Amenity,
    'Place': Place,
    'Review': Review
}


class HBNBCommand(cmd.Cmd):
    """Command interpreter for AirBnB clone."""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF to exit the program."""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def do_create(self, arg):
        """Create a new instance and print its id."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            obj = classes[args[0]]()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """Show string representation of an instance."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **"); return
        if args[0] not in classes:
            print("** class doesn't exist **"); return
        if len(args) < 2:
            print("** instance id missing **"); return
        key = f"{args[0]}.{args[1]}"
        obj = storage.all().get(key)
        print(obj if obj else "** no instance found **")

    def do_destroy(self, arg):
        """Destroy an instance by class name and id."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **"); return
        if args[0] not in classes:
            print("** class doesn't exist **"); return
        if len(args) < 2:
            print("** instance id missing **"); return
        key = f"{args[0]}.{args[1]}"
        objs = storage.all()
        if key in objs:
            del objs[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Print all string representations, optionally filtered by class."""
        args = shlex.split(arg)
        objs = storage.all()
        if not args:
            print([str(o) for o in objs.values()])
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            print([str(o) for k, o in objs.items() if k.startswith(args[0])])

    def do_update(self, arg):
        """Update an instance by adding/updating attribute."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **"); return
        if args[0] not in classes:
            print("** class doesn't exist **"); return
        if len(args) < 2:
            print("** instance id missing **"); return
        key = f"{args[0]}.{args[1]}"
        objs = storage.all()
        if key not in objs:
            print("** no instance found **"); return
        if len(args) < 3:
            print("** attribute name missing **"); return
        if len(args) < 4:
            print("** value missing **"); return

        obj = objs[key]
        name, value = args[2], args[3]
        if hasattr(obj, name):
            t = type(getattr(obj, name))
            try: setattr(obj, name, t(value))
            except: setattr(obj, name, value)
        else:
            setattr(obj, name, value)
        obj.save()

    def default(self, line):
        """Handle advanced <Class>.<command>() syntax."""
        import re, json
        m = re.fullmatch(r"(\w+)\.(\w+)\((.*)\)", line)
        if not m:
            print("** invalid syntax **"); return
        cls, cmd_name, args = m.groups()
        if cls not in classes:
            print("** class doesn't exist **"); return

        if cmd_name == "all":
            self.do_all(cls)
        elif cmd_name == "count":
            print(len([k for k in storage.all() if k.startswith(cls)]))
        elif cmd_name in ("show", "destroy"):
            arg0 = args.strip().strip('"')
            getattr(self, f"do_{cmd_name}")(f"{cls} {arg0}")
        elif cmd_name == "update":
            if args.strip().endswith('}'):
                id_str, dict_str = args.split(',',1)
                d = json.loads(dict_str.replace("'", '"'))
                for k,v in d.items():
                    self.do_update(f'{cls} {id_str.strip().strip(\'"\')} {k} "{v}"')
            else:
                parts = [p.strip() for p in args.split(',',2)]
                self.do_update(f'{cls} {parts[0].strip().strip(\'"\')} {parts[1].strip().strip(\'"\')} "{parts[2].strip().strip(\'"\')}"')

    def do_help(self, arg):
        """Show help for commands."""
        return super().do_help(arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
