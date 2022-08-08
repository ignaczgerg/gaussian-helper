import args

def parseFromFile(filepath: str, split_char: str, savepath: str, filetype: str):
    """
    :filepath: Path to the file to be splitted
    :split_char: string entries which by the original file will be splitted. 
    :save_path: to save the file to the given folder
    """
    print(split_char)
    print(filepath)
    parsedListFromFile = []
    unended_item = False
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            if line.find(split_char)!=-1 or unended_item: 
                if line.find(split_char) != -1: #says that there is \item present in line
                    parsedListFromFile.append(split_char+line.split(split_char)[-1])
                    unended_item=True  
                else:
                    parsedListFromFile[-1]+=line.split(split_char)[-1]
            line = fp.readline()

    #write each item of parseListFromFile to file
    for index, item in enumerate(parsedListFromFile):
        with open(savepath+str(index)+'.'+filetype, 'w') as out:
            out.write(item)

args = args.SplitterArgs().parse_args()

def main():
    parseFromFile(args.filepath, args.split_chars, args.savepath, args.filetype) #call function for each file

if __name__ == "__main__": 
    main()
