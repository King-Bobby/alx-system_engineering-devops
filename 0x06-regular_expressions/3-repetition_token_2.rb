#!/usr/bin/env ruby
# RegEx that matches hbtn, hbtttn and not hbn

puts ARGV[0].scan(/hbt+n/).join
