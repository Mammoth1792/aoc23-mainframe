/* rexx */
/* Advent of Code 2023 - Mainframe - Day 2 - Challenge 1 */

/* Read Input Dataset containing game information into a stem variable */
input = "AOC9IT.AOC.DAY2.INPUT"
"alloc dd(input) da('"input"') shr"
"execio * diskr input (stem game_list. finis"

/* Establish maximum values for the dice */
red_max = 12
green_max = 13
blue_max = 14
game_total = 0

/* Loop through each game and calculate possible games */
do game = 1 to game_list.0
  call interpret_game game_list.game
  if result = 1 then
    game_total = game_total + game
end
say game_total
exit

/* Interpret each Game to see if it's valid */
interpret_game:
parse arg game_string
valid_game = 1
sets_left = 1
set_count = 1
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
  if result = 0 then do
    valid_game = 0
    leave
  end
end
return valid_game

/* Interpret each handful of dice to see if it's valid */
interpret_dice:
parse arg dice_string
valid_set = 1
dice_left = 1
do while(dice_left & valid_set)
  parse var dice_string number color ',' dice_string
  valid_set = interpret_color(color, number)
  if valid_set = 0 then leave
  if index(dice_string,',') = 0 then do
    parse var dice_string number color
    valid_set = interpret_color(color, number)
    dice_left = 0
  end
end
return valid_set

/* Interpret if the amount of dice exceeds possible amount */
interpret_color:
color = strip(arg(1),'b')
number = strip(arg(2),'b')
valid_dice = 1
select
  when color == 'red' then 
    do
      if number > red_max then
        valid_dice = 0
    end
  when color == 'green' then 
    do
      if number > green_max then
        valid_dice = 0
    end
  when color == 'blue' then 
    do
      if number > blue_max then
        valid_dice = 0
    end
  otherwise
    nop
end
return valid_dice