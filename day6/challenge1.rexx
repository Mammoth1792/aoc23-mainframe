/* rexx */
/* Advent of Code 2023 - Mainframe - Day 6 - Challenge 1 */

time_distance.0 = 4
time_distance.1 = 62 644
time_distance.2 = 73 1023
time_distance.3 = 75 1240
time_distance.4 = 65 1023

total_possibilities = 1

do race = 1 to time_distance.0
  possible_wins = 0
  parse var time_distance.race time_of_race distance_record
  do button_speed = 0 to time_of_race
    distance_traveled = (time_of_race - button_speed) * button_speed
    if distance_traveled > distance_record then
      possible_wins = possible_wins + 1
  end
  total_possibilities = total_possibilities * possible_wins
end

say total_possibilities
exit
