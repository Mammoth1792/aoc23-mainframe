/* rexx */
/* Advent of Code 2023 - Mainframe - Day 5 - Challenge 1 */

/* Read Input Dataset containing game cards into a stem variable */
input = "AOC9IT.AOC.DAY5.INPUT"
"alloc dd(input) da('"input"') shr"
"execio * diskr input (stem almanac. finis"

map_count = 1

/* Parse all the numbers and such */
do line = 1 to almanac.0
  select
    /* Parse out Seeds */
    when index(almanac.line, 'seeds:') > 0 then
      do
        parse var almanac.line 'seeds:' seed_numbers
        do number = 1 by 1 while seed_numbers <> ''
          parse var seed ' ' seed_numbers
          seeds.number = seed
        end
        seeds.0 = number - 1
      end
    /* Parse out Map values */
    when index(almanac.line, 'map:') > 0 then
      do
        map_line_counter = 0
        map_line_left = 1
        line = line + 1
        do i = 1 to almanac.0
          map_line_counter = map_line_counter + 1
          almanac_maps.map_count.map_line_counter = strip(almanac.line,'b')
          say "Line: "||strip(almanac.line,'b')
          line = line + 1
          if strip(almanac.line,'b') == '' then leave
        end
        almanac_maps.map_count.0 = map_line_counter
        map_count = map_count + 1
      end
    otherwise nop
  end
end

/* Run through each Seed and it's various maps */

do seed = 1 to seeds.0
  pointer = seeds.i
  do map = 1 to almanac_maps.0
    do value = 1 to almanac_maps.maps.0
      parse var almanac_maps.maps.value destination_range_start source_range_start range_length
      source_range_end = source_range_start + range_length
      if pointer >= source_range_start & pointer <= source_range_end then
        do
          range_indexer = pointer - source_range_start
          pointer = range_indexer + destination_range_start
          leave
        end
    end
  end
  location.i = pointer
end
do i = 1 to seeds.0
  say location.i
end
exit