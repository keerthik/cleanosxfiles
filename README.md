# Clean up OSX Files

Deletes `._*` and `.DS_Store` files in recursively in all subfolders. These files are generated after using a drive with a Mac (OSX) computer. These are extraneous and pollute the file space when using the same drive with a Windows PC. Deleting these files will not hinder usage on an OSX device, although these files will be re-created.

## ⚠️ WARNING: Read before using

**Do not use this script on a boot drive or OSX system drive. This is for external/auxiliary drive use only!**

If you modify this script, or use it on an boot drive, you risk deletion of important system files and could render your device inoperable.

## Credit

The original script is from @pantuflip's [DeleteTempFiles](https://github.com/Pantuflip/DeleteTempFiles), before I fixed it to work on my drives and translated various prompts and text to English.