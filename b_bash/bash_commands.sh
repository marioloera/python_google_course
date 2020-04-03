grep ' jane ' ../data/list.txt

grep " jane " ../data/list.txt | cut -d ' ' -f 1

grep " jane " ../data/list.txt | cut -d ' ' -f 1-3

grep " jane " ../data/list.txt | cut -d ' ' -f 1,3

# cut lines based on -d (delimiter)
# -f return the fields separated by the delimiter

#defining a variable, no spaces next to equal sign
variable=434
echo $variable
# to create a new write a file or overwrite
echo 'first line'> file.txt

# >>  to append a file
echo 'second line'>> file.txt

# condititons 
# test evaluates expresion, -e returns true if 
# a file exists
if test -e ~/data/jane_profile_07272018.doc; 
then 
	echo "File exists"; 
else 
	echo "File doesn't exist"; 
fi

#for loop

for i in 1 2 3; 
do 
	echo $i; 
done

