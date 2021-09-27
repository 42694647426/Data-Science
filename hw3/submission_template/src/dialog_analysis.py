import pandas as pd
import getopt, sys
import json
def generate_json(dialog: pd.DataFrame, output_path: str):
    pony = ["twilight sparkle", "applejack", "rarity", "pinkie pie", "rainbow dash", "fluttershy"]
    output = {"count":dict.fromkeys(pony, 0),"verbosity":dict.fromkeys(pony, 0)}
    for index, row in dialog.iterrows():
        ponies = [p for p in pony if p in row["pony"].lower()]
        if ponies:
            for p in ponies: 
                output["count"][p] +=1
    for i in pony:
        output["verbosity"][i] = output["count"][i] / dialog.shape[0]
    with open(output_path, 'w') as f:
        json.dump(output, f)
    return

if __name__ == "__main__":
    argumentList = sys.argv[1:]
    # Options
    options = "hmo:"
    # Long options
    long_options = ["Help", "My_file", "Output ="]

    try:
        # Parsing argument
        arguments, values = getopt.getopt(argumentList, options, long_options)
        
        # checking each argument
        for currentArgument, currentValue in arguments:
            if currentArgument in ("-o", "--Output"):
                path = str(sys.argv[-1])
                dialog = pd.read_csv(path)
                generate_json(dialog, currentValue)
                
    except getopt.error as err:
        # output error, and return with an error code
        print (str(err))
    
    
