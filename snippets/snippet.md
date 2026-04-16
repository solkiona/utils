# Merge all .tsx and .css files into a single file

This snippet combines all `.tsx` and `.css` files inside the `src/` directory (including subdirectories) into a single file called `UIcontext.txt`.  
It also adds headers to indicate the original file paths.

---

## Bash Command Snippet

```bash
# Remove old output if exists
rm -f UIcontext.txt

# Traverse src/ recursively, select .tsx and .css, exclude node_modules
find src -type f \( -name "*.tsx" -o -name "*.css" \) \
  ! -path "*/node_modules/*" \
  | sort \
  | while read f; do
      echo "----- FILE: $f -----" >> UIcontext.txt
      cat "$f" >> UIcontext.txt
      echo "" >> UIcontext.txt
    done

echo "✅ UIcontext.txt created!"

# Single one line code, change the extensions for reusability
find src -type f \( -name "*.tsx" -o -name "*.css" \) -exec sh -c 'echo "----- FILE: {} -----" >> UIcontext.txt; cat "{}" >> UIcontext.txt; echo "\n" >> UIcontext.txt' \;

# added another file type -0 -name "*.ts"
find src -type f \( -name "*.tsx" -o -name "*.ts" \) \
  -exec sh -c 'echo "----- FILE: {} -----" >> UIcontext.txt; cat "{}" >> UIcontext.txt; echo "\n" >> UIcontext.txt' \;



#entire backend context , scans all folders
find . -type f -name "*.py" \
  ! -path "*/venv/*" \
  ! -path "*/__pycache__/*" \
  ! -path "*/migrations/*" \
  ! -name "__init__.py" \
  -exec sh -c 'echo "----- FILE: {} -----" >> BACKENDcontext.txt; cat "{}" >> BACKENDcontext.txt; echo "\n" >> BACKENDcontext.txt' \;


#backend context peculiar to specific app folders
find accounts commissions transactions wallets withdrawals utilities core \
  -type f -name "*.py" \
  ! -path "*/migrations/*" \
  ! -name "__init__.py" \
  -exec sh -c 'echo "----- FILE: {} -----" >> BACKENDcontext.txt; cat "{}" >> BACKENDcontext.txt; echo "\n" >> BACKENDcontext.txt' \;

#Write your test result to file while viewing on the stdout
python manage.py test --verbosity=2 2>&1 | tee test_result.txt


