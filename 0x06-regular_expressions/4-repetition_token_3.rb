#!/usr/bin/env ruby
# RegEx that matches hb(with 't' 0 or more times)n

puts ARGV[0].scan(/hbt*n/).join
