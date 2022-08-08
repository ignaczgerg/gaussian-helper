import args

def insert(filepath:str, savepath: str, filetype: str):
    source_file = open(filepath, 'r')
    target_file = open(f"{savepath}/mod_{filetype}", 'w')
    first_row = True
    for row in source_file:
        if first_row:
            row = "%chk=test-4.chk\n%CPU=0-53\n# opt b3lyp/6-31g(d) geom=connectivity\n"
            first_row = False
        target_file.write(row)

args = args.JobCreatorArgs().parse_args()

def main():
    insert(args.filepath, args.savepath, args.filetype)

if __name__ == "__main__": 
    main()
