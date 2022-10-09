# Compare Two Directory And Remove Similar Files And Then Empty Directories

## Description

Compare two files based on 
1. relative paths
2. last updated date
3. size.

If **all three criteria** matches then remove files from the second location.
After removing the files it will remove empty directories as well.

## How to Test
1. Copy and paste one directory with many files and folders
2. Edit one or two files from the new pasted(second) directory
3. Create `config.py` file and assign absolute path to `BASE_DIR` and `BACKUP_DIR` variables.
4. Run code.
5. If you don't see any error, verify only updated files are there or not.
6. If you see an error or code did not work, [contact me](https://twitter.com/Sahil_Fruitwala).