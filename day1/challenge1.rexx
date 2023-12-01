/* rexx */
/* Advent of Code 2023 - Mainframe - Day 1 - Challenge 1 */

/* Read Input Dataset containing calibration values into a stem variable */
input = "AOC9IT.AOC.DAY1.INPUT"
"alloc dd(input) da('"input"') shr"
"execio * diskr input (stem calibration_values. finis"

/* Setting initial variable */
total = 0

/* Loop through each value */
do line = 1 to calibration_values.0
  call calculate_total calibration_values.line
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
