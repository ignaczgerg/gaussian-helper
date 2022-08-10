import args

### M062X method ###


def insert(filepath:str, savepath: str, filetype: str, id:str):
    source_file = open(filepath, 'r')
    target_file = open(f"{savepath}/{id}_in{filetype}", 'w')
    first_row = True
    for row in source_file:
        if first_row:
            row = f"%chk={id}_out.chk\n%CPU=0-53\n%mem=4GB\n# opt M062X/6-31+G(d,p) geom=connectivity integral=ultrafine\n"
            first_row = False
        target_file.write(row)

args = args.JobCreatorArgs().parse_args()

def main():
    insert(args.filepath, args.savepath, args.filetype, args.id)

if __name__ == "__main__": 
    main()
