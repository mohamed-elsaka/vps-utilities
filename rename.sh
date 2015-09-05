for FILE in *.avi; 
	if [[ $FILE == *"03c"* ]] then
		do $newFile = ${$FILE//03/_};
  		do mv "$FILE" "$newFile";
	fi 
done;
