#!/usr/bin/python
import csv

def main():
    print("Paste the below into the bottom of your .bashrc file \n--------------------")
    header = """ 
# User specific aliases and functions
if [ -z "$TMUX" ]; then
    tmux attach -t TM || tmux new -s TM
fi 

if [ "$TMUX" ]; then
  tmux rename-window $HOSTNAME
fi
"""
    print(header)
    # Read hosts.csv file and output bash aliases
    with open('hosts.csv', 'r') as csvfile:
        lines = csv.DictReader(csvfile)
        for line in lines:
            print("alias " + line["alias"] + "=\"tmux rename-window '" + line["alias"] + "'; ssh " + line["username"] + "@" + line["host"] + " | tee log/" + line["alias"] + "_\\$(date +%Y-%m-%d_%H:%M:%S).log\"") 
         
if __name__ == "__main__":
    main()