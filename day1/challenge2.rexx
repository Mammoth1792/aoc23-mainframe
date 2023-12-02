/* rexx */
/* Advent of Code 2023 - Mainframe - Day 1 - Challenge 2 */

/* Read Input Dataset containing calibration values into a stem variable */
input = "AOC9IT.AOC.DAY1.INPUT"
"alloc dd(input) da('"input"') shr"
"execio * diskr input (stem calibration_values. finis"

/* Establish total variable */
total = 0

/* Loop through each value */
do line = 1 to calibration_values.0
  call replace_numbers calibration_values.line
  call calculate_total result
  total = total + result
end
say total
exit

calculate_total:
parse arg input_text
/* Strip all non-numerical characters out of string */
translated_value = translate(input_text,,'abcdefghijklmnopqrstuvwxyz')
/* Remove leading/trailing blanks */
stripped_value = strip(translated_value,'b')
/* Provide left most and right most value */
left_value = left(stripped_value,1)
right_value = right(stripped_value,1)
/* Append them together */
calculated_value = left_value||right_value
return calculated_value

/* Not proud of this but it works! */
replace_numbers:
parse arg input_text
/* Calculate length of input text */
text_length = length(input_text)
do char = 1 to text_length
  if pos('one',input_text) == char then do
    input_text = overlay('1',input_text,char,2)
    iterate
  end
  if pos('two',input_text) == char then do
    input_text = overlay('2',input_text,char,2)
    iterate
  end
  if pos('three',input_text) == char then do
    input_text = overlay('3',input_text,char,2)
    iterate
  end
  if pos('four',input_text) == char then do
    input_text = overlay('4',input_text,char,2)
    iterate
  end
  if pos('five',input_text) == char then do
    input_text = overlay('5',input_text,char,2)
    iterate
  end
  if pos('six',input_text) == char then do
    input_text = overlay('6',input_text,char,2)
    iterate
  end
  if pos('seven',input_text) == char then do
    input_text = overlay('7',input_text,char,2)
    iterate
  end
  if pos('eight',input_text) == char then do
    input_text = overlay('8',input_text,char,2)
    iterate
  end
  if pos('nine',input_text) == char then do
    input_text = overlay('9',input_text,char,2)
    iterate
  end
end
return input_text
