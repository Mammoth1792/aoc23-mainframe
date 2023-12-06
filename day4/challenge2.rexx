/* rexx */
/* Advent of Code 2023 - Mainframe - Day 4 - Challenge 2 */

/* Read Input Dataset containing game cards into a stem variable */
input = "AOC9IT.AOC.DAY4.INPUT"
"alloc dd(input) da('"input"') shr"
"execio * diskr input (stem list_of_cards. finis"
total_amount = 0
card_totals.0 = 216
do i = 1 to card_totals.0
  card_totals.i = 1
end
/* list_of_cards.0 */
do card = 1 to list_of_cards.0
  parse var list_of_cards.card junk ': ' set_of_numbers
  set_of_numbers = translate(set_of_numbers,'.',' ')
  parse var set_of_numbers possible_winning_numbers '|' numbers_you_have
  call calculate_points possible_winning_numbers numbers_you_have
  say "Card "||card||" had "||result||" matches"
  next_card = card + 1
  end_card = card + result
  duplicates = card_totals.card
  say "There are "||duplicates||" of Card "||card
  do count = next_card to end_card
    card_totals.count = card_totals.count + duplicates
    say "Card "||count||" has "||card_totals.count||" cards now"
  end
end
do i = 1 to card_totals.0
  total_amount = total_amount + card_totals.i
end
say total_amount
exit

calculate_points:
parse arg possible_winning_numbers numbers_you_have
/* Remove beginning/ending periods */
possible_winning_numbers = strip(possible_winning_numbers,'b','.')
numbers_you_have = strip(numbers_you_have,'b','.')

do i = 1 by 1 while possible_winning_numbers <> ''
  parse var possible_winning_numbers winning_number_set.i '.' possible_winning_numbers
  winning_number_set.i = strip(winning_number_set.i,'b')
end
winning_number_set.0 = i - 1

do i = 1 by 1 while numbers_you_have <> ''
  parse var numbers_you_have your_numbers_set.i '.' numbers_you_have
  your_numbers_set.i = strip(your_numbers_set.i,'b')
end
your_numbers_set.0 = i - 1

point_count = 0
do a = 1 to winning_number_set.0
  if winning_number_set.a == '' then iterate
  do b = 1 to your_numbers_set.0
      if your_numbers_set.b == '' then iterate
      if your_numbers_set.b == winning_number_set.a then do
          point_count = point_count + 1
          iterate
      end
  end
end

return point_count
