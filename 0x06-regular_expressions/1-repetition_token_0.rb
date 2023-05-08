#!/usr/bin/env ruby
# RegEx that matches (t) in the word not less than 2 or more than 5
# eg hbttn, hbtttn, hbttttn, hbtttttn

puts ARGV[0].scan(/hbt{2,5}n/).join
