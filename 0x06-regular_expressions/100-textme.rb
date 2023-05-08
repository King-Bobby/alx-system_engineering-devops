#!/usr/bin/env ruby
# RegEx that matches and returns [sender], [receiver], [flag]

puts ARGV[0].scan(/\[(?:from:|to:|flags:)(.*?)\]/).join(',')
