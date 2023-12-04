/* rexx */
/* Advent of Code 2023 - Mainframe - Day 2 - Challenge 2 */

/* Read Input Dataset containing game information into a stem variable */
input = "AOC9IT.AOC.DAY2.INPUT"
"alloc dd(input) da('"input"') shr"
"execio * diskr input (stem game_list. finis"

/* Establish maximum values for the dice */
total_power = 0

/* Loop through each game and calculate possible games */
do game = 1 to game_list.0
  call interpret_game game_list.game
  total_power = total_power + result
end
say total_power
exit

/* Interpret each Game to find the fewest number of dice */
interpret_game:
parse arg game_string
valid_game = 1
sets_left = 1
set_count = 1
fewest_red = 0
fewest_green = 0
fewest_blue = 0
parse var game_string junk ':' game_string
do while(sets_left)
  parse var game_string set ';' game_string
  sets.set_count = strip(set,'b')
  set_count = set_count + 1
  if index(game_string,';') = 0 then do
    sets.set_count = strip(game_string,'b')
    sets.0 = set_count
    sets_left = 0
  end
end
do set = 1 to sets.0
  call interpret_dice sets.set
  parse var result set_red set_green set_blue
  if set_red > fewest_red then
    fewest_red = set_red
  if set_green > fewest_green then 
    fewest_green = set_green
  if set_blue > fewest_blue then 
    fewest_blue = set_blue
end
game_power = fewest_red * fewest_green * fewest_blue
return game_power

/* Interpret each handful of dice to see if it's valid */
interpret_dice:
parse arg dice_string
dice_left = 1
red_dice = 0
green_dice = 0
blue_dice = 0
do while(dice_left)
  if index(dice_string,',') > 0 then
    parse var dice_string number color ',' dice_string
  else do
    parse var dice_string number color
    dice_left = 0
  end
  select
    when color == 'red' then
      do
        if number > red_dice then
          red_dice = number
      end
    when color == 'green' then
      do
        if number > green_dice then
          green_dice = number
      end
    when color == 'blue' then
      do
        if number > blue_dice then
          blue_dice = number
      end
    otherwise
      nop
  end
end
fewest_dice = red_dice||" "||green_dice||" "||blue_dice
return fewest_dice
