import argparse
import sys
import os
import json

class CLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description='A basic CLI application',
            usage='''cli <command> [<args>]

Commands available:
   greet     Greet the user
   add       add task to the list
   delete    delete a task
   markd     put label on completed task
   markp     put label on progressing task
   lista     list all task
   listn     list all task that aren't done
   listy     list all task that are done
   listp     list all task that are in progres
''')
        self.parser.add_argument('command', help='Command to execute')
        self.commands = {
            'greet': self.greet,
            'add': self.add,
            'delete': self.delete,
            'markd': self.markd,
            'markp': self.markp,
            'lista': self.lista,
            'listn': self.listn,
            'listy': self.listy,
            'listp': self.listp
        }
        self.lt = 'lt.json'

    
    def load(self):
        if os.path.exists(self.lt):
            with open(self.lt, 'r') as f:
                return json.load(f)
        return []
    
    
    def save(self, tasks):
        with open(self.lt, 'w') as f:
            json.dump(tasks, f)

    
    def greet(self, name):
        parser = argparse.ArgumentParser(description='Greet the user')
        parser.add_argument('--g', default='User', help='Name to greet')
        name = parser.parse_args(name)
        print(f"Hello, {name.g}!")
        tasks = self.load()
        if tasks == []:
            print('you have not make a single list')
        else:
            print('u have list of:')
            for x in tasks:
                print(x)

    
    def add(self, args):
        parser = argparse.ArgumentParser(description='Add task ')
        parser.add_argument('--a', required=True, help='Task to add')
        parsed_args = parser.parse_args(args)
        tasks = self.load()
        if parsed_args.a in tasks:
            while True:
                usr = input(f'{parsed_args.a} already in task, do you still want to add it? y/n: ').lower()
                if usr in ['y', 'yes']:
                    tasks.append(parsed_args.a)
                    self.save(tasks)
                    print(f'add, "{parsed_args.a}" to the list')
                    break
                elif usr in ['n', 'no']:
                    print(f'{parsed_args.a} not added')
                    break
                else:
                    print('only yes/y or n/no')
        else:
            tasks.append(parsed_args.a)
            self.save(tasks)
            print(f'add, "{parsed_args.a}" to the list')
    
    
    def delete(self, args):
        parser = argparse.ArgumentParser(description='remove task ')
        parser.add_argument('--d', required=True, help='Task to remove')
        parsed_args = parser.parse_args(args)
        tasks = self.load()
        
        if parsed_args.d in tasks:
            tasks.remove(parsed_args.d)
            self.save(tasks)
            print(f'removed, "{parsed_args.d}" to the list')
        else:
            print(f'"{parsed_args.d}" is not in the list')

    
    def markd(self, args):
       parser = argparse.ArgumentParser(description='mark task ')
       parser.add_argument('--md', required=True, help='Mark Task') 
       parsed_args = parser.parse_args(args)
       tasks = self.load()
       if parsed_args.task in tasks:
           index = tasks.index('eat')
           word = parsed_args.task
           parsed_args.task = '^' + word
           tasks[index] = parsed_args.task
           self.save(tasks)
           print(f'task marked!')
       else:
           print(f'"{parsed_args.task}" is not in the list or already marked')
    
    
    def markp(self, args):
       parser = argparse.ArgumentParser(description='mark task ')
       parser.add_argument('--mp', required=True, help='Mark Task') 
       parsed_args = parser.parse_args(args)
       tasks = self.load()
       if parsed_args.task in tasks:
           index = tasks.index('eat')
           word = parsed_args.task
           parsed_args.task = '!' + word
           tasks[index] = parsed_args.task
           self.save(tasks)
           print(f'task marked!')
       else:
           print(f'"{parsed_args.task}" is not in the list or already marked')
 

    
    def lista(self, args):
        tasks = self.load() 
        if tasks == []:
            print('you have no task yet')
        else: 
            print('tasks:')
            print('\n')
            for x in tasks:
                print(x)

        
    
    def listn(self, task):
        tasks = self.load()
        lis = []
        for x in tasks:
            if x[0] != '^' and x[0] != '!':
                lis.append(x)
        if lis == []:
            print('you do not have uncomplete task')
        else:
            print('uncomplete task:')
            for x in lis:
                print(x)


 
    
    def listy(self, task):
        tasks = self.load()
        lis = []
        for x in tasks:
            if x[0] == '^':
                lis.append(x)
        if lis == []:
            print("you haven't completed any task")
        else:
            print('completed task:')
            print('\n')
            for x in lis:
                print(x)


    
    def listp(self, task):
        tasks = self.load()
        lis = []
        for x in tasks:
            if x[0] == '!':
                lis.append(x)
        if lis == []:
            print("you haven't progressing task")
        else:
            print('progressing task:')
            print('\n')
            for x in lis:
                print(x)

 
    def run(self):
        
        args = self.parser.parse_args(sys.argv[1:2])
        
        if args.command not in self.commands:
            print('Invalid command')
            self.parser.print_help()
            return
        
        
        self.commands[args.command](sys.argv[2:])

def main():
    cli = CLI()
    cli.run()

if __name__ == '__main__':
    main()
